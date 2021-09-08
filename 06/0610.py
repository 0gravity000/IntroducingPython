# 6.10 メソッドのタイプ
class A():
    count = 0
    def __init__(self):
        A.count += 1    # self.countだとインスタンスの属性になる
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):  # クラスメソッド
        print("A has", cls.count, "Little objects")

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()

# 静的メソッド
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has brought to you by Acme')

CoyoteWeapon.commercial()