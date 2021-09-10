# 8.4.3 SQLite
# SQLiteはPythonの標準ライブラリとして実装され、
# 通常のファイルにデータベースを格納する
# データベースを格納したファイルはマシン、OSの違いを越えて扱うことができる

# sqlite3モジュールをインポート
import sqlite3
# enterprise.dbを作る
conn = sqlite3.connect('enterprise.db')
# カーソル
curs = conn.cursor()
# zooテーブルを作る
curs.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAR)''')
# データを追加
curs.execute('INSERT INTO zoo (critter VALUES("duck", 5, 0.0)')
# データを追加
curs.execute('INSERT INTO zoo (critter VALUES("bear", 2, 1000.0)')
# プレースホルダを使ったより安全な挿入 SQLインジェクションからシステムを守ってくれる
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute('ins, ("weasel", 1, 2000.0)')
# データを取り出す
curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)

# 個体数順でソート
curs.execute('SELECT * FROM zoo ORDER BY count')
curs.fetchall()

# 降順
curs.execute('SELECT * FROM zoo ORDER BY count DESC')
curs.fetchall()

# 最も損失の大きい動物を選択
curs.execute('''SELECT * FROM zoo WHERE
    damages = (SELECT MAX(damages) FROM zoo)''')
curs.fetchall()

# カーソルを閉じる
curs.close()
# 接続を閉じる
conn.close()