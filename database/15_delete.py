import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="ohgiraffers",
    password="ohgiraffers",
    database="menudb"
)

cursor = connection.cursor()

menu_code = 10

sql = "DELETE FROM tbl_menu WHERE menu_code = %s"

cursor.execute(sql, (menu_code,))

# commit 처리
connection.commit()

print(f"@@@{cursor.rowcount}개의 행 삭제 완료@@@")

cursor.close()
connection.close()
