# 7.1.3.1 match()による正確なマッチ

# マッチングの対象となる文字列のパターンとマッチングするソース文字列を定義する
# 'You'がパターン、'Young Frankenstein'がソース文字列
# match()は、ソースの先頭がパターンになっているかどうかをチェックする
import re
result = re.match('You', 'Young Frankenstein')

import re
source = 'Young Frankenstein'
m = re.match('You', source) # match()はsourceの先頭がパターンに一致するか見る
if m:   #match()はオブジェクトを返す。マッチした部分を確かめる
    print(m.group())

m = re.match('^You', source)     # パターンの先頭に^をつけても同じ意味

# match()は何も返さない。matchはパターンがソースの先頭になければ成功しない
m = re.match('Frank', source)
if m:
    print(m.group())

# search()はパターンがソースのどこにあってもよい
m = re.search('Frank', source)
if m:
    print(m.group())

# パターンの「.」は任意の1文字、「*」は任意の個数の直前のものという意味
m = re.match('.*Frank', source)
if m:   # matchはオブジェクトを返す
    print(m.group())

