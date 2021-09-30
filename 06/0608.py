# 6.8 プロパティによる属性値の取得、設定
# オブジェクト指向言語の中には、外部から直接アクセスできないプロパティをサポートしているものがある
# そのような非公開の属性の値を読み書きするため、ゲッターメソッド、セッターメソッドがある
# Pythonは、すべての属性とメソッドが公開のため
# ゲッター、セッターを書く必要はないが、書くことはできる 
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name   #非公開にしたいプロパティ
    def get_name(self): #ゲッター
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name): #セッター
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name) #nameプロパティのゲッターとセッターを定義する

# オブジェクト(インスタンス)を作る
fowl = Duck('Howard')
# nameプロパティを参照すると、実際にはゲッターget_name()メソッドが呼び出される
fowl.name
# inside the getter
# 'Howard'

# ゲッターget_name()メソッドを普通に呼び出すこともできる
fowl.get_name()
# inside the getter
# 'Howard'

# nameプロパティに値を入れると、セッターset_name()メソッドが呼び出される
fowl.name = 'Daffy'
# inside the setter

fowl.name
# inside the getter
# 'Daffy'

# set_name()メソッドを普通に呼び出すこともできる
fowl.set_name('Daffy')
# inside the setter

fowl.name
# inside the getter
# 'Daffy'


#プロパティはデコレータで定義することもできる
# ともにname()という名前を持つが、前につくデコレータが異なる2つのメソッドを定義
# @property
#   ゲッターメソッドの前に付けるデコレータ
# @name.setter
#   セッターメソッドの前につけるデコレータ
class Duck():
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

# オブジェクト(インスタンス)を作る
fowl = Duck('Howard')
# ゲッター
fowl.name
# inside the getter
# 'Howard'

# セッター
fowl.name = 'Donald'
fowl.name
# inside the getter
# 'Donald'

# プロパティは計算された値も参照できる
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self): #ゲッター
        return 2 * self.radius

# オブジェクト(インスタンス)を作る
c = Circle(5)
# 
c.radius    # 5
# diameterプロパティにアクセスする（ゲッター）
c.diameter  # 10
# 別の値を設定
c.radius = 7
c.diameter  # 14
# diameterはセッターを指定していないのでエラー
# diameterは読み出し専用のプロパティとして動作する
c.diameter = 20
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
'''

# プロパティの定義を書き換えても、クラス定義内のコードを書き変えるだけで済み
# 呼び出し元には手を付ける必要がない、というメリットがある
