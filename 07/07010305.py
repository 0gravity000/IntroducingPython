# 7.1.3.5 sub()によるマッチした部分の置換
import re
source = 'Young Frankenstein'
m = re.sub('n', '?', source)
m   # subは文字列を返す
