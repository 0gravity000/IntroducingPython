# 4.6 内包表記
# 4.6.1 リスト内包表記
# [expression for item in iterable]
number_list = [number for number in range(1, 6)]
number_list

number_list = [number-1 for number in range(1, 6)]
number_list

# [expression for item in iterable if condition]
a_list = [number for number in range(1, 6) if number % 2 == 1]
a_list

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

# 内包表記を使ったループ
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
  print(cell)

# タプルのアンパックを使う
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for row, col in cells:
  print(row, col)

# 4.6.2 辞書内包表記
# {key_item: value_item for item in iterable}
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
letter_counts

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
letter_counts

# 4.6.3 集合内包表記
# [item for item in iterable]
a_set = {number for number in range(1, 6) if number % 3 == 1}
a_set

# 4.6.4 ジェネレータ内包表記