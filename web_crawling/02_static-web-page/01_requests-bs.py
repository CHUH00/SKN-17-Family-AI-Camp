# 정적 페이지 웹 스크래핑 -> requests, beautifulsoup
# 정적 페이지 = 요청한 url에서 응답받은 html을 그대로 사용한 경우 (Server Side Rendering)

# https://tedboy.github.io/bs4_doc/generated/generated/bs4.BeautifulSoup.html
import requests
from bs4 import BeautifulSoup

# web request 요청 함수
def web_request(url):
    response = requests.get(url)
    print(response)                # <Response [200]>
    print(response.status_code)    # 응답코드
    print(response.text)           # html
    return response

# url = "https://naver.com"
# response = web_request(url)

with open('../html_sample.html', 'r', encoding='utf-8') as f:
    html = f.read()



# BeautifulSoup 객체 활용
bs = BeautifulSoup(html, 'html.parser') # html을 parsing해서 데이터 추출
# print(bs)
# print(type(bs))

def test_find():
    # find(): html 태그 및 속성을 dict로 조회 (1개만 조회)
    tag = bs.find('li')
    print(tag)
    print(type(tag))

    # find_all(): html 태그 및 속성을 dict로 조회 (전부 다 조회)
    tags = bs.find_all('section', {'id': 'section1'})
    print(tags)
    print(type(tags))

def test_selector():
    # CSS 선택자로 요소 추출
    tag = bs.select_one('section#section2')
    print(tag)
    print(type(tag))

    tags = bs.select('.section-content')
    print(tags)
    print(type(tags))

# [힌트] ResultSet -> Tag -> text 속성(= 내용)

def get_content1():
    # id가 section2인 section 태그의 후손 li 태그'들'의 내용 출력
    tags = bs.select('section#section2 li')

    for tag in tags:
        print(tag.text)    

def get_content2():
    # id가 section1인 section 태그의 자식 h2태그의 '내용', p 태그의 '내용' 출력
    h2_tag = bs.select_one('section#section1 > h2')
    print(h2_tag.text)

    p_tag = bs.select('section#section1 > p')
    for tag in p_tag:
        print(tag.text)

def get_content3():
    # id가 section1인 section 태그의 자식태그 조회 -> 내용 출력
    # [힌트] section#section1 -> select() or select_one()
    # [힌트] findChildren()
    section1_tag = bs.select_one('section#section1')

    children = section1_tag.findChildren()
    print(children)

    h2_tag = section1_tag.select_one('h2')
    p_tags = section1_tag.select('p')
    print(h2_tag.text)
    print([p_tag.text for p_tag in p_tags])



# 함수 실행
# test_find()
# test_selector()
# get_content1()
# get_content2()
get_content3()
