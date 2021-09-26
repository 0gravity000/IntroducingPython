# Trueとは何か

'''
Falseとみなされるもの
ブール値	False
null	None
整数のゼロ	0
floatのゼル	0.0
空文字	''
空リスト	[]
空タプル	()
空辞書	{}
空集合	set()

上記以外はすべてTrueとみなされる
'''

some_list = []
if some_list:
	print("There's something in here")
else:
	print("Hey, it's empty!")
