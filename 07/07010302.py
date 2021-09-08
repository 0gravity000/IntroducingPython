# 7.1.3.2 search()による最初のマッチ
import re
source = 'Young Frankenstein'
m = re.search('Frank', source)
if m:
    print(m.group())
