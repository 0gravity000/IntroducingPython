# 8.4.6 SQLAlchemy
# 8.4.6.3 ORM（オブジェクト関係マッピング）
# SQLAlchemyのトップレベルレベル

# sqlalchemyをインポートしてエイリアスsaとする
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
# データベースを作り、メモリ内にその記憶領域を作る
#引数の文字列は'sqlite://:memory:'でもよい
conn = sa.create_engine('sqlite://')
# ORMで作る。
# zooクラスを定義し、属性とテーブルの列を対応付ける
Base = declarative_base()
class Zoo(Base):
  __tablename__ = 'zoo'
  critter = sa.Column('critter', sa.String, primary_key=True)
  count = sa.Column('count', sa.Integer)
  damages = sa.Column('damages', sa.Float)
  def __init__(self, critter, count, damages):
    self.critter = critter
    self.count = count
    self.damages = damages
  def __repr__(self):
      return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)

Base.metadata.create_all(conn)

# データを挿入
first = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)
first
second
third

# データベースとやりとりするためのセッションをを作る
# うまく動いていない
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()
# 上記で作った3つのオブジェクトをデータベースに書き込む
session.add(first)
session.add_all([second, third])
session.commit()

# カレントディレクトリにzoo.dbファイルができているはず
# sqlite3コマンド
# sqlite3 zoo.db
# .tables
# select * from zoo;
