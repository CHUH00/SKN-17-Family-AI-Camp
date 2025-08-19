# 동적 페이지 웹 크롤링 -> selenium
# 동적 페이지 = 요청한 URL에서 응답받은 HTML 안의 JS를 실행해 HTML을 새로 만든 경우 (Client Side Rendering)

# Selenium
# - 인증을 요구하는 특정 웹 페이지의 데이터 스크랩
# - 무한 댓글 스크랩
# - 브라우저용 매크로
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. chrome 브라우저 실행
path = 'chromedriver.exe'
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)

# 2. 특정 url 접근
# driver.get('https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%ED%81%AC%EB%A1%A4%EB%A7%81')
driver.get('https://naver.com')
time.sleep(1)

# - 검색어 입력 및 검색
search_box = driver.find_element(By.ID, 'query')
search_box.send_keys('크롤링')
search_box.send_keys(Keys.RETURN)
time.sleep(1)

# - 뉴스 탭 이동 (탭 다음으로 이동 -> 탭 선택)
next_btn = driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[2]/div[2]/a/span')
next_btn.click()
time.sleep(1)

news_btn = driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[9]/a')
news_btn.click()
time.sleep(1)

# - 스크롤 처리
for _ in range(5):
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.END)
    time.sleep(1)

# 3. 데이터 가져오기
news_contents_elems = driver.find_elements(By.CSS_SELECTOR, 'span.sds-comps-text-type-headline1')

for news_contents_elem in news_contents_elems:
    parent = news_contents_elem.find_element(By.XPATH, "..")

    title = news_contents_elem.text
    href = parent.get_attribute('href')
    print(title, "|", href)

# 4. 브라우저 종료 (드라이버 종료)
driver.quit()
