# 6.5 メソッドの追加

# 親クラス
class Car1():
    def exclaim(self):
        print("I'm a Car!")

# 子クラス
# 子クラスは親クラスにないメソッドneed_a_push()を追加できる
class Yugo1(Car1):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

    def need_a_push(self):
        print("A little help here?")

# オブジェクト(インスタンス)を作る
give_me_a_car = Car1()
give_me_a_yugo = Yugo1()

# 子クラスの追加メソッドneed_a_push()を呼び出し
give_me_a_yugo.need_a_push()

# 親クラスでは、追加メソッドneed_a_push()を呼び出しエラー
give_me_a_car.need_a_push()