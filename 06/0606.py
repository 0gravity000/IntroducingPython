# 6.6 superによる親への支援要請

# 親クラス
class Person():
    def __init__(self, name):
        self.name = name

# 子クラス
# 子クラスが親メソッドを呼び出したい時は、super()を使う
# __init__()をオーバーライドしている
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)  # 引数にselfはいらない。
        self.email = email

# オブジェクト(インスタンス)を作る
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')

# プロパティにアクセスする
bob.name
bob.email

# 以下のようにも書けるけど、継承の意味がなくなってしまう
# super().__init__(name) することで、親クラスが変更しても反映される
# super()を使っていれば、Personクラスの定義が将来変更されても、
# EmailPersonクラスはPersonクラスから継承している属性やメソッドはその変更を反映したものになる
class EmailPerson(Person):
    def __init__(self, name, email):
        self.__init__(name) #ココに注意
        self.email = email
