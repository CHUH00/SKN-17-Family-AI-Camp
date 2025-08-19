# 메뉴코드가 7번인 메뉴의 메뉴명과 메뉴가격 수정
# 메뉴코드, 메뉴명, 메뉴가격은 변수에 담아서 사용

import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",         # MySQL 서버 주소
    user = "ohgiraffers",       # 사용자 이름
    password = "ohgiraffers",   # 비밀번호
    database = "menudb"         # 사용할 데이터베이스 (스키마)
)

cursor = connection.cursor()

sql = "UPDATE tbl_menu SET menu_name = (%s), menu_price = (%s) WHERE menu_code = (%s)"
values = ('카레라이스', '5000', '7')

cursor.execute(sql, values)

# Commit 처리
connection.commit()

print(f"{ cursor.rowcount }개의 행 수정 완료@@")
    
cursor.close()
connection.close()