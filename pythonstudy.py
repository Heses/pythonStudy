#387p
class Car: #클래스 생성
    name=""
    speed=0

    def __init__(self, name, speed): #생성자 생성
        self.name=name
        self.speed=speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

#변수 선언
car1, car2= None, None

#메인 코드
car1= Car("아우디",0) #인스턴스 생성
car2= Car("벤츠",30)

print("%s의 현재 속도는 %d입니다" %(car1.getName(), car1.getSpeed()))
print("%s의 현재 속도는 %d입니다" %(car2.getName(), car2.getSpeed()))