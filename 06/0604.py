# 6.4 メソッドのオーバーライド
class Car1():
    def exclaim(self):
        print("I'm a Car!")

class Yugo1(Car1):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

give_me_a_car = Car1()
give_me_a_yugo = Yugo1()

give_me_a_car.exclaim()

give_me_a_yugo.exclaim()

#
class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor" + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lower = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lower.name)