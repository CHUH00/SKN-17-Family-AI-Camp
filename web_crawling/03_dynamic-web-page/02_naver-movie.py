from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Chrome 브라우저 실행
path = 'chromedriver.exe'
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)

# 2. naver에 '현재상영영화' 검색
driver.get('https://naver.com')
time.sleep(1)

# - 검색어 입력 및 검색
search_box = driver.find_element(By.ID, 'query')
search_box.send_keys('현재상영영화')
search_box.send_keys(Keys.RETURN)
time.sleep(1)

# 3. 영화 영역 탐색
movie_items = driver.find_elements(By.CSS_SELECTOR, "div.data_area")  # 영화 박스

for movie_item in movie_items:
    title = movie_item.find_element(By.CSS_SELECTOR, "div.area_text_box > a").text
    link = movie_item.find_element(By.CSS_SELECTOR, "a.img_box").get_attribute('href')
    
    # 4. 영화 제목과 url 출력
    print(f"- {title}")
    print(f"  링크: {link}")

# 5. 드라이버 종료
driver.quit()