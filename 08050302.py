# 8.5.3.2 リスト
import redis
conn = redis.Redis()

conn.lpush('zoo', 'bear')

conn.lpush('zoo', 'alligator', 'duck')

conn.linsert('zoo', 'befor', 'bear', 'breaver')

conn.linsert('zoo', 'after', 'bear', 'cassowary')

conn.lset('zoo', 2, 'marmoset')

conn.rpush('zoo', 'yak')

conn.lindex('zoo', 3)

conn.lrange('zoo', 0, 2)

conn.ltrim('zoo', 1, 4)

conn.lrange('zoo', 0, -1)
