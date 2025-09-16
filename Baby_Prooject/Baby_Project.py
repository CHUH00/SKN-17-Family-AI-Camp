import requests, json, os, time, re
from bs4 import BeautifulSoup
from collections import defaultdict

BASE = 'https://www.childcare.go.kr/?menuno={id}'
OUTFILE = 'childcare_pages.json'
headers = {"User-Agent": "Mozilla/5.0"}

def parse_page(html: str) -> dict:
    bs = BeautifulSoup(html, 'lxml')
    data = defaultdict(list)
    current_title = None
    need_span_title = False

    # 기존 selector (제목, 본문, 리스트)
    selector = (
        'h4.title_line, h5.title_line, '
        'span.text_box, '
        'p.txt, '
        'ul[class*="dot_list_blue"] > li'
    )

    for el in bs.select(selector):
        if el.name in ('h4', 'h5') and 'title_line' in el.get('class', []):
            title_text = el.get_text(strip=True)
            if title_text == '궁금해요':
                need_span_title = True
                current_title = None
                continue
            current_title = el.get_text(separator=' ', strip=True)
            _ = data[current_title]

        elif el.name == 'span' and 'text_box' in el.get('class', []):
            if need_span_title:
                current_title = el.get_text(separator=' ', strip=True)
                _ = data[current_title]
                need_span_title = False

        elif el.name == 'p' and 'txt' in el.get('class', []):
            if current_title and not el.find('span'):
                text = ' '.join(el.get_text(separator=' ', strip=True).split())
                if text:
                    data[current_title].append(text)

        elif el.name == 'li':
            if current_title:
                item = ' '.join(el.get_text(separator=' ', strip=True).split())
                if item:
                    data[current_title].append(item)

    # Q/A 영역 추가 크롤링
    qna_list = []
    for dd in bs.select("dl.accordion.qna dd"):
        raw = dd.get_text(" ", strip=True)
        raw = re.sub(r"\s+", " ", raw)

        m = re.search(r"Q\s*[:.]\s*(.*?)\s*A\s*[:.]\s*(.*)$", raw, flags=re.I | re.S)
        if m:
            q = m.group(1).strip(' "“”')
            a = m.group(2).strip(' "“”')
            if q and a:
                qna_list.append({"Q": q, "A": a})

    if qna_list:
        data["_QnA"] = qna_list  # 특별 키로 저장

    return dict(data)


# 기존 JSON 불러오기(없으면 빈 dict)
if os.path.exists(OUTFILE):
    with open(OUTFILE, 'r', encoding='utf-8') as f:
        all_data = json.load(f)
else:
    all_data = {}

# ids 범위 돌면서 저장
with requests.Session() as s:
    for i in range(344, 586):
        url = BASE.format(id=i)
        r = s.get(url, headers=headers, timeout=15)
        r.raise_for_status()
        page_data = parse_page(r.text)

        all_data[str(i)] = page_data
        print(f'OK {i}: {len(page_data)} titles + {len(page_data.get("_QnA", []))} qna')

        with open(OUTFILE, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        time.sleep(0.5)

print(f'Saved -> {OUTFILE}')