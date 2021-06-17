#class 메소드 심화

class Line:
    def __init__(self, length):
        self.length=length
        print(self.length, '길이의 선이 생성되었다.')

    def __del__(self):
        print(self.length,'길이의 선이 삭제되었다.')

    def __repr__(self):
        return '선의 길이: '+str(self.length) #print()문으로 출력할때 실행되는 메서드

    def __add__(self, other):
        return self.length + other.length

    def __lt__(self, other):
        return self.length < other.length

    def __eq__(self, other):
        return self.length == other.length

#main code
myLine1= Line(100)
myLine2= Line(200)

print(myLine1)
print(myLine2)

print('두 선 길이의 합:',myLine1 + myLine2)

if myLine1 < myLine2:
    print('선분2가 더 기네요')
elif myLine1 == myLine2:
    print('선분 길이가 같네요')
else:
    print('모르겠네요')

del(myLine2)