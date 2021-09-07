# 4.6.4 ジェネレータ内包表記
number_thing = (number for number in range(1, 6))
type(number_thing)

for number in number_thing:
    print(number)

number_list = list(number_thing)
number_list

# ジェネレータは一度だけしか実行できない
# そのためジェネレータをもう一度使ったり、バックアップしたりすることはできない
try_again = list(number_thing)
try_again
