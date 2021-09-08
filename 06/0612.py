# 6.12 特殊メソッド
# マジックメソッドとも呼ばれる
# 先頭と末尾がダブルアンダースコアになっている

class Word():
  def __init__(self, text):
    self.text = text
  def equals(self, word2):
    return self.text.lower() == word2.text.lower()

# オブジェクト(インスタンス)を作る
first = Word('ha')
second = Word('HA')
third = Word('eh')
# 普通にメソッドを呼び出す
first.equals(second)
first.equals(third)

# equals()メソッドを特殊メソッド__eq__()に変更
class Word():
  def __init__(self, text):
    self.text = text
  def __eq__(self, word2):
    return self.text.lower() == word2.text.lower()

# オブジェクト(インスタンス)を作る
first = Word('ha')
second = Word('HA')
third = Word('eh')
# 特殊メソッド__eq__()の使い方
first == second
first == third

#参考
# https://docs.python.org/ja/3/reference/datamodel.html?highlight=__eq#object.__eq__


'''
他にも以下のような特殊メソッドがある
__eq__
__ne__
__lt__
__gt__
__le__
__ge__

__add__
__sub__
__mul__
__floordiv__
__truediv__
__mode__
__pow__
__str__
__repr__
__len__

'''

