# 6.14.1 名前付きタプル
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
duck

duck.bill

duck.tail

# 名前月タプルは辞書からも作れる
parts = {'bill': 'wide organge', 'tail': 'long'}
duck2 = Duck(**parts)   # キーワード引数
# 以下のように書くのと同じ
# duck2 = Duck(bill = 'wide orange', tail = 'long')
duck2

duck3 = duck2._replace(tail='magnificent', bill='crushing')
duck3

#
duck_dict = {'bill': 'wide orange', 'tail': 'long'}
duck_dict
# 辞書にはフィールドを追加できる
duck_dict['color'] = 'green'
duck_dict

# 名前付きタプルには追加できない
duck_dict.color = 'green'   # エラー