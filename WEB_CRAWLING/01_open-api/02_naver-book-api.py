# import 구문은 제일 위에 모아두는 거 기억하시죠?
import urllib.request
import json
import mysql.connector

# API KEY 설정
client_id = "FIZvVi35nzEiqC5WxF_F"
client_secret = "KKE4m5V5Bw"

# 검색어 설정
text = "빅데이터"
encText = urllib.parse.quote(text)

# url 및 헤더 설정
start_num = 1
display = 100

url = "https://openapi.naver.com/v1/search/book.json?query=" + encText + "&start=" + str(start_num) + "&display=" + str(display)
    
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)

body = response.read().decode('utf-8')

# api 요청 및 결과값 json 반환
# [힌트] json <-> 파이썬 dictionary 변환
#           import json
#           json.loads(json)
body_json = json.loads(body)

# DB 연결 객체 생성
connection = mysql.connector.connect(
    host = "localhost",
    user = "ohgiraffers",
    password = "ohgiraffers",
    database = "bookdb"
)

# SQL 수행을 위한 커서 생성
cursor = connection.cursor()

# API를 통해 받아온 정보를 가지고 INSERT 수행
for i in range(len(body_json['items'])):
    values = ()
    sql = "INSERT INTO naver_book (book_title, book_image, author, publisher, isbn, book_description, pub_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values += (body_json['items'][i]['title'], body_json['items'][i]['image'], body_json['items'][i]['author'], body_json['items'][i]['publisher'], 
               body_json['items'][i]['isbn'], body_json['items'][i]['description'], body_json['items'][i]['pubdate'])

    print(sql, values)
    cursor.execute(sql, values)
    
    # 데이터베이스 트랜잭션 처리 (commit -> 반영)
    connection.commit()

    print(f"{ cursor.rowcount }개의 행 삽입 완료.")

# 커서 및 연결 객체 종료 (반납)
cursor.close()
connection.close()