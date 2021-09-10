# 8.4.6 SQLAlchemy
# 個々のデータベースは、方言がある
# SQLAlchemyは、これらの方言を埋めるもの
# SQLAlchemyのインストール
# pip install sqlalchemy

# 8.4.6.1 エンジンレイヤ
# SQLAlchemyの一番低レベル

# sqlalchemyをインポートしてエイリアスsaとする
import sqlalchemy as sa
# データベースを作り、メモリ内にその記憶領域を作る
#引数の文字列は'sqlite://:memory:'でもよい
conn = sa.create_engine('sqlite://')
# 3つの列を持つzooテーブルをSQLで作る
conn.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAR)''')
# SQLで3個のデータを挿入する
ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000.0)
conn.execute(ins, 'weasel', 1, 2000.0)
# 取り出す
rows = conn.execute('SELECT * FROM zoo')
# <sqlalchemy.engine.cursor.LegacyCursorResult object at 0x0000016BDA15DD90>
# ResultsProxyではない？
print(rows)
# ループで表示
for row in rows:
  print(row)