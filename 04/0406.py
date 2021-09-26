# 4.6 内包表記
# 内包表記はひとつ以上のイテレータからPythonデータ構造をコンパクトに作れる

# 4.6.1 リスト内包表記
# [expression for item in iterable]
number_list = [number for number in range(1, 6)]
number_list	# [1, 2, 3, 4, 5]

number_list = [number-1 for number in range(1, 6)]
number_list	# [0, 1, 2, 3, 4]

# 内包表記でない別の書き方 その1
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
number_list	# [1, 2, 3, 4, 5]

# 内包表記でない別の書き方 その2
number_list = []
for number in range(1, 6):
	number_list.append(number)
number_list	# [1, 2, 3, 4, 5]

# 内包表記でない別の書き方 その3
number_list =list(range(1, 6))
number_list	# [1, 2, 3, 4, 5]


# 末尾に条件を付け加えることもできる
# [expression for item in iterable if condition]
a_list = [number for number in range(1, 6) if number % 2 == 1]
a_list	# [1, 3, 5]

# 内包表記でない別の書き方
a_list = []
for number in range(1, 6):
  if number % 2 == 1:
    a_list.append(number)

a_list

# ネストされたループ
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
  for col in cols:
    print(row, col)
'''
1 1
1 2
2 1
2 2
3 1
3 2
'''

# 内包表記を使ったループ
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
  print(cell)
'''
(1, 1)
(1, 2)
(2, 1)
(2, 2)
(3, 1)
(3, 2)
'''

# タプルのアンパックを使う
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for row, col in cells:
  print(row, col)
'''
1 1
1 2
2 1
2 2
3 1
3 2
'''

# for row in rows for col in のそれぞれの後ろにifを付けることもできる


# 4.6.2 辞書内包表記
# {key_item: value_item for item in iterable}
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
letter_counts	# {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
letter_counts	# {'l': 1, 'r': 1, 'e': 2, 't': 2, 's': 1}

# 4.6.3 集合内包表記
# {item for item in iterable}	辞書内包表記と似ている
a_set = {number for number in range(1, 6) if number % 3 == 1}
a_set	# {1, 4}


# 4.6.4 ジェネレータ内包表記
# タプル()には内包表記がない。()で括ってもタプル()の内包表記ではない
# これはジェネレータ内包表記になる
number_thing = (number for number in range(1, 6))
number_thing	# <generator object <genexpr> at 0x00000215A419CC80>
type(number_thing)	# <class 'generator'>

# ジェネレータオブジェクトはforループで処理できる
for number in number_thing:
	print(number)
'''
1
2
3
4
5
'''

# ジェネレータ内包表記をlist()でラップすれば、リスト内包表記のように動作させることができる
number_list = list(number_thing)
number_list	# [1, 2, 3, 4, 5]

# ジェネレータは1度だけしか実行できない
# リスト、集合、文字列、辞書はメモリ内にあるが、
# ジェネレータは1度にひとつずつ、その場で値を作りイテレータに渡し、作った値を覚えていない
try_again = list(number_thing)
try_again	# []

