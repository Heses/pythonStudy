
#Thread : 프로그램 하나에서 여러 작업을 동시에 처리하도록 하는 기능
#Multi Thread : 여러 개의 스레드를 작동하는 것

import time
import threading

class RaceCar:
    carname=''
    def __init__(self,name):
        self.carname=name

    def runcar(self):
        for _ in range(0,3): #변수 없이 for문 돌리려면 _ 사용, 띄어쓰기 주의
            carStr=self.carname+'~~running.\n'
            print(carStr,end='')
            time.sleep(0.1) #0.1sec stop

car1=RaceCar('자동차1')
car2=RaceCar('자동차2')
car3=RaceCar('자동차3')
car4=RaceCar('자동차4')

th1=threading.Thread(target=car1.runcar)
th2=threading.Thread(target=car2.runcar)
th3=threading.Thread(target=car3.runcar)

th1.start()
th2.start()
th3.start()