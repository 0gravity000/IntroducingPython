# 8.5.3 Redis
# Redisはデータ構造サーバー
# pip install redis
# Redisサーバーのインストールも必要
# https://weblabo.oscasierra.net/redis-windows-install/

# 8.5.3.4 集合
# Redisの集合はPythonの集合とよく似ている

# Redisをインポート
import redis
# Redisサーバーに接続
# redis.Redis('localhost')、redis.Redis('localhost', '6379')でもOK
conn = redis.Redis()
# sadd()で集合に1個または複数の値を追加する
conn.sadd('zoo', 'duck', 'goat', 'turkey')
# scard()で集合の値の数を取得する
conn.scard('zoo')
# smembers()で集合のすべての値を取得する
conn.smembers('zoo')
# srem()で集合から値を取り除く
conn.srem('zoo', 'turkey')
# もう1つ集合を作る
conn.sadd('better_zoo', 'tiger', 'wolf', 'duck')
# sinter()で積集合を取得する
conn.sinter('zoo', 'better_zoo')
# sinterstore()で積集合を取得して、fowl_zooに結果を格納する
conn.sinterstore('fowl_zoo', 'zoo', 'better_zoo')
conn.smembers('fowl_zoo')
# sunion()で和集合を取得する
conn.sunion('zoo', 'better_zoo')
# sunionstore()で和集合を取得して、fabulous_zooに格納する
conn.sunionstore('fabulous_zoo', 'zoo', 'better_zoo')
conn.smembers('fabulous_zoo')
# sdiff()で差集合を取得する
conn.sdiff('zoo', 'better_zoo')
# sdiffstore()で差集合を取得し、zoo_saleに格納する
conn.sdiffstore('zoo_sale', 'zoo', 'better_zoo')
conn.smembers('zoo_sale')
