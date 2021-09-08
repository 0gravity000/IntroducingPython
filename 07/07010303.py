# 7.1.3.3 findall()によるすべてのマッチの検索
import re
source = 'Young Frankenstein'
m = re.findall('n', source)
m   # findallはリストを返す

print('Found', len(m), 'matches')

m = re.findall('n.', source)
m

m = re.findall('n.?', source)
m