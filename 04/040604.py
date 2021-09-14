# 4.6.4 ジェネレータ内包表記
# タプルには内容表記がない
# リスト内包表記の[]を()に変えれば、
# タプル無い悲報表記ができたと思われるが、そうではなく
# ジェネレータない氷表記になり、ジェネレータオブジェクトを返す
number_thing = (number for number in range(1, 6))
type(number_thing)

# ジェネレータオブジェクトが直接forループで処理できる
for number in number_thing:
    print(number)

# ジェネレータ内包表記をlist()でラップすれば
# リスト内包表記のように動作させることができる
number_list = list(number_thing)
number_list

# ジェネレータは一度だけしか実行できない
# そのためジェネレータをもう一度使ったり、バックアップしたりすることはできない
# もう一度このジェネレータを使おうとすると、もう何も出てこない
try_again = list(number_thing)
try_again
