#추상클래스(추상메소드) : 자식클래스에서 부모 메소드의 이름을 강요하도록 함

from abc import *

class AbstractClass(metaclass = ABCMeta):  #abc클래스를 상속받으면 추상크래스가 된다
    @abstractmethod
    def myMethod(self): #@abstractmethod을 하면 추상 메소드가 됨
        pass
    
    def normalMethod(self):
        print('추상클래스는 일반 메소드를 가질 수도 있따')
        
#parent=AbstractClass() #err : 추상클래스는 객체를 만들 수 없다.TypeError: AbstractClass.__init_subclass__() takes no keyword arguments

class Child1(AbstractClass):
    name='난 Child'
    
    #추상의 족쇄에서 벗어나기 위한 오버라이딩
    def myMethod(self):
        print('Child1에서 추상메소드에 내용을 적어서 오버라이드함')
    
c1=Child1() #오버라이딩 없이 쓰면 에러 TypeError: AbstractClass.__init_subclass__() takes no keyword arguments
print(c1.name)
c1.myMethod()
c1.normalMethod()
print()

class Child2(AbstractClass):
    def myMethod(self):
        print('Child2에서 추상의 마법을 풀다/추상에서 빠져나옴')
        print('이제는 자유다')

    def normalMethod(self):
        print('추상클래스의 일반 메소드는 오버라이딩이 선택적이다') #안하면 부모꺼 수행 하면 자식꺼 수행
        
    def good(self):
        print('Child2 고유 메소드')
        
c2=Child2()
c2.myMethod()
c2.normalMethod()
c2.good()

print('-----------------')
imsi=c1
imsi.myMethod()
print()
imsi=c2
imsi.myMethod()