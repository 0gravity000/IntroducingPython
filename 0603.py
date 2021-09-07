# 6.3 継承
class Car():
    pass

class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()

class Car1():
    def exclaim(self):
        print("I'm a Car!")

class Yugo1(Car1):
    pass

give_me_a_car = Car1()
give_me_a_yugo = Yugo1()

give_me_a_car.exclaim()

give_me_a_yugo.exclaim()