import sqlite3

connection = sqlite3.connect('./db/sample.db')
c = connection.cursor()

c.execute("CREATE TABLE IF NOT EXISTS code (id int, contents varchar(1024))")
c.execute("INSERT code (id int, contents varchar(1024))")
c.execute("SELECT * FROM code")

conn.commit()
conn.close()