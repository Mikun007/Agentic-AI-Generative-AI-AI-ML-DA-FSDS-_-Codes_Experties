import mysql.connector

conn = mysql.connector.connect(host = 'localhost', user="root", password='1234', database='pythondb')

my_cursor = conn.cursor()

sql = 'insert into student (name, branch, id) values(%s, %s, %s)'

val=[
    ("john", 'cse', '56'),
    ("mike", "IT", '78'),
    ('tyson', 'me', '80')
]

my_cursor.executemany(sql, val)
conn.commit()
print(my_cursor.rowcount, 'record inserted')