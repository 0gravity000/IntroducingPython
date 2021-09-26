# 4.5 forによる反復処理
# rabbitsはイテラブルオブジェクト（イテレーションに対応している）
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Petar']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

# よりPythonらしいコード
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Petar']
for rabbit in rabbits:
    print(rabbit)

# 文字列をforで処理すると、1文字づつ文字が生成される
word = 'cat'
for letter in word:
    print(letter)

# 辞書のキーを生成する
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation:     # または for card in accusation.keys():
    print(card)

# 辞書の値を生成する
for value in accusation.values():
    print(value)

# itemsはキー/値ペアをタプルで返す
for item in accusation.items():
    print(item)

# itemsが返すタプル（キー/値ペア）は、
# 第1引数cardにキー、第2引数contentsに値を代入できる
for card, contents in accusation.items():
	# cardにはキー、contentsには値が入る
    print('Card', card, 'has the contents', contents)


# 4.5.1 breakによる中止
# forループにbreak文を入れると、
# whileループの時と同様に、そこでループを中止する

# 4.5.2 continueによる次のイテレーションの開始
# forループにcontinue文を入れると、
# whileループの時と同様に、ループの次のイテレーションにジャンプする

# 4.5.3 elseによるbreakのチェック
# whileループの時と同様に、forは正常終了したかどうかをチェックするelseを持っている
# breakが呼び出されなければelse文が実行される
cheeses = []
for cheese in cheeses:
	print('This shop has some lovely', cheese)
	break
else:	# breakしていない時に実行される breakチェッカー
	print('This is not much of a cheese shop, is it?')


# 4.5.4 zip()を使った複数のシーケンスの反復処理
# zip()はもっともサイズの小さいシーケンス要素を処理しつくしたときに止まる
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']	# puddingは無視される
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy",dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
# タプルを作る
list(zip(english, french))
# 辞書を作る
dict(zip(english, french))

# 4.5.5 range()による数値シーケンスの生成
# range(start, end, step)	[ start:end:step ]によるスライスと似ている
for x in range(0, 3):
    print(x)

# リスト化する
list(range(0, 3))

# 2,1,0
for x in range(2, -1, -1):
    print(x)

# 2,1,0をリスト化する
list(range(2, -1, -1))

# 0,2,4,6,8,10
list(range(0, 11, 2))
