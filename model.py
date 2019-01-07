import sqlite3 # 標準ライブラリであるsqlite3をインポートする

connection = sqlite3.connect('./db/sample.db') # データベースファイルにアクセスする
cursor = connection.cursor() #　Cursorオブジェクトをつくる（いまは理解しなくても大丈夫）

# codeという名前のテーブルを作成する
cursor.execute("CREATE TABLE IF NOT EXISTS code (id int, contents varchar(1024))")

# codeテーブルにコードを保存する
cursor.execute("INSERT INTO code(id, contents) VALUES(?,?)", [1, "print('Hello, world')"])
conn.commit() # 保存をコミット

# codeテーブルの全データを取得する
result = cursor.execute("SELECT * FROM code")

for row in result:
    print(row)

conn.close()　# 接続を切る（理解しなくてもよいが、必ず書く）
