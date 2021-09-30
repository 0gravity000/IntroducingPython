# 6.4 メソッドのオーバーライド

# 親クラス
class Car1():
    def exclaim(self):
        print("I'm a Car!")

# 子クラスでexclaim()メソッドをオーバーライドする。
# exclaim()の振る舞いが書き換えられる
class Yugo1(Car1):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

# オブジェクト(インスタンス)を作る
give_me_a_car = Car1()
give_me_a_yugo = Yugo1()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

# 親クラス
class Person():
    def __init__(self, name):
        self.name = name

# 子クラス
class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

# 子クラス
class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

# オブジェクト(インスタンス)を作る
person = Person('Fudd')
doctor = MDPerson('Fudd')
lower = JDPerson('Fudd')

print(person.name)  # Fudd
print(doctor.name)  # Doctor Fudd
print(lower.name)   # Fudd, Esquire

