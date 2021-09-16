import mysql.connector
from mysql.connector import Error

def mysql_connect(hostname,username,password,db):
    try:
        connection = mysql.connector.connect(
        host = hostname,
        user = username,
        passwd = password,
        database = db
        )
        print("Successfully connected")
    except Error as e:
        print(e)
    return connection

def cursor_connect(connection,):
    cursor = connection.cursor()

def close_connection(cursor,connection):
    try:
        cursor.close()
        connection.close()
        print("MYSQL connection closed")
    except Error as e:
        print(e)
