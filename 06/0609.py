# 6.9 非公開属性のための名前のマングリング
class Duck1():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self): #ゲッター
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name): #セッター
        print('inside the setter')
        self.__name = input_name

fowl = Duck1('Howard')
fowl.name

fowl.name = 'Donald'

fowl.name

fowl.__name     # エラー __name属性にはアクセスできない

fowl._Duck1__name