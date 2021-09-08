# 6.2 classによるクラス定義
class Person():
    pass

someone = Person()

#
class Person1():
    def __init__(self):
        pass

#
class Person2():
    def __init__(self, name):
        self.name = name

hunter = Person2('Elmer Fudd')
print('The mighty hunter: ', hunter.name)
