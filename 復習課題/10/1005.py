# 10-1
from datetime import date
now = date.today()
now_str = now.isoformat()
with open('today.txt', 'wt') as output:
  print(now_str, file=output) #末尾に改行が追加される

# 以下でもOK
with open('today.txt', 'wt') as output:
  output.write(now_str)

# 10-2
with open('today.txt', 'rt') as input:
  today_string = input.read()

today_string

# 10-3
import time
fmt = "%Y-%m-%d\n"
time.strptime(today_string, fmt)

# 10-4
import os
os.listdir('.')

# 10-5
import os
os.listdir('..')

# 10-6
# multi_times.py
# python multi_times.py

# 10-7
from datetime import date
my_day = date(1973, 1, 20)
my_day

# 10-8
my_day.weekday()
my_day.isoweekday()

# 10-9
from datetime import timedelta
partry_day = my_day + timedelta(days=10000)
partry_day
