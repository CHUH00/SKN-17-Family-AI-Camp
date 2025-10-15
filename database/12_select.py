import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="ohgiraffers",
    password="ohgiraffers",
    database="menudb"
)

cursor = connection.cursor()

sql = "SELECT * FROM tbl_menu"

cursor.execute(sql)

result_rows = cursor.fetchall()

for row in result_rows:
    print(row)

cursor.close()
connection.close()
