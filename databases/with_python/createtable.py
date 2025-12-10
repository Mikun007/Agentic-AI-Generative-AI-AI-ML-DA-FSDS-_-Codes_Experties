import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password='1234', database="pythondb")

my_cursor = conn.cursor()
my_cursor.execute("Create table student (name varchar(50),"
                  " branch varchar(10),"
                  " id int"
                  ")"
                  )

my_cursor.execute("show tables")

for x in my_cursor:
    print(x)