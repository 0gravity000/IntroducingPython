# 8.5.3.4 集合
import redis
conn = redis.Redis()

conn.sadd('zoo', 'duck', 'goat', 'turkey')

conn.scard('zoo')

conn.smembers('zoo')

conn.srem('zoo', 'turkey')

conn.sadd('better_zoo', 'tiger', 'wolf', 'duck')

conn.sinter('zoo', 'better_zoo')

conn.sinterstore('fowl_zoo', 'zoo', 'better_zoo')

conn.smembers('fowl_zoo')

conn.sunion('zoo', 'better_zoo')

conn.sunionstore('fabulous_zoo', 'zoo', 'better_zoo')

conn.smembers('fabulous_zoo')

conn.sdiff('zoo', 'better_zoo')

conn.sdiffstore('zoo_sale', 'zoo', 'better_zoo')

conn.smembers('zoo_sale')