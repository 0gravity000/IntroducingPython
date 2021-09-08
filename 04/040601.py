# 4.6.1 リスト内包表記
number_list = []
for number in range(1, 6):
    number_list.append(number)

number_list

number_list = list(range(1, 6))
number_list

# リスト内包表記を使った Pythonらしいコード
# ［ expression for item in iterable ］
number_list = [number for number in range(1, 6)]
number_list

number_list = [number -1 for number in range(1, 6)]
number_list

# リスト内包表記には条件式も追加できる
# ［ expression for item in iterable if condition］
a_list = [number for number in range(1, 6) if number % 2 == 1]
a_list

# 上記は以下と一緒
a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)

a_list

# 内包表記ではfor節を複数使うことができる
# 内包表記を使って結果を(row, col)形式のタプルにしてcells変数に代入
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

# 上記は以下と一緒
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

# なおタプルのアンパックを使って、cellsリストを反復処理しながら
# タプルからrow,colの値を引き抜くこともできる
for row, col in cells:
    print(row, col)
