import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="ohgiraffers",
    password="ohgiraffers",
    database="menudb"
)

cursor = connection.cursor()

menu_code = 7
menu_name = "변경된 메뉴명"
menu_price = 7777

sql = "UPDATE tbl_menu SET menu_name = %s, menu_price = %s WHERE menu_code = %s"

cursor.execute(sql, (menu_name, menu_price, menu_code))

# commit 처리
connection.commit()

print(f"@@@{cursor.rowcount}개의 행 수정 완료@@@")

cursor.close()
connection.close()
