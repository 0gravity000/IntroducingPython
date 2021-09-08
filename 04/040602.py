# 4.6.2 辞書包括表現
# {key_item: value_item for item in iterable}
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
letter_counts

# 少しpythonらしいコード
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
letter_counts
