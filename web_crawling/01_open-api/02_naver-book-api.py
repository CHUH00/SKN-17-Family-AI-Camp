# import 구문은 제일 위에 모아두는 거 기억하시죠?
import urllib.parse
import urllib.request
import json
import mysql.connector

# API KEY 설정
client_id = 'vPn2yQZIJXeRMIXoJ7Ap'
client_secret = 'Dy1f37DWeD'

# 검색어 설정
searchText = urllib.parse.quote('데이터')

# url 및 헤더 설정
# url = 'https://openapi.naver.com/v1/search/book.json?query=' + searchText + '&display=100'
url = 'https://openapi.naver.com/v1/search/book.json?query=' + searchText + '&display=1'    # 전체 정보를 가져오기 위해 total 먼저 확인
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

# api 요청 및 결과값 json 반환
# [힌트] json <-> 파이썬 dictionary 변환
#           import json
#           json.loads(json객체) -> dictionary 반환
# api 요청 및 결과값 json 변환 (dictionary)
response = urllib.request.urlopen(request)
response_body = response.read()
response_body = json.loads(response_body)

# book_list = response_body['items']
total_count = response_body['total']    # 전체 정보를 가져오기 위해 total 먼저 확인
start_num = 1                           # start 파라미터 변경을 위한 변수 초기화
loop_count = total_count // 100 + 1     # 반복 횟수 설정을 위한 변수
book_list = []                          # 응답받은 정보를 담기 위한 변수 초기화

# 전체 정보를 가져오기 위한 반복
for i in range(loop_count):
    url = 'https://openapi.naver.com/v1/search/book.json?query=' + searchText + '&display=100&start=' + str(start_num)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request)
    response_body = response.read()
    response_body = json.loads(response_body)

    book_list += response_body['items']
    start_num += 100

    # API 정의상 start 파라미터의 최댓값이 1000이기 때문에 조건 설정
    if start_num > 1000:
        break

# DB 연결 객체 생성
connection = mysql.connector.connect(
    host="localhost",
    user="ohgiraffers",
    password="ohgiraffers",
    database="bookdb"
)

# sql 수행을 위한 커서 생성
cursor = connection.cursor()

# API를 통해 받아온 정보를 가지고 INSERT 수행
sql = "INSERT INTO naver_book (book_title, book_image, author, publisher, isbn, book_description, pub_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"

for book_info in book_list:
    values = (book_info['title'], book_info['image'], book_info['author'], 
              book_info['publisher'], str(book_info['isbn']), 
              book_info['description'], book_info['pubdate'])
    cursor.execute(sql, values)

# 데이터베이스 트랜잭션 처리 (commit -> 반영)
connection.commit()

# 커서 및 연결 객체 종료 (반납)
cursor.close()
connection.close()
