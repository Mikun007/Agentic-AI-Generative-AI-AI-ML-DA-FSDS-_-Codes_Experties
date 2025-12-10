import mysql.connector # pip install mysql-connector-python

conn = mysql.connector.connect(host="localhost", user="root", passwd="1234")

if conn.is_connected():
    print("Connection established")

print(conn)
print(conn.is_connected())