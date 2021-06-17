class Car:
    speed=0
    def upspeed(self, val):
        self.speed+=val
        print("현재 속도(슈퍼 클래스): %d" %self.speed)

class Seden(Car):
    def upspeed(self, val):
        self.speed+=val

        if self.speed>150:
            self.speed=150
            print("현재 속도(서브 클래스): %d" %self.speed)

class Truck(Car):
    pass

sedan1, truck1 =None, None

truck1= Truck()
sedan1= Seden()

print("트럭-->",end="")
truck1.upspeed(200)

print("승용차-->",end="")
sedan1.upspeed(200)