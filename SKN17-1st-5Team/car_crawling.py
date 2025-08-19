from selenium import webdriver  # 브라우저 제어
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os, time

# 0) 다운로드 받을 폴더 준비
data_dir = os.path.abspath("data")
os.makedirs(data_dir, exist_ok=True)

# 1) ChromeOptions 에 다운로드 경로 지정
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": data_dir,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
})

# 2) 드라이버 실행
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 3) 페이지 열기
    driver.get(
        'https://stat.molit.go.kr/portal/cate/statView.do'
        '?hRsId=58&hFormId=5559&hSelectId=5559'
        '&sStyleNum=1&sStart=202505&sEnd=202505'
        '&hPoint=00&hAppr=1'
    )
    time.sleep(1)

    # 4) “통계정보” 탭 클릭
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/div/div[2]/div[1]/ul/li[2]/a'
    ).click()
    time.sleep(2)

    # 5) 페이지 스크롤(전체)로 컨테이너가 보이게끔
    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(1)

    # 6) 다운로드 리스트(inner-scroll) 컨테이너 선택
    container = driver.find_element(
        By.XPATH,
        '//*[@id="main"]/div/div[3]/div[1]/div/div[2]/div[2]/div'
    )

    # 7) 컨테이너 안에서 “자동차 등록자료 통계” 텍스트가 포함된 모든 링크 수집
    links = container.find_elements(
        By.XPATH,
        ".//a[contains(normalize-space(.), '자동차 등록자료 통계')]"
    )

    # 8) 클릭해서 전부 다운로드
    for link in links:
        # 보이게끔 스크롤
        driver.execute_script("arguments[0].scrollIntoView(true);", link)
        time.sleep(0.2)
        link.click()
        print("↓ 다운로드 시작:", link.text)
        time.sleep(1)  # 다운로드 트리거 대기

            # 2023년 04월 데이터 클릭 후 루프 종료
        if '2023년 04월' in link.text:
            print("✅ 2023년 04월 데이터 다운로드 완료, 종료합니다.")
            break

    # 9) 다운로드 마무리 대기
    time.sleep(5)
    print("✅ 다운로드 완료! data 폴더 내용:", os.listdir(data_dir))

finally:
    driver.quit()
