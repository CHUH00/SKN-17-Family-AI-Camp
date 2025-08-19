import streamlit as st
import pandas as pd
from joblib import load
import plotly.express as px
import numpy as np

# --- 페이지 설정 ---
st.set_page_config(page_title="사용자 이탈 예측", page_icon="🤖", layout="wide")

# --- 스타일 ---
st.markdown("""
<style>
.result-banner {
  padding: 16px 20px; border-radius: 12px; font-size: 1.05rem; display:flex;
  align-items:center; gap:10px; margin-bottom: 14px;
}
.result-banner.success { background:#ecf9f1; border:1px solid #b7e4c7; color:#1b5e20; }
.result-banner.error   { background:#fdecec; border:1px solid #ffb3b3; color:#b00020; }

/* 가운데 정렬용 래퍼 */
.result-center-wrapper {
  display: flex;
  justify-content: center;  /* 가로 중앙 */
  align-items: center;      /* 세로 정렬(카드 높이 기준) */
  margin-top: 16px;
  margin-bottom: 16px;
}

/* 확률 카드 - 더 길고 크게 */
.big-card {
  background:#ffffff; border:1px solid #e6e6e6; border-radius:20px;
  padding:40px 80px; /* 패딩 크게 */
  box-shadow:0 4px 12px rgba(0,0,0,0.08);
  text-align:center;
  width: clamp(520px, 60vw, 900px); /* 화면 비율에 따라 길게 */
  min-height: 220px;               /* 높이 크게 */
  display:flex; flex-direction:column; justify-content:center; align-items:center;
  transition: all 0.2s ease-in-out;
}
.big-card:hover { box-shadow:0 8px 22px rgba(0,0,0,0.12); transform: translateY(-3px); }
.big-card .label { font-size:1.35rem; color:#555; margin-bottom:12px; }
.big-card .value { font-size: clamp(2.6rem, 5vw, 4.2rem); font-weight:800; line-height:1.1; }

/* 모바일 대응 */
@media (max-width: 680px) {
  .big-card { padding:28px 24px; width: 92vw; min-height: 180px; }
  .big-card .label { font-size:1.1rem; }
}

/* Plotly 여백 살짝 */
.block-container { padding-top: 1.2rem; }
</style>
""", unsafe_allow_html=True)

# --- 모델 및 데이터 로드 ---
@st.cache_resource
def load_model():
    try:
        return load("xgb_model.joblib")
    except FileNotFoundError:
        st.error("오류: 'xgb_model.joblib' 파일이 없습니다. 현재 디렉토리에 파일이 있는지 확인하세요.")
        return None

@st.cache_data
def load_results_data():
    try:
        return pd.read_csv("test_predictions.csv")
    except FileNotFoundError:
        st.error("오류: 'test_predictions.csv' 파일이 없습니다. 현재 디렉토리에 파일이 있는지 확인하세요.")
        return None

model = load_model()
results_df = load_results_data()

# --- 메인 ---
if model is not None and results_df is not None:
    st.title("📈 사용자 이탈 예측 모델")
    st.write("사용자의 활동 정보를 입력하여 이탈 가능성을 예측해 보세요.")
    st.markdown("---")

    with st.container(border=True):
        st.header("🔍 사용자 데이터로 이탈 예측")
        st.info("아래에 사용자 데이터를 입력하고 예측 버튼을 눌러보세요.")

        # 입력 구역
        col_left, col_right = st.columns(2)
        with col_left:
            st.markdown("##### 개인 정보")
            gender_x_label = st.selectbox("성별", ["남성", "여성"])
            gender_x = 2 if gender_x_label == "여성" else 1

            mar_x_label = st.selectbox("결혼 여부", ["미혼", "기혼", "사별", "이혼"])
            mar_x_map = {"미혼": 1, "기혼": 2, "사별": 3, "이혼": 4}
            mar_x = mar_x_map[mar_x_label]

            relig_x_label = st.selectbox(
                "종교",
                ["무교", "불교", "기독교(개신교)", "기독교(천주교)", "유교", "원불교", "증산교", "천도교", "대증교", "기타"]
            )
            relig_x_map = {"무교":0,"불교":1,"기독교(개신교)":2,"기독교(천주교)":3,"유교":4,"원불교":5,"증산교":6,"천도교":7,"대증교":8,"기타":9}
            relig_x = relig_x_map[relig_x_label]

            time_y = st.slider("연 평균 이용시간 (분)", 0, 1000, 500)

        with col_right:
            st.markdown("##### 미디어 이용 행태")
            y19, y24 = st.columns(2)

            with y19:
                st.caption("0=거의 안 함 ~ 11=매우 자주")
                d01_x = st.slider("게시글 확인", 0, 11, 5, key="19_d01_x")
                d02_x = st.slider("게시글 작성", 0, 11, 5, key="19_d02_x")
                d03_x = st.slider("게시글 공유", 0, 11, 5, key="19_d03_x")
                d04_x = st.slider("댓글/좋아요", 0, 11, 5, key="19_d04_x")

            with y24:
                st.caption("0=거의 안 함 ~ 11=매우 자주")
                d01_y = st.slider("게시글 확인", 0, 11, 5, key="24_d01_y")
                d02_y = st.slider("게시글 작성", 0, 11, 5, key="24_d02_y")
                d03_y = st.slider("게시글 공유", 0, 11, 5, key="24_d03_y")
                d04_y = st.slider("댓글/좋아요", 0, 11, 5, key="24_d04_y")

        st.markdown("---")

        # 버튼
        if st.button("이탈 예측 결과 확인하기 🚀", use_container_width=True):
            user_data = pd.DataFrame({
                "gender_x":[gender_x], "mar_x":[mar_x], "relig_x":[relig_x],
                "d01_x":[d01_x], "d02_x":[d02_x], "d03_x":[d03_x], "d04_x":[d04_x],
                "d01_y":[d01_y], "d02_y":[d02_y], "d03_y":[d03_y], "d04_y":[d04_y],
                "time_y":[time_y]
            })
            expected_features = ["gender_x","mar_x","relig_x","d01_x","d02_x","d03_x","d04_x",
                                 "d01_y","d02_y","d03_y","d04_y","time_y"]
            user_data = user_data[expected_features]

            try:
                pred = model.predict(user_data)
                if hasattr(model, "predict_proba"):
                    proba = model.predict_proba(user_data)[0]
                else:
                    df_val = model.decision_function(user_data)
                    p1 = 1/(1+np.exp(-df_val))
                    proba = np.array([1-p1[0], p1[0]])

                # 결과 영역
                st.markdown("---")

                # 배너
                if pred[0] == 1:
                    st.markdown('<div class="result-banner error">예측 결과: <b>이탈할 가능성이 높음</b> ❗</div>', unsafe_allow_html=True)
                    label_text = "이탈 확률"
                    pct = proba[1] * 100
                else:
                    st.markdown('<div class="result-banner success">예측 결과: <b>이탈하지 않을 가능성이 높음</b> 🎉</div>', unsafe_allow_html=True)
                    label_text = "비이탈 확률"
                    pct = proba[0] * 100

                # 중앙 카드 (길고 크게)
                st.markdown(
                    f'''
                    <div class="result-center-wrapper">
                      <div class="big-card">
                        <div class="label">{label_text}</div>
                        <div class="value">{pct:.2f}%</div>
                      </div>
                    </div>
                    ''',
                    unsafe_allow_html=True
                )

                # 특성 중요도(옵션)
                if hasattr(model, "feature_importances_"):
                    st.markdown("---")
                    st.subheader("변수별 영향도")
                    feat_df = pd.DataFrame({
                        "feature": expected_features,
                        "importance": model.feature_importances_
                    }).sort_values("importance", ascending=False)
                    fig = px.bar(
                        feat_df, x="feature", y="importance",
                        title="이탈 예측에 영향을 미치는 주요 변수",
                        color="importance", color_continuous_scale=px.colors.sequential.Blues
                    )
                    st.plotly_chart(fig, use_container_width=True)

            except Exception as e:
                st.error(f"예측 중 오류가 발생했습니다: {e}")

    st.markdown("---")
    st.markdown("© 2025 Streamlit")
