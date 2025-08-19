import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from datetime import datetime

# 스크랩한 뉴스 정보를 담을 NewsEntry Class
class NewsEntry:
    def __init__(self, title, href, img_path):
        self.title = title
        self.href = href
        self.img_path = img_path

    def __repr__(self):
        return f'NewsEntry<title={ self.title }, href={ self.href }>'

# 1. requests -> url 요청
keyword = input('뉴스 검색 키워드 입력: ')
url = f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}"

response = requests.get(url)

# 2. html 응답
html = response.text

# 3. BeautifulSoup 객체 생성 (html 파싱)
bs = BeautifulSoup(html, 'html.parser')

# 4. 뉴스 박스 아이템
news_contents = bs.select('.fds-news-item-list-tab > div')

# NewsEntry 객체를 담을 배열 초기화
news_list = []

for idx, news_content in enumerate(news_contents):
    title_tag = news_content.select_one('span.sds-comps-text-type-headline1')
    href_tag = title_tag.find_parent('a')
    img_tag = news_content.find_all('img')[1]
    
    title = title_tag.text
    href = href_tag['href']
    img_path = ''

    # 이미지 경로 추출 + 이미지 저장
    if img_tag.has_attr('src'):
        img_path = img_tag['src']

        img_dir = 'images'
        file_name = datetime.now().strftime('%y%m%d_%H%M%S_') + str(idx + 1) + '.jpg'
        urlretrieve(img_path, f'{img_dir}/{file_name}')

    news_entry = NewsEntry(title, href, img_path)
    news_list.append(news_entry)

# 결과 출력
for news in news_list:
    print(news)
