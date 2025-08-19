from selenium import webdriver
import time 
from selenium.webdriver.common.by import By

path ='chromedriver.exe'
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service = service)

driver.get('https://www.kia.com/kr/pbv/kia-pbv/faq') 
time.sleep(3)

body = driver.find_element(By.TAG_NAME, "body")

idx = 0
FAQs = {}
while idx !=10:
    driver.execute_script("window.scrollTo(0, 750)")
    next_btn = driver.find_element(By.XPATH,f'//*[@id="accordion-item-{idx}-button"]')
    next_btn.click()
    title = driver.find_element(By.XPATH,f'//*[@id="accordion-item-{idx}-button"]/span[1]').text
    paragraphs = driver.find_elements(By.XPATH,f'//*[@id="accordion-item-{idx}-panel"]/div/div/div/p')
    texts = [p.text for p in paragraphs]
    content = "".join(texts)
    FAQs[title] = content
    time.sleep(3)
    idx +=1
time.sleep(1)
driver.quit()