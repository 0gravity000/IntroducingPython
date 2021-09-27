# 4.7 関数
# 関数の定義 def宣言
# 関数の呼び出し

# 何もしない関数の定義
def do_nothing():
    pass

# 何もしない関数の呼び出し
do_nothing()

# 引数のない関数宣言
def make_a_sound():
    print('quack')

# 引数のない関数の呼び出し
make_a_sound()

# 引数なし、戻り値あり関数の宣言
def agree():
    return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected')

# 引数あり、戻り値あり関数の宣言
def echo(anything): # anything は仮引数
    return anything + ' ' + anything

# 引数あり、戻り値あり関数の呼び出し
echo('foo') # foo は実引数

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
def do_nothing():
    pass

print(do_nothing())	# None

# Noneはブール値としての評価はfalse。でもfalseと同じではない
# Noneは空の値と存在しない値を区別するために必要

# 4.7.1 位置引数
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

# 先頭から順に対応する位置の仮引数にコピーされる
menu('chardonnay', 'chiken', 'cake')
# {'wine': 'chardonnay', 'entree': 'chiken', 'dessert': 'cake'}


# 4.7.2 キーワード引数
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

# 対応する仮引数=実引数のように指定する
# 関数定義と引数の順番が異なっていてもよい
menu(entree='beef', dessert='bagle', wine='bordeaux')
# {'wine': 'bordeaux', 'entree': 'beef', 'dessert': 'bagle'}


def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

# 位置引数とキーワード引数の両方を使う場合、まず先に位置引数を指定する
menu('frontenac', entree='fish', dessert='flan')
# {'wine': 'frontenac', 'entree': 'fish', 'dessert': 'flan'}


# 4.7.3 デフォルト引数値の指定
# 仮引数にはデフォルト値を指定できる
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

# 関数の呼び出し時に対応する実引数を渡さなかった時にデフォルト引数値が使われる
menu('chardonnay', 'chiken')
# {'wine': 'chardonnay', 'entree': 'chiken', 'dessert': 'pudding'}

# 関数の呼び出し時に引数を指定すれば、デフォルト値の代わりに使われる
menu('dunkelfelder', 'duck', 'doughnut')
# {'wine': 'dunkelfelder', 'entree': 'duck', 'dessert': 'doughnut'}


#
def buggy(arg, result=[]):
	result.append(arg)
	print(result)

buggy('a')	# ['a']
buggy('b')	# ['a', 'b']

#
def works(arg):
	result = []
	result.append(arg)
	return result

works('a')	# ['a']
works('b')	# ['b']

#
def nonbuggy(arg, result=None):
	if result is None:
		result = []
	result.append(arg)
	print(result)

nonbuggy('a')	# ['a']
nonbuggy('b')	# ['b']


# 4.7.4 *による位置引数のタプル化
# 関数定義のなかで仮引数の一部として*を使うと、
# 可変個の位置引数をタプルにまとめて仮引数にセットする
def print_args(*args):
    print('Positional argument tuple:', args)

# 実引数なしで呼び出し
print_args()
# Positional argument tuple: ()

# 渡した位置引数はどのようなものでもargsタプルとして表示される
print_args(3, 2, 1, 'wait:', 'uh...')
# Positional argument tuple: (3, 2, 1, 'wait:', 'uh...')


# print()のように可変個の実引数をとる関数を書くときに役立つ
# 必須の位置引数がある場合、最後に*argsを書く
def print_more(requied1, requied2, *args):
    print('Need this one:', requied1)
    print('Need this one too:', requied2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
'''
Need this one: cap
Need this one too: gloves
All the rest: ('scarf', 'monocle', 'mustache wax')
'''

# 4.7.5 **によるキーワード引数の辞書化
# **を使えば、キーワード引数を1個の辞書にまとめることができる
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
# Keyword arguments: {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}

# *argsと**kwargsを併用する場合、*argsと**kwargsの順で並べる
# argsもkwargsも、この名前でなくても良いが、一般的にargsとkwargsの名前で使われる


# 4.7.6 docstring
# 関数本体の先頭に文字列を組み込めば、関数定義にドキュメントを付けることができる
def echo(anything):
    'echoは、与えられた入力引数を返す'
    return anything

# help()を呼び出し、関数名を渡すと、引数リストとともに
# きれいに整形されたdocstringが返される
help(echo)
'''
Help on function echo in module __main__:

echo(anything)
    echoは、与えられた入力引数を返す
'''

# 複数行にわたるdocstring
def print_if_true(thing, check):
    '''
    第2引数が真なら、第1引数を表示する
    処理内容：
        1. 第2引数が真かどうかチェックする
        2. 真なら第1引数を表示する
    '''
    if check:
        print(thing)

# きれいに整形されたdocstringが返される
help(print_if_true)

# 整形前のdocstring
# __doc__は、関数内の変数としてのdocstringの名前
help(print_if_true.__doc__)

# 4.7.7 一人前のオブジェクトとしての関数
# Ptyhonではすべてのものがオブジェクト
# 関数もオブジェクト。数値、文字列、タプル、リスト、辞書もオブジェクト
def answer():
    print(42)

answer()	# 42

def run_something(func):
    func()

# 'answer'を渡す。'answer()'ではない
# Pythonでは()は関数呼び出しを意味する
# ()がなければ、関数をオブジェクトとして扱う
run_something(answer)	# 42

type(run_something)	# <class 'function'>

#
def add_args(arg1, arg2):
	print(arg1 + arg2)

type(add_args)	# <class 'function'>

def run_something_with_args(func, arg1, arg2):
	func(arg1, arg2)

run_something_with_args(add_args, 5, 9)	#14

#
def sum_args(*args):
	# sum()は組み込み関数。イテラブルな数値引数に格納されている値の合計を返す
	return sum(args)

def run_with_potisional_args(func, *args):
	return func(*args)

run_with_potisional_args(sum_args, 1, 2, 3, 4)	#10


# 4.7.8 関数内関数
# 関数を他の関数の中で定義することができる
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

outer(4, 7)	#11

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

knights('Ni!')	# "We are the knights who say: 'Ni!'"


# 4.7.9 クロージャ
# クロージャとは多の関数によって動的に生成される関数で、
# その関数の外で作られた変数の値を覚えておいたり、変えたりできる
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2   # コピーを返すが呼び出さない

a = knights2('Duck')
b = knights2('Hasenpfeffer')
# aもb関数だがクロージャでもある
type(a)	# <class 'function'>
type(b)	# <class 'function'>
a	# <function knights2.<locals>.inner2 at 0x00000215A4C85550>
b	# <function knights2.<locals>.inner2 at 0x00000215A4C855E0>
# 呼び出す
# aもbもkhights2に自分たちが作られた時に使われていたsayingの内容を覚えている
a()	# "We are the knights who say: 'Duck'"
b()	# "We are the knights who say: 'Hasenpfeffer'"


# 4.7.10 無名関数：ラムダ関数
def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + '!'

edit_story(stairs, enliven)
'''
Thud!
Meow!
Thud!
Hiss!
'''

# :から末尾までは、関数定義
# コールバック関数を定義するときは、ラムダ関数が役立つ
edit_story(stairs, lambda word: word.capitalize() + '!')
'''
Thud!
Meow!
Thud!
Hiss!
'''
