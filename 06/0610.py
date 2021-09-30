# 6.10 メソッドのタイプ
# メソッドの第1引数がselfなら、インスタンスメソッド（いわゆる普通のメソッド）
# @classmethodデコレータと第1引数がclsなら、クラスメソッド
class A():
    count = 0
    def __init__(self):
        A.count += 1    # これは、クラス属性。self.countだとインスタンスの属性になってしまう
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):  # クラスメソッド
        print("A has", cls.count, "Little objects") # A.countでもOK

# オブジェクト(インスタンス)を作る
easy_a = A()
breezy_a = A()
wheezy_a = A()
# クラスメソッドを呼び出す
A.kids()    # A has 3 Little objects

# 静的メソッド
# クラスにもオブジェクト(インスタンス)にも影響を与えない
# 独立した存在としてふらふらしているよりも都合がいいので、
# クラス定義の中にいるだけのもの
# @staticmethodデコレータを付けると、静的メソッド
# 第1引数にselfやclsを取らない
class CoyoteWeapon():
    @staticmethod
    def commercial():   #静的メソッド
        print('This CoyoteWeapon has brought to you by Acme')

# オブジェクト(インスタンス)を作らず、実行できる
CoyoteWeapon.commercial()   # This CoyoteWeapon has brought to you by Acme

