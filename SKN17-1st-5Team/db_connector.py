# db_connector.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = 'localhost'
        , user = 'ohgiraffers'
        , password = 'ohgiraffers'
        , database = 'cardb'
    )