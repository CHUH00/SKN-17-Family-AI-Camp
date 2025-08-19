import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",         # MySQL 서버 주소
    user = "ohgiraffers",       # 사용자 이름
    password = "ohgiraffers",   # 비밀번호
    database = "menudb"         # 사용할 데이터베이스 (스키마)
)

if connection.is_connected():
    print('@@@MySQL 서버에 성공적으로 연결@@@')
    
connection.close()