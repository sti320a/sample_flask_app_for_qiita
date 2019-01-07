import sqlite3

connection = sqlite3.connect('./db/sample.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS code (id int, contents varchar(1024))")

cursor.execute("INSERT INTO code(id, contents) VALUES(?,?)", [1, "print('Hello, world')"])
connection.commit()

result = cursor.execute("SELECT * FROM code")

for row in result:
    print(row)

connection.close()
