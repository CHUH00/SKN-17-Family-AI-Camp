import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",         # MySQL 서버 주소
    user = "ohgiraffers",       # 사용자 이름
    password = "ohgiraffers",   # 비밀번호
    database = "menudb"         # 사용할 데이터베이스 (스키마)
)

cursor = connection.cursor()

# sql = "INSERT INTO tbl_menu (menu_name, menu_price, category_code, orderable_status) VALUES ('허니콤보', 20000, 4, 'Y')"
sql = "INSERT INTO tbl_menu (menu_name, menu_price, category_code, orderable_status) VALUES (%s, %s, %s, %s)"

values = ('레드콤보', 23000, 4, 'Y')

cursor.execute(sql, values)

# Commit 처리
connection.commit()

print(f"{ cursor.rowcount }개의 행 삽입 완료@@")
    
cursor.close()
connection.close()