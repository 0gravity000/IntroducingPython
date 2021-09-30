# 6.14 モジュールでなくクラスとオブジェクトを使うべきなのはいつか

# 6.14.1 名前付きタプル
# 名前付きタプルがタプルのサブクラスで、位置[offset]だけでなく、名前.nameでも値にアクセスできる
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')  # 第1引数は名前、第2引数は空白区切りでフィールド名を指定
duck = Duck('wide orange', 'long')
duck    # Duck(bill='wide orange', tail='long')

duck.bill   # 'wide orange'

duck.tail   # 'long'

# 名前付きタプルは辞書からも作れる
parts = {'bill': 'wide organge', 'tail': 'long'}
duck2 = Duck(**parts)   # キーワード引数
# 以下のように書くのと同じ
# duck2 = Duck(bill = 'wide orange', tail = 'long')
duck2   # Duck(bill='wide organge', tail='long')

# 名前付きタプルはイミュータブルだが、1個以上のフィールドを交換した別の名前付きタプルを返すことができる
duck3 = duck2._replace(tail='magnificent', bill='crushing')
duck3   # Duck(bill='crushing', tail='magnificent')

# 辞書として定義
duck_dict = {'bill': 'wide orange', 'tail': 'long'}
duck_dict   # {'bill': 'wide orange', 'tail': 'long'}
# 辞書にはフィールドを追加できる
duck_dict['color'] = 'green'
duck_dict   # {'bill': 'wide orange', 'tail': 'long', 'color': 'green'}

# 名前付きタプルには追加できない
duck_dict.color = 'green'   # エラー
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'color'
'''