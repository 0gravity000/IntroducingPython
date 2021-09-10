# 8.5.3 Redis
# Redisはデータ構造サーバー
# pip install redis
# Redisサーバーのインストールも必要
# https://weblabo.oscasierra.net/redis-windows-install/

# 8.5.3.7 キャッシュと有効期限
# Redisのすべてのキーには寿命、有効期限がある
# デフォルトでは永遠になっている

# Redisをインポート
import redis
# Redisサーバーに接続
# redis.Redis('localhost')、redis.Redis('localhost', '6379')でもOK
conn = redis.Redis()

import time
key = 'now you see it'
conn.set(key, 'but not for long')
# expire()でキーをいつまで残しておくか指定できる
conn.expire(key, 5)

conn.ttl(key)

conn.get(key)

time.sleep(6)
conn.get(key)

# expireat()で、指定したUnix時間にキーが無効になる
# キーの有効期限は、キャッシュをフレッシュしたり、
# ログインセッションを制限したりするために役立つ
