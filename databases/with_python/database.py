# Database Creation
import mysql.connector

conn = mysql.connector.connect(host="localhost", user='root', password='1234')

if conn.is_connected():
    print("Connection established")

my_cursor = conn.cursor()
my_cursor.execute('create database pythondb')
print(my_cursor)