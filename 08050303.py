# 8.5.3.3 ハッシュ
import redis
conn = redis.Redis()

conn.hmset('song', {'do': 'a deer', 're': 'about a deer'})

conn.hset('song', 'mi', 'a note to follow re')

conn.hget('song', 'mi')

conn.hmget('song', 're', 'do')

conn.hkeys('song')

conn.hvals('song')

conn.hlen('song')

conn.hgetall('song')

conn.hsetnx('song', 'fa', 'a note that rhymes with la')