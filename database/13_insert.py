import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="ohgiraffers",
    password="ohgiraffers",
    database="menudb"
)

cursor = connection.cursor()

sql = "INSERT INTO tbl_menu (menu_name, menu_price, category_code, orderable_status) VALUES (%s, %s, %s, %s)"

values = ("레드콤보", 23000, 4, "Y")

cursor.execute(sql, values)

# commit 처리
connection.commit()

print(f"@@@{cursor.rowcount}개의 행 삽입 완료@@@")

cursor.close()
connection.close()
