#클래스의 상속

class Person:
    say='나는 인간입니다.'
    nai='22' #프로토타입의 멤버'
    __kbs='공영방송' #private 멤버 변수 (Person class에서만 유효하다)
    
    def __init__(self,nai): #nai를 받는다.
        print('Person 생성자')
        self.nai=nai #persontype의 객체가 만들어질 때 갖는 나이 / 위에 nai와 기억장소가 다르다.
        #person객체 타입의 멤버
        
    def printInfo(self):
        print('나이:{},이야기:{}'.format(self.nai,self.say))
    
    def hello(self):
        print('안녕',self.__kbs)
        
print(Person.say,Person.nai)
#Person.printInfo() #파라미터를 만족시킬 수 없어서 err TypeError: printInfo() missing 1 required positional argument: 'self'
p=Person('24')  #객체변수 그냥 만들어볼게요 p는 self로 들어가고 nai는 self.nai의 nai로 들어간다.
#아래 쓸 일은 잘 없겠지만 그냥 해본겁니다.
p.printInfo()
p.hello()

print('*********Employee*************')
'''
#생성자가 없는 경우
class Employee(Person):
    pass

emp=Employee('26')
emp.printInfo()
'''
#생성자가 있는 경우
class Employee(Person):
    say='일하는 동물' #부모의 멤버는 자식에 의해서 캡슐화 된다(숨는다)
    subject='근로자'
    
    def __init__(self):
        print('Employee 생성자')
    
    def printInfo(self):
        print('Employee의 printInfo 메소드')
        
    def empPrintInfo(self): #여기서 self는 Employee기 때문에 Employee에서 찾을거야
        print(self.say,self.nai,self.subject) #Employee에서 찾다가 없으니 부모로 올라간다.
        print(self.say,super().say,self.nai,super().nai) #self.say:일하는 동물 #super().say:나는 인간입니다.
        #printInfo() #self없이 그냥 이렇게 입력하면 모듈이 함수를 찾는다.
        self.printInfo() #현재 클래스(Employee부터 뒤짐)
        super().printInfo() #처음부터 부모클래스를 뒤져본다
        self.hello()
        #print(super().say,super().__kbs) #private 멤버기 때문에 안됨
        #AttributeError: 'super' object has no attribute '_Employee__kbs'
        
        

emp=Employee()
emp.printInfo()
emp.empPrintInfo()

'''
#TypeError: __init__() takes 1 positional argument but 2 were given
emp=Employee('26') #임플로이의 생성자를 보면 나이를 안받고 있잖아, 그니까 이때는 쓰면 에러야
emp.printInfo()
'''
''' 
emp=Employee()
emp.printInfo() 
#이걸 임플로이에서 찾는데 프린트 인포가 없으니 부모로 올라간다. 그래서  def printInfo(self):
print('나이:{},이야기:{}'.format(self.nai,self.say)) 에 임플로이 주소가 담기는데 여기에 나이가 없잖아
그러니까 부모 프로토타입으로 가서 나이를 찾아서 22살이 출력된다
'''


print('*********Worker*************')
class Worker(Person):
    def __init__(self,nai):
        print('Worker 생성자')
        super().__init__(nai) #위아래 아무곳이나 가능 #부모 생성자 호출 #Bound method call
        #()안에 nai랑 self(주소)를 달고 부모한테 간다.
    def wPrintInfo(self):
        self.printInfo()  #wor의 주소를 가지고 부모한테 간다.

wor=Worker('28')
print(wor.say,wor.nai) #wor.say 하면 먼저 Worker에서 뒤져본다 /wor이 객체의 주소를 기억한다. 그 객체에는 나이28이 들어있다.
wor.wPrintInfo()

print('---------Programer-----------')
class Programer(Worker):
    def __init__(self,nai):
        print('Programer 생성자')
        #super().__init__(nai)     #Bound method call
        Worker.__init__(self, nai) #UnBound call #self가 pr의 주소와 30을가지고Woker로 간다.

    def ProShow(self):
        self.printInfo()

pr=Programer('30')
print(pr.say,pr.nai) #나는 인간입니다. 30
pr.ProShow()         #나이:30,이야기:나는 인간입니다.

print('~~~~~~~~~~타입을 확인해볼게영~~~~~~~~~~~')
print(type(3))
print(type(pr))
print(type(wor))
print(Programer.__bases__, Worker.__bases__, Person.__bases__)

















