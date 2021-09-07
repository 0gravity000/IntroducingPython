# 8.4.3 SQLite
import sqlite3
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAR)''')

#
curs.execute('INSERT INTO zoo (critter VALUES("duck", 5, 0.0)')

curs.execute('INSERT INTO zoo (critter VALUES("bear", 2, 1000.0)')

# プレースホルダを使ったより安全な挿入
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute('ins, ("weasel", 1, 2000.0)')

#
curs.execute('SELECT * FROM zoo')

rows = curs.fetchall()
print(rows)

#個体数順でソート
curs.execute('SELECT * FROM zoo ORDER BY count')

curs.fetchall()

#降順
curs.execute('SELECT * FROM zoo ORDER BY count DESC')

curs.fetchall()

#
curs.execute('''SELECT * FROM zoo WHERE
    damages = (SELECT MAX(damages) FROM zoo)''')

curs.fetchall()

curs.close()
conn.close()