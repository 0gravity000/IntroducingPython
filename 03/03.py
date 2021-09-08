# 3.2.1 []またはlist()による作成
# リストは、0個以上の要素をカンマで区切り、[]で囲む
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']

# list()関数で空リストを作ることもできる
another_empty_list = list()
another_empty_list

# 3.2.2 list()によるほかのデータ型からリストへの変換
list('cat')

a_tuple = ('ready', 'fire', 'aim')
list(a_tuple)

birthday = '1/6/1952'
birthday.split('/')

splitme = 'a/b//c/d///e'
splitme.split('/')

splitme.split('//')

# 3.2.3 [offset]を使った要素の取り出し
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[0]
marxes[1]
marxes[2]
marxes[-1]
marxes[-2]
marxes[-3]

# 3.2.4 リストのリスト
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
all_birds
all_birds[0]
all_birds[1]
all_birds[1][0]

# 3.2.5 [offset]による要素の書き換え
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
marxes

# 3.2.6 オフセットの範囲を指定したスライスによるサブシーケンスの取り出し
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[0:2]
marxes[::2]
marxes[::-2]
marxes[::-1]

# 3.2.7 append()による末尾への要素の追加
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
marxes

# 3.2.8 extend()または+=を使ったリストの結合
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
marxes

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
marxes

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
marxes

# 3.2.9 insert()によるオフセットを指定した要素の追加
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.insert(3, 'Gummo')
marxes

marxes.insert(10, 'Karl')
marxes

# 3.2.10 delによる指定したオフセットの要素の削除
del marxes[-1]
marxes

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes[2]
del marxes[2]
marxes
marxes[2]

# 3.2.11 remove()による値に基づく要素の削除
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.remove('Gummo')
marxes

# 3.2.12 pop()でオフセットを指定して用をを取り出し、削除する方法
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.pop()
marxes
marxes.pop(1)
marxes

# 3.2.13 index()により要素の値から要素のオフセットを知る方法
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.index('Chico')

# 3.2.14 inを使った値の有無のテスト
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
'Groucho' in marxes
'Bob' in marxes

words = ['a', 'deer', 'a', 'female', 'deer']
'deer' in words

# 3.2.15 count()を使った値の個数の計算
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.count('Harpo')

marxes.count('Bob')

snl_skit = ['cheesebuger', 'cheesebuger', 'cheesebuger']
snl_skit.count('cheesebuger')

# 3.2.16 join()による文字列への変換
marxes = ['Groucho', 'Chico', 'Harpo']
', ' .join(marxes)  #join()はsplit()の逆

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
joined
separated = joined.split(separator)
separated
separated == friends

# 3.2.17 sort()による要素の並べ替え
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
sorted_marxes
marxes
marxes.sort()
marxes

numbers = [2, 1, 4.0, 3]
numbers.sort()
numbers

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
numbers

# 3.2.18 len()による長さの取得
marxes = ['Groucho', 'Chico', 'Harpo']
len(marxes)

# 3.2.19 =による代入とcopy()によるコピー
a = [1, 2, 3]
a
b = a
b
a[0] = 'surprise'
a
b   #ここ重要
b[0] = 'I hate surprises'
b
a

a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]

a[0] = 'integer lists are boring'
a
b
c
d

# 3.3 タプル
# 3.3.1 ()を使ったタプルの作成
empty_tuple = ()
empty_tuple

# 末尾にカンマを付けてタプルを作成
one_marx = 'Groucho',
one_marx

# 要素が複数の場合、カンマで区切る。最後の要素の後ろのカンマは省略できる
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_tuple

# 値全体を()で囲むとタプルと分かりやすい
marx_tuple = ('Groucho', 'Chico', 'Harpo')
marx_tuple

marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple    #タプルのアンパック
a
b
c

password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
password
icecream

# 変換関数のtuple()を使う
marx_list = ['Groucho', 'Chico', 'Harpo']
tuple(marx_list)

# 3.4 辞書
# 辞書 連想配列 ハッシュ ハッシュマップ dictとも呼ばれる
# 3.4.1 {}による作成
empty_dict = {}
empty_dict

# 3.4.2 dict()を使った変換
# { key:value }
# 2つの値のシーケンスを辞書に変換する
# 2要素のシーケンスを含むものなら何でも使える
lol = [['a', 'b'], ['c', 'b'], ['e', 'f']]
dict(lol)

lot = [('a', 'b'), ('c', 'b'), ('e', 'f')]
dict(lot)

tol = (['a', 'b'], ['c', 'b'], ['e', 'f'])
dict(tol)

los = ['ab', 'cd', 'ef']
dict(los)

tos = ('ab', 'cd', 'ef')
dict(tos)

# 3.4.3 [key]による要素の追加、変更
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Falin': 'Michael',
}
pythons

# 辞書のキーは一意でなくてはならない
pythons['Gilliam'] = 'Garry'
pythons

pythons['Gilliam'] = 'Terry'
pythons

some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Falin',
    'Terry': 'Jones',
}
some_pythons

# 3.4.4 update()による辞書の結合
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Falin': 'Michael',
}
pythons
others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
pythons

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
first

# 3.4.5 delによる指定したキーを持つ要素の削除
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Falin': 'Michael',
    'Marx': 'Groucho',
    'Howard': 'Moe',
}
del pythons['Marx']
pythons
del pythons['Howard']
pythons

# 3.4.6 clear()によるすべての要素の削除
pythons.clear()
pythons
pythons = {}
pythons

# 3.4.7 inを使ったキーの有無のテスト
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Jones': 'Terry',
    'Falin': 'Michael',
}
pythons
'Chapman' in pythons
'Falin' in pythons
'Gilliam' in pythons

# 3.4.8 [key]による要素の取得
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Jones': 'Terry',
    'Falin': 'Michael',
}
pythons['Cleese']
pythons['Marx']
'Marx' in pythons
# 辞書専用のget()関数 キーがあればその値が返される
pythons.get('Cleese')

# キーなければ指定したオプション値が返される
pythons.get('Marx', 'Not a Python')
# オプション値を指定しなかれなNoneになる。インタープリタには何も表示されない
pythons.get('Marx')

# 3.4.9 keys()によるすべてのキーの取得
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
signals.keys()
list(signals.keys())

# .4.10 values()によるすべての値の取得
list(signals.values())

# .4.11 items()によるすべてのキー/値ペアの取得
list(signals.items())

# =による代入とcopy()によるコピー
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
save_signals

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
signals
original_signals

# 3.5 集合
# 3.5.1 set()による作成
empty_set = set()
empty_set
# 1個以上のカンマ区切りの値を{}で囲む
even_numbers = {0, 2, 4, 6, 8}
even_numbers
odd_numbers = {1, 3, 5, 7, 9}
odd_numbers

# 3.5.2 set()によるほかのデータ型から集合への変換
# 重複する'e'と't'は1つになる
set('letters')

set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])

set(('Ummagumma', 'Echoes', 'Atom Heart Mother'))

# 辞書を渡すと、キーだけが使われる
set({'apple': 'red', 'orage': 'orange', 'cherry': 'red'})

# 3.5.3 inを使った値の有無のテスト
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

# 3.5.4 組み合わせと演算
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

# 3.6 データ構造の比較
marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
marx_list[2]
marx_tuple[2]
marx_dict['Harpo']

# 3.7 もっと大きいデータ構造
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

tuple_of_lists = marxes, pythons, stooges
tuple_of_lists

list_of_lists = [marxes, pythons, stooges]
list_of_lists

dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges':stooges}
dict_of_lists

# タプルは辞書のキーになれる（イミュータブルのため）
# リスト、辞書、集合は辞書のキーになれない
houses = {
    (44.79, -93.14, 285): 'My House',
    (38.89, -77.03, 13): 'The White House',
}
