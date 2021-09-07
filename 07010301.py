# 7.1.3.1 match()による正確なマッチ
import re
source = 'Young Frankenstein'
m = re.match('You', source) # matchはsourceの戦闘がパターンに一致するか見る
if m:
    print(m.group())

m = re.match('*You', source)     # パターンの先頭に*をつけても同じ意味

m = re.match('Frank', source)
if m:
    print(m.group())

m = re.search('Frank', source)
if m:
    print(m.group())

m = re.match('.*Frank', source)
if m:   # matchはオブジェクトを返す
    print(m.group())

