# 4.7 関数
# 何もしない関数の定義
def do_nothing():
    pass

# 何もしない関数の呼び出し
do_nothing()

#
def make_a_sound():
    print('quack')

make_a_sound()

#
def agree():
    return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected')

#
def echo(anything): # anything は仮引数
    return anything + ' ' + anything

echo('foo') # foo は実引数

#
def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."
    
comment = commentary('blue')
print(comment)

# 関数がreturnを呼び出さなければ、戻り値はNoneとなる
print(do_nothing())

# Noneはブール値としての評価はfalse。でもfalseと同じではない
# Noneは空の値と存在しない値を区別するために必要

# 4.7.1 位置引数
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay', 'chiken', 'cake')

# 4.7.2 キーワード引数
menu(entree='beef', dessert='bagle', wine='bordeaux')

# 位置引数とキーサード引数の両方を使う場合、まず先に位置引数を指定する
menu('frontenac', entree='fish', dessert='flan')

# 4.7.3 デフォルト引数地の指定
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay', 'chiken')
menu('dunkelfelder', 'duck', 'doughnut')

# 4.7.4 *による位置引数のタプル化
def print_args(*args):
    print('Positional argument tuple:', args)

# 実引数なしで呼び出し
print_args()

# 渡した位置引数はどのようなものでもargsタプルとして表示される
print_args(3, 2, 1, 'wait:', 'uh...')

# print()のように可変個の実引数をとる関数を書くときに役立つ
# 必須の位置引数がある場合、最後に*argsを書く
def print_more(requied1, requied2, *args):
    print('Need this one:', requied1)
    print('Need this one too:', requied2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

# 4.7.5 **によるキーワード引数の辞書化
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


# 4.7.6 docstring
# 関数本体の先頭に文字列を組み込めば、関数定義にドキュメントを付けることができる
def echo(anything):
    'echoは、与えられた入力引数を返す'
    return anything

help(echo)

def print_if_true(thing, check):
    '''
    第2引数が真なら、第1引数を表示する
    処理内容：
        1. 第2引数が真かどうかチェックする
        2. 真なら第1引数を表示する
    '''
    if check:
        print(thing)

help(print_if_true)
help(print_if_true.__doc__)

# 4.7.7 一人前のオブジェクトとしての関数
# Ptyhonではすべてのものがオブジェクト
# 関数もオブジェクト。数値、文字列、タプル、リスト、辞書もオブジェクト
def answer():
    print(42)

answer()

def run_something(func):
    func()

# 'answer'を渡す。'answer()'ではない
# Pythonでは()は関数呼び出しを意味する
# ()がなければ、関数をオブジェクトとして扱う
run_something(answer)

type(run_something)

# 4.7.8 関数内関数
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

outer(4, 7)

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

knights('Ni!')

# 4.7.9 クロージャ
# クロージャとは多の関数によって動的に生成される関数で、
# その関数の外で作られた変数の値を覚えておいたり、変えたりできる
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2   # コピーを返すが呼び出さない

a = knights2('Duck')
b = knights2('Hasenpfeffer')
type(a)
type(b)
a
b
# 呼び出す
a()
b()

# 4.7.10 無名関数：ラムダ関数
def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + '!'

edit_story(stairs, enliven)
# :から末尾までは、関数定義
# コールバック関数を定義するときは、ラムダ関数が役立つ
edit_story(stairs, lambda word: word.capitalize() + '!')
