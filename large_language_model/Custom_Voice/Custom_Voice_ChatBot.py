import os
from pathlib import Path
import tempfile
import time

import mimetypes, base64, streamlit as st, os
from audio_recorder_streamlit import audio_recorder
from dotenv import load_dotenv
from IPython.display import Audio, display

from openai import OpenAI
from TTS.api import TTS
from pydub import AudioSegment

# -----------------------------------------------------------
# 기본 설정 / 스타일
# -----------------------------------------------------------
st.set_page_config(
    page_title="학우들 보이스 기반 고민 상담 챗봇",
    page_icon="🎙️",
    layout="wide",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@300;400;600;700&display=swap');
html, body, [class*="css"]  { font-family: 'Pretendard', system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif; }
.kicker { font-size: 14px; letter-spacing: .12em; text-transform: uppercase; opacity: .75; }
.hero-title { font-size: 28px; font-weight: 700; margin-top: 6px; }
.hero-sub { font-size: 15px; opacity: .85; margin-top: 4px; }
.chip { display: inline-block; padding: 6px 10px; border-radius: 999px; background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.08); margin-right: 8px; font-size: 12px; }
.msg-row { display: flex; gap: 12px; margin-bottom: 14px; }
.msg-user, .msg-assistant {
  max-width: 100%;
  border-radius: 14px; padding: 12px 14px; border: 1px solid rgba(255,255,255,.08);
  box-shadow: 0 6px 18px rgba(0,0,0,.25);
}
.msg-user { background: rgba(59,130,246,.10); }
.msg-assistant { background: rgba(16,185,129,.10); }
.avatar { width: 36px; height: 36px; border-radius: 999px; background: rgba(255,255,255,.12); display:flex; align-items:center; justify-content:center; }
.small { font-size: 12px; opacity: .8; }
.btn-row { display:flex; gap:10px; }
.spacer16 { height: 16px; }
.spacer8 { height: 8px; }
.audio-wrapper { border-radius: 12px; overflow: hidden; border:1px solid rgba(255,255,255,.08); }
hr.smooth { border: none; border-top: 1px solid rgba(255,255,255,.08); margin: 14px 0; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# 환경/리소스 로드
# -----------------------------------------------------------
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

@st.cache_resource(show_spinner=False)
def get_openai():
    if not OPENAI_API_KEY:
        st.error("OPENAI_API_KEY가 설정되지 않았습니다 (.env 확인).")
    return OpenAI(api_key=OPENAI_API_KEY)

@st.cache_resource(show_spinner=False)
def load_tts_model():
    # 터미널에서 쓰던 XTTS v2
    return TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

client = get_openai()
tts = load_tts_model()

# -----------------------------------------------------------
# 상수/유틸 (짧은 녹음 방지)
# -----------------------------------------------------------
MIN_REC_SECONDS = 0.30

def wav_duration_sec(path: Path) -> float:
    """WAV 길이를 초 단위로 반환 (에러 시 0)"""
    try:
        seg = AudioSegment.from_file(path)
        return len(seg) / 1000.0
    except Exception:
        return 0.0

# -----------------------------------------------------------
# 스피커 레퍼런스 폴더
# -----------------------------------------------------------
BASE_SPK_DIR = Path("dataset/wavs")
BASE_SPK_DIR.mkdir(parents=True, exist_ok=True)

def list_reference_wavs():
    if not BASE_SPK_DIR.exists():
        return []
    return sorted([p for p in BASE_SPK_DIR.glob("*.wav") if p.is_file()])

# -----------------------------------------------------------
# 유틸: 파일 저장 / ASR / LLM / TTS / 자동재생
# -----------------------------------------------------------
def _save_audio_bytes_to_wav(audio_bytes: bytes, out_path: Path) -> Path:
    out_path = out_path.with_suffix(".wav")
    with open(out_path, "wb") as f:
        f.write(audio_bytes)
    return out_path

def transcribe_wav_with_openai(wav_path: Path) -> str:
    if wav_duration_sec(wav_path) < 0.10:
        raise ValueError("녹음이 너무 짧습니다. 0.3초 이상 말씀해 주세요.")

    with open(wav_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language="ko"
        )
    return transcript.text.strip()

def chat_reply(messages, temperature: float = 0.3) -> str:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=temperature,
        messages=messages
    )
    return completion.choices[0].message.content.strip()

def synthesize_tts_ko(text: str, speaker_refs, out_path: Path):
    out_path = out_path.with_suffix(".wav")
    spk_ref_paths = [str(p) for p in speaker_refs] if speaker_refs else None
    tts.tts_to_file(
        text=text,
        file_path=str(out_path),
        speaker_wav=spk_ref_paths,
        language="ko"
    )
    return out_path

def autoplay_audio(file_path: str, hidden: bool = True):
    if not os.path.exists(file_path):
        st.error(f"오디오 파일을 찾을 수 없습니다: {file_path}")
        return

    mime, _ = mimetypes.guess_type(file_path)
    if mime is None:
        ext = os.path.splitext(file_path)[1].lower()
        mime = "audio/mpeg" if ext == ".mp3" else "audio/wav" if ext in (".wav", ".wave") else "audio/mp4"

    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()

    hidden_attr = " hidden" if hidden else ""
    html = f"""
    <audio id="intro-audio" autoplay muted playsinline{hidden_attr}>
        <source src="data:{mime};base64,{b64}" type="{mime}">
    </audio>
    <script>
      const a = document.getElementById('intro-audio');
      // iOS/Chrome 정책: 첫 제스처 때 소리 켜고 재생 시도
      function resume() {{
        try {{
          a.muted = false;
          if (a.paused) a.play().catch(()=>{{}});
        }} catch(_) {{}}
        window.removeEventListener('pointerdown', resume);
        window.removeEventListener('keydown', resume);
        window.removeEventListener('touchstart', resume);
      }}
      window.addEventListener('pointerdown', resume, {{once:true}});
      window.addEventListener('keydown', resume, {{once:true}});
      window.addEventListener('touchstart', resume, {{once:true}});
    </script>
    """
    st.markdown(html, unsafe_allow_html=True)

def autoplay_audio(file_path, hidden=False):
    """
    오디오 파일을 자동 재생하는 함수.
    - file_path: 문자열(단일 파일) 또는 리스트(여러 파일)
    - hidden: True면 플레이어 숨김, False면 플레이어 표시
    """
    
    def _play_single(f):
        if not os.path.exists(f):
            raise FileNotFoundError(f"{f} not found.")
        audio = Audio(f, autoplay=True)
        display(audio)
    
    if isinstance(file_path, list):
        for f in file_path:
            _play_single(f)
    else:
        _play_single(file_path)

# -----------------------------------------------------------
# 세션 스테이트
# -----------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "너는 친절한 고민 상담가야. 한국어로 공감하고 구체적인 조언을 제공해."}
    ]
if "temperature" not in st.session_state:
    st.session_state.temperature = 0.3
if "last_user_audio" not in st.session_state:
    st.session_state.last_user_audio = None
if "autoplay" not in st.session_state:
    st.session_state.autoplay = True

# -----------------------------------------------------------
# 헤더 / 인트로
# -----------------------------------------------------------
with st.container():
    st.markdown('<div class="kicker">Intro</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">학우들 보이스 데이터 기반 고민 상담 챗봇</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">데이터 출처 — 정의중님, 최동현님 목소리</div>', unsafe_allow_html=True)
    st.markdown('<div class="spacer8"></div>', unsafe_allow_html=True)
    st.markdown('<span class="chip">🎙️ 마이크로 고민을 말해보세요</span> <span class="chip">🧠 LLM 응답</span> <span class="chip">🔊 보이스 응답(자동 재생)</span>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
            
        
st.markdown('<div class="spacer16"></div>', unsafe_allow_html=True)

# -----------------------------------------------------------
# 사이드바: 설정
# -----------------------------------------------------------
with st.sidebar:
    st.header("⚙️ 설정")
    st.session_state.temperature = st.slider("창의성 (temperature)", 0.0, 1.5, st.session_state.temperature, 0.1)

    ref_list = list_reference_wavs()
    if ref_list:
        ref_labels = [p.name for p in ref_list]
        sel = st.multiselect("스피커 레퍼런스(.wav)", ref_labels, default=ref_labels[:1])
        speaker_refs = [p for p in ref_list if p.name in sel]
    else:
        st.info("dataset/wavs 폴더에 화자 레퍼런스 .wav를 넣으면 보이스가 더 자연스럽습니다.")
        speaker_refs = []

    st.toggle("🔊 답변 자동 재생", value=st.session_state.autoplay, key="autoplay")

    st.markdown("---")
    if st.button("🗑️ 대화 초기화"):
        st.session_state.messages = [
            {"role": "system", "content": "너는 친절한 고민 상담가야. 한국어로 공감하고 구체적인 조언을 제공해."}
        ]
        st.rerun()

# -----------------------------------------------------------
# 메인: 녹음 → 텍스트 → 응답 → TTS(자동 재생)
# -----------------------------------------------------------
col_left, col_right = st.columns([1.1, 1])

with col_left:
    st.subheader("🎧 녹음")
    st.caption("버튼을 누르고 고민을 말하세요. 말이 끝나면 버튼을 다시 눌러 녹음을 종료합니다.")
    audio_bytes = audio_recorder(
        pause_threshold=1.0,
        sample_rate=44100,
        text="",
        icon_size="2x",
        recording_color="#22c55e",
        neutral_color="#374151"
    )

    if audio_bytes:
        if len(audio_bytes) < 4000:
            st.warning("녹음이 너무 짧아요. 최소 0.3초 이상 말해주세요.")
            st.stop()

        tmp_wav_path = Path(tempfile.gettempdir()) / f"user_rec_{int(time.time())}.wav"
        _save_audio_bytes_to_wav(audio_bytes, tmp_wav_path)

        st.session_state.last_user_audio = str(tmp_wav_path)

        try:
            with st.spinner("⏳ 음성 → 텍스트 변환 중..."):
                user_input = transcribe_wav_with_openai(tmp_wav_path)
        except Exception as e:
            st.error(f"음성 인식 중 오류: {e}")
            st.stop()

        with st.container():
            st.markdown("**나:**")
            st.write(user_input)
            st.markdown('<div class="audio-wrapper">', unsafe_allow_html=True)
            st.audio(audio_bytes, format="audio/wav")
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        st.session_state.messages.append({"role": "user", "content": user_input})

with col_right:
    st.subheader("💬 대화")
    hist = [m for m in st.session_state.messages if m["role"] in ("user", "assistant")]
    for m in hist:
        if m["role"] == "user":
            st.markdown('<div class="msg-row">', unsafe_allow_html=True)
            st.markdown('<div class="avatar">🧑</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="msg-user">{m["content"]}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="msg-row">', unsafe_allow_html=True)
            st.markdown('<div class="avatar">🤖</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="msg-assistant">{m["content"]}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    if 'audio_bytes' in locals() and audio_bytes:
        with st.spinner("🧠 생각 중..."):
            assistant_text = chat_reply(st.session_state.messages, temperature=st.session_state.temperature)

        st.session_state.messages.append({"role": "assistant", "content": assistant_text})

        with st.spinner("🔊 보이스 생성 중..."):
            out_path = Path(tempfile.gettempdir()) / f"assistant_{int(time.time())}.wav"
            synthesize_tts_ko(assistant_text, speaker_refs, out_path)
            out_path_str = str(out_path)

        st.markdown("**🧔🏻‍♂️ 정의중(보이스):**")
        st.write(assistant_text)

        if st.session_state.autoplay:
            autoplay_audio(out_path_str)

        st.markdown('<div class="audio-wrapper">', unsafe_allow_html=True)
        st.audio(out_path_str)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
