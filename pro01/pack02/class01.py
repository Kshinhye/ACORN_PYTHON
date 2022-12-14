# class: 새로운 타입을 만드는 것(생성), 객체 지향적(중심적)인 프로그래밍(자원의 재활용가능)
# 별도에도 메모리를 확보하게된다 oop가 뭐니
# 형식| class 클래스명():멤버(필드일수도 있고, 메소드가 있을 수도 있다)~
# 생성자, 소멸자가 있다.
# 접근지정자(public,private)가 없다. 메소드 오버로딩이 없다.
# 다중상속이 가능하다. interface가 없다.

print('뭔가를 하다가 모듈의 멤버인 클래스를 선언하기')

##파이썬의 세계에서는 new없이 객체로 만들어진다. 이것이 바로 프로토 타입이다 원형 클래스
class TestClass: #prototype, 원형클래스 객체 생성. 고유의 이름 공간을 확보
    aa=1 #멤버변수(멤버필드),public

    def __init__(self):  #constructor 생성자 
        print('생성자')
        
    def __del__(self):
        print('소멸자')
        
    def printMessage(self): #method
        name='한국인' #지역변수
        print(name)
        print(self.aa) #클래스의 멤버를 호출할 땐 self를 쓴다 (자바에서 this처럼)

print(TestClass,id(TestClass))
##그래서 프린트 한 다음 TestClass.aa 하면 1이 찍힌다.
print(TestClass.aa)

print()
test=TestClass() #생성자 호출한 후 TestClass type의 객체가 하나 또 만들어 진겁니다~ (객체 생성)
print(test.aa) #멤버필드 호출

#메소드 호출
#TestClass.printMessage() #err:printMessage() missing 1 required positional argument: 'self’
test.printMessage() #Bound method call
print()
TestClass.printMessage(test) #UnBound method call

print()
print(type(1))
print(type(1.1))
print(type(test)) #TestClass type 내가 새로 만든거임!
print(id(test),id(TestClass))





















