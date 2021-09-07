# 8.5.3.5 ソート済み集合(zset) 
import redis
conn = redis.Redis()

import time

now = time.time()
now

conn.zadd('logins', 'smeagol', now)

conn.zadd('logins', 'sauron', now+(5*60))

conn.zadd('logins', 'bilbo', now+(2*60*60))

conn.zadd('logins', 'treebeard', now+(24*60*60))

conn.zrank('logins', 'bilbo')

conn.zscore('logins', 'bilbo')

conn.zrange('logins', 0, -1)

conn.zrange('logins', 0, -1, withscores=True)