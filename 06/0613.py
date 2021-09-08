# 6.13 コンポジション
# 継承はis-aの関係（子クラスは親クラスである）
# コンポジションはhas-aの関係（xクラスはyクラスを持っている）
# アヒルはくちばし(bill)、しっぽ(tail)をもっている

# くちばしクラス
class Bill():
    def __init__(self, description):
        self.description = description

# しっぽクラス
class Tail():
    def __init__(self, length):
        self.length = length

# アヒルクラス
class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')

# オブジェクト(インスタンス)を作る
tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail) #アヒルはくちばし(bill)、しっぽ(tail)をもっている
duck.about()
