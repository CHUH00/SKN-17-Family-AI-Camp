from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
import mysql.connector

path ='/Users/woojin/Desktop/SK Networks Family AI Camp_17/1차_5팀_NOESIS/chromedriver'
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

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'ohgiraffers',
    password ='ohgiraffers', 
    database = 'cardb' 
) 

if connection.is_connected(): 
    print('MySQL 서버에 성공적으로 연결')

cursor = connection.cursor() 


sql = 'insert into FAQ (title, content) values (%s, %s)' 

title = ''
content = ''


for k,v in FAQs.items():
    title = k
    content = v
    values = (title,content)
    print(title, content)
    cursor.execute(sql,values)


# commit 처리
connection.commit()

print(f'{cursor.rowcount}개의 행 삽입 완료')

cursor.close()

connection.close()