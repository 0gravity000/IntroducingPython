# 6.5 メソッドの追加
class Car1():
    def exclaim(self):
        print("I'm a Car!")

class Yugo1(Car1):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car1()
give_me_a_yugo = Yugo1()

give_me_a_yugo.need_a_push()

# エラー
give_me_a_car.need_a_push()