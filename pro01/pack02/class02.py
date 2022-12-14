#클래스

class Car:
    handle=0 #멤버 변수  #Car type의 객체에서 참조 가능 멤버 필드
    speed=0 #멤버 변수
    
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
        
    def showData(self): #Car type의 객체에서 참조 가능 멤버 필드
        km='킬로미터'
        msg='속도:' + str(self.speed)+km + ',핸들은' +str(self.handle)#클래스를 부를 땐 self #km같은 지역변수를 부를 땐 그냥
        return msg
    
print(id(Car))
print(Car.handle)
print(Car.speed)
print()
car1=Car('tom',10) #생성자 호출 후 객체 생성 #JAVA Car car1=new Car()
print(car1.handle,car1.name,car1.speed) #지역이 우선 지역을 우선 찾음
car1.color='보라' #car1고유의 멤버 필드 #JAVA는 반드시 설계도에 있는것만 참조할 수 있지만 Python은 이게 가능
print('car1.color: %s'%car1.color)
print('------------------------')
#car2=Car() #err TypeError: __init__() missing 2 required positional arguments: 'name' and 'speed'
car2=Car('James',20)
print(car2.handle,car2.name,car2.speed)
#print('car2 color: %s'%car2.color) #AttributeError: 'Car' object has no attribute 'color'

print('주소:',id(Car),id(car1),id(car2)) 
print()
print(car1.showData())
print(car2.showData())
print(Car.showData(car2))
print('~~~')
car2.speed=100
Car.handle=1
car1.handle=2
print('car2:',car2.showData()) #스피커 빵빵한 현성이는 속도:100킬로미터
print('car1:',car1.showData()) #인형 커스텀한 소현이는 속도:10킬로미터
print()