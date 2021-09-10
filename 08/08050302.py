# 8.5.3 Redis
# Redisはデータ構造サーバー
# pip install redis
# Redisサーバーのインストールも必要
# https://weblabo.oscasierra.net/redis-windows-install/

# 8.5.3.2 リスト
# Redisリストは、文字列しか格納できない
# リストは、最初の挿入を行ったときに作成される

# Redisをインポート
import redis
# Redisサーバーに接続
# redis.Redis('localhost')、redis.Redis('localhost', '6379')でもOK
conn = redis.Redis()

# lpush()は先頭へ挿入
conn.lpush('zoo', 'bear')
# lpush()で先頭へ複数要をを挿入
conn.lpush('zoo', 'alligator', 'duck')
# linsert()は値の前か後ろに挿入
conn.linsert('zoo', 'before', 'bear', 'breaver')
conn.linsert('zoo', 'after', 'bear', 'cassowary')
# lset()は、指定した位置に挿入する（リストはすでに存在していなかればならない）
conn.lset('zoo', 2, 'marmoset')
# rpush()は末尾へ村有
conn.rpush('zoo', 'yak')
# lindex()は指定したオフセットの値を得る
conn.lindex('zoo', 3)
# lrange()は指定したオフセット範囲の値を得る
conn.lrange('zoo', 0, 2)
# ltrim()はリストを刈り込む。指定したオフセットの範囲の要素だけが残る
conn.ltrim('zoo', 1, 4)
conn.lrange('zoo', 0, -1)
