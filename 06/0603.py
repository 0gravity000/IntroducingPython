# 6.3 継承
# 子クラスでは、追加、変更したい部分だけを定義する
# そうすると、追加、変更した部分が使われ、親クラスのものは使われない
# これをオーバーライドという

# 親クラス
class Car():
    pass

# 子クラス
class Yugo(Car):
    pass

# それぞれのクラスからオブジェクト(インスタンス)を作る
give_me_a_car = Car()
give_me_a_yugo = Yugo()

# 親クラスでexclaim()メソッドを定義
class Car1():
    def exclaim(self):
        print("I'm a Car!")

# 子クラスで継承する
class Yugo1(Car1):
    pass

# それぞれのクラスからオブジェクト(インスタンス)を作る
give_me_a_car = Car1()
give_me_a_yugo = Yugo1()

give_me_a_car.exclaim()
# 子クラスは親クラスのexclaim()メソッドを継承している
give_me_a_yugo.exclaim()