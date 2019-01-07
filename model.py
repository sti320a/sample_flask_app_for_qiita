import sqlite3

connection = sqlite3.connect('./db/sample.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS code (id int, contents varchar(1024))")
cursor.execute("INSERT code (id int, contents varchar(1024))")
cursor.execute("SELECT * FROM code")

conn.commit()
conn.close()