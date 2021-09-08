# 6.7 selfによる自己弁護
class Car1():
    def exclaim(self):
        print("I'm a Car!")

car = Car1
car.exclaim()

# これでもOK。car.exclaim()と同じ
# でもあえて使う理由はない
Car1.exclaim(car)
