# 8.5.3.6 ビット 
import redis
conn = redis.Redis()

days = ['2013-02-25', '2013-02-26', '2013-02-27']
big_spender = 1089
tire_kicker = 40459
late_joiner = 550212

conn.setbit(days[0], big_spender, 1)

conn.setbit(days[0], tire_kicker, 1)

conn.setbit(days[1], big_spender, 1)

conn.setbit(days[2], big_spender, 1)

conn.setbit(days[2], late_joiner, 1)

for day in days:
    conn.bitcount(day)


conn.getbit(days[1], tire_kicker)

conn.bitop('and', 'everyday', *days)

conn.bitcount('everyday')

conn.getbit('everyday', big_spender)

conn.bitop('or', 'alldays', *days)

conn.bitcount('alldays')
