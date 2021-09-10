# 8.5.3 Redis
# Redisはデータ構造サーバー
# pip install redis
# Redisサーバーのインストールも必要
# https://weblabo.oscasierra.net/redis-windows-install/

# 8.5.3.5 ソート済み集合(zset) 
# zsetは一意な値の集合だか、それぞれの値がスコアと呼ばれる浮動小数点も持っている
# 要素には値とスコアのどちらからでもアクセスできる

# Redisをインポート
import redis
# Redisサーバーに接続
# redis.Redis('localhost')、redis.Redis('localhost', '6379')でもOK
conn = redis.Redis()

import time
now = time.time()
now

# zadd()で追加する
conn.zadd('logins', 'smeagol', now)
conn.zadd('logins', 'sauron', now+(5*60))
conn.zadd('logins', 'bilbo', now+(2*60*60))
conn.zadd('logins', 'treebeard', now+(24*60*60))

# zrank()
conn.zrank('logins', 'bilbo')
# zscore()
conn.zscore('logins', 'bilbo')
# zrange()で全員をログイン順で見る
conn.zrange('logins', 0, -1)
conn.zrange('logins', 0, -1, withscores=True)
