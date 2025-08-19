from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from urllib.request import urlretrieve
from datetime import datetime

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
for idx in range(9):
    movie_items = driver.find_elements(By.CSS_SELECTOR, "div.data_area")  # 영화 박스

    for movie_item in movie_items:
        # [심화 2] 이미지도 가지고 오기
        title = movie_item.find_element(By.CSS_SELECTOR, "div.area_text_box > a").text
        img_box = movie_item.find_element(By.CSS_SELECTOR, "a.img_box")
        link = img_box.get_attribute('href')
        img_src = img_box.find_element(By.TAG_NAME, "img").get_attribute("src")

        # 4. 영화 제목과 url 출력
        print(f"- {title}")
        print(f"  링크: {link}")
        print(f"  이미지: {img_src}")

        filename = f'movie_images/{datetime.now().strftime('%y%m%d_%H%M%S')}_{title}.jpg'
        urlretrieve(img_src, filename)

    # [심화 1] 다음 페이지도 가지고 오기
    if idx != 8:
        next_btn = driver.find_element(By.XPATH, '//*[@id="main_pack"]/div[3]/div[2]/div/div/div/div[1]/div[4]/div/a[2]')
        next_btn.click()
        time.sleep(1)

# 5. 드라이버 종료
driver.quit()
