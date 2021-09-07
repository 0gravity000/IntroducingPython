# 2.3.11 多彩な文字列操作
poem = '''All tjat doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid whice is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

# 0-12を取り出し
poem[:13]

len(poem)

poem.startswith('All')

poem.endswith('That\'s all, folks!')

word = 'the'
poem.find(word)
poem.rfind(word)
poem.count(word)
poem.isalnum()
