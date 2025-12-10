import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password='1234')

my_cursor = conn.cursor()

my_cursor.execute("show databases")
for x in my_cursor:
    print(x)