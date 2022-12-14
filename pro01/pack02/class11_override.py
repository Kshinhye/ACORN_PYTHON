#method override(재정의)
#다형성 폴리모피즘?:동일한 이름의 메소드지만 기능은 다양함

class Parent:
    def printData(self):
        pass

class Child1(Parent): 
    def printData(self):  #이것이 바로 메소드 오버라이딩 #동일한 메소드지만 기능은 달라
        print('Child1에서 재정의')

class Child2(Parent): 
    def printData(self):  #이것이 바로 메소드 오버라이딩 #동일한 메소드지만 기능은 달라
        print('Child2에서 재정의')
        print('오버라이드는 부모의 메소드를 자식이 재정의')
        
    def abc(self):
        print('Child2의 고유 메소드')

c1=Child1()
c1.printData()
print()
c2=Child2()
c2.printData()
print()
print('다형성-------(JAVA랑 이런 차이가 있구나 하는 정도만 알아두세용)')
#par=Parent() #부모의 객체변수 #파이썬에서는 얘 필요없음
par=c1 #그냥 아무 변수에 넘겨주고 수행하면 됩니다
par.printData()
print()
par=c2
par.printData()
par.abc()

print()
plist=[c1,c2] #c1,c2 둘 다 parent type
for i in plist:
    i.printData()
    ''' (console)
    Child1에서 재정의
    Child2에서 재정의
    오버라이드는 부모의 메소드를 자식이 재정의
    '''
