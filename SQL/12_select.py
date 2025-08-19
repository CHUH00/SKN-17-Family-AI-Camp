import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",         # MySQL 서버 주소
    user = "ohgiraffers",       # 사용자 이름
    password = "ohgiraffers",   # 비밀번호
    database = "menudb"         # 사용할 데이터베이스 (스키마)
)

cursor = connection.cursor()

sql = "SELECT * FROM tbl_menu"

cursor.execute(sql)

result_row = cursor.fetchall()

for row in result_row:
    print(row)
    
cursor.close()
connection.close()