# 메뉴코드가 10번인 메뉴 삭제
# 메뉴코드는 변수에 담아서 사용

import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",         # MySQL 서버 주소
    user = "ohgiraffers",       # 사용자 이름
    password = "ohgiraffers",   # 비밀번호
    database = "menudb"         # 사용할 데이터베이스 (스키마)
)

cursor = connection.cursor()

sql = "DELETE FROM tbl_menu WHERE menu_code = (%s)"
code_num = ('11',)

cursor.execute(sql, code_num)

# Commit 처리
connection.commit()

print(f"{ cursor.rowcount }개의 행 삭제 완료@@")
    
cursor.close()
connection.close()