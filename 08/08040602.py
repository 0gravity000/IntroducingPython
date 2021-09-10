# 8.4.6 SQLAlchemy
# 8.4.6.2 SQL表現言語
# SQLAlchemyの2番目のレベル SQLとPythonの間の中間レベルの接続

# sqlalchemyをインポートしてエイリアスsaとする
import sqlalchemy as sa
# データベースを作り、メモリ内にその記憶領域を作る
#引数の文字列は'sqlite://:memory:'でもよい
conn = sa.create_engine('sqlite://')
# zooテーブルを表現言語で作る。SQLではない
meta = sa.MetaData()
zoo = sa.Table('zoo', meta,
  sa.Column('critter', sa.String, primary_key=True),
  sa.Column('count', sa.Integer),
  sa.Column('damages', sa.Float)
  )
meta.create_all(conn)
# 表現言語でデータを挿入
conn.execute(zoo.insert(('duck', 10, 0.0)))
conn.execute(zoo.insert(('bear', 2, 1000.0)))
conn.execute(zoo.insert(('weasel', 1, 2000.0)))
# 取り出す
results = conn.execute(zoo.select())
rows = results.fetchall()
print(rows)
