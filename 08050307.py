# 8.5.3.7 キャッシュと有効期限 
import redis
conn = redis.Redis()

import time
key = 'now you see it'
conn.set(key, 'but not for long')

conn.expire(key, 5)

conn.ttl(key)

conn.get(key)

time.sleep(6)
conn.get(key)
