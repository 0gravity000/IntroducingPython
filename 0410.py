# 4.10 名前空間とスコープ
animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print('at th top level:', animal)

print_global()

# 関数内でグローバル変数の値を書き換えるとエラーになる
def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)

change_and_print_global()   # エラー

#
animal = 'fruitbat'
def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

change_local()
animal
id(animal)

#
animal = 'fruitbat'
def change_and_print_global2():
    global animal
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

animal
change_and_print_global2()
animal

#
animal = 'fruitbat'
def change_local2():
    animal = 'wombat'   # ローカル変数
    print('locals:', locals())

animal
change_local2()

print('globals:', globals())    #
animal