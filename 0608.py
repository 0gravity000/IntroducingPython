# 6.8 プロパティによる属性値の取得、設定
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self): #ゲッター
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name): #セッター
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

fowl = Duck('Howard')
fowl.name

fowl.get_name()

fowl.name = 'Daffy'

fowl.name

fowl.set_name('Daffy')

fowl.name

#プロパティはデコレータで定義することもできる
# ともにname()という名前を持つが、前につくデコレータが異なる2つのメソッドを定義
# @property
#   ゲッターメソッドの前に付けるデコレータ
# @name.setter
#   セッターメソッドの前につけるデコレータ
class Duck1():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self): #ゲッター
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name): #セッター
        print('inside the setter')
        self.hidden_name = input_name

fowl = Duck1('Howard')
fowl.name

fowl.name = 'Donald'

fowl.name

#
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
c.radius

c.diameter

c.radius = 7
c.diameter

c.diameter = 20