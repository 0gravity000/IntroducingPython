# 4.5 forによる反復処理
# rabbitsはいてラブルオブジェクト（イテレーションに対応している）
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Petar']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

# よりPythonらしいコード
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Petar']
for rabbit in rabbits:
    print(rabbit)

word = 'cat'
for letter in word:
    print(letter)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation:     # または for card in accusation.keys():
    print(card)

for value in accusation.values():
    print(value)

# itemsはキー/値ペアをタプルで返す
for item in accusation.items():
    print(item)

# itemsが返すタプル（キー/値ペア）は、
# 第1引数cardにキー、第2引数contentsに値を代入できる
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

# 4.5.4 zip()を使った複数のシーケンスの反復処理
# zip()はもっともサイズの小さいシーケンス要素を処理しつくしたときに止まる
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy",dessert)

#タプルを作る
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
list(zip(english, french))
dict(zip(english, french))

# 4.5.5 range()による数値シーケンスの生成
for x in range(0, 3):
    print(x)

list(range(0, 3))

for x in range(2, -1, -1):
    print(x)

list(range(2, -1, -1))

list(range(0, 11, 2))
