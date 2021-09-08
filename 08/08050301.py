# 8.5.3.1 文字列
import redis
conn = redis.Redis()

conn.keys('*')

conn.set('secret', 'ni!')

conn.set('carats', 24)

conn.set('fever', '101.5')

conn.get('secret')

conn.get('carats')

conn.get('fever')

# 設定失敗
conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!')
# すでに secret は存在するため
conn.get('secret')

conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing!')

conn.get('secret')

conn.getrange('secret', -6, -1)

conn.setrange('secret', 0, 'ICKY')

conn.get('secret')

conn.mset({'pie': 'cherry', 'cordial': 'sherry'})

conn.mget(['fever', 'carats'])

conn.delete('fever')

conn.incr('carats')

conn.incr('carats', 10)

conn.decr('carats')

conn.decr('carats', 15)

conn.set('fever', '101.5')

conn.incrbyfloat('fever')

conn.incrbyfloat('fever', 0.5)

conn.incrbyfloat('fever', -2.0)
