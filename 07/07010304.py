# 7.1.3.4 split()によるマッチを利用した分割
import re
source = 'Young Frankenstein'
m = re.split('n', source)
m   # splitはリストを返す
