# 8.5.3 Redis
# Redisはデータ構造サーバー
# pip install redis
# Redisサーバーのインストールも必要
# https://weblabo.oscasierra.net/redis-windows-install/

# 8.5.3.3 ハッシュ
# Redisのハッシュは、Pythonの辞書とよく似ているが、文字列しか格納できない
# そのため深さは1レベルだけに限られ、深くネストされた構造は作れない

# Redisをインポート
import redis
# Redisサーバーに接続
# redis.Redis('localhost')、redis.Redis('localhost', '6379')でもOK
conn = redis.Redis()
# hmset()を使ってsongハッシュにdo、reフィールドを同時に設定する
conn.hmset('song', {'do': 'a deer', 're': 'about a deer'})
# hset()を使ってハッシュ内の1個のフィールドの値を設定する
conn.hset('song', 'mi', 'a note to follow re')
# hget()を使って1個のフィールドの値を取得する
conn.hget('song', 'mi')
# hmget()を使って複数のフィールドの値を取得する
conn.hmget('song', 're', 'do')
# hkeys()を使って、すべてのハッシュのすべてのフィールドのキーを取得する
conn.hkeys('song')
# hvals()を使って、すべてのハッシュのすべてのフィールドの値を取得する
conn.hvals('song')
# hlen()を使って、ハッシュのフィールド数を取得する
conn.hlen('song')
# hgetall()を使って、すべてのハッシュのすべてのフィールドのキーと値を取得する
conn.hgetall('song')
# hsetnx()を使ってキーがまだなければフィールドを設定する
conn.hsetnx('song', 'fa', 'a note that rhymes with la')
