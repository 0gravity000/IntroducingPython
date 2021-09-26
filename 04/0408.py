# 4.8 ジェネレータ
# range()はジェネレータのひとつである
# python2では、range()はリストを返す(メモリに収まる以上の整数を生成できない)
# python3では、ジェネレータを返す
sum(range(1, 101))

# ジェネレータ関数
# 値をreturnで返さず、yieldで返す
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

# my_rangeは関数
my_range	# <function my_range at 0x00000215A41C0EE0>

# my_rangeはジェネレータオブジェクトを返す
ranger = my_range(1, 5)
ranger	#<generator object my_range at 0x00000215A419C9E0>

# ジェネレータオブジェクトはforで処理できる
for x in ranger:
    print(x)
'''
1
2
3
4
'''

# もう1度実行すると、何も返さない
for x in ranger:
    print(x)

# Pythonのイテレータとジェネレータ
# https://qiita.com/tomotaka_ito/items/35f3eb108f587022fa09
