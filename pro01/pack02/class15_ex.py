#Python 24번: 추상 클래스를 이용한 상속 연습문제

from abc import *

class Employee(metaclass=ABCMeta):

    def __init__(self,irum,nai): #고유의 인스턴스
        self.irum=irum
        self.nai=nai

    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def data_print(self):
        pass

    def irumnai_print(self):
        print('이름: '+self.irum+', 나이: '+str(self.nai),end='')
#선생님 풀이
class Temporary(Employee):
    ilsu=0
    ildang=0
    
    def __init__(self,irum,nai,ilsu,ildang):
        Employee.__init__(self,irum, nai)
        self.ilsu=ilsu;
        self.ildang=ildang;
    
    def pay(self):
        return self.ilsu * self.ildang
        
    def data_print(self):
        self.irumnai_print();
        print(', 월급: '+str(self.pay()))
    
t=Temporary('홍길동',25,20,150000)
t.data_print()

class Regular(Employee):
    def __init__(self,irum,nai,salary):
        super().__init__(irum, nai)
        self.salary=salary
        
    def pay(self,salary):
        return self.salary
        
    def data_print(self):
        print('이름: {}, 나이: {}, 급여: {}'.format(self.irum,self.nai,self.salary))
    
r=Regular('한국인',27,3500000)
r.data_print()

#신혜 풀이
class Salesman(Regular):
    def __init__(self,irum,nai,salary,sales,commission):
        super().__init__(irum, nai,salary)
        self.sales=sales;
        self.commission=commission
        
    def pay(self):
        self.su=self.salary+round(self.sales*self.commission)
        
    def data_print(self):
        print('이름: {}, 나이: {}, 수령액: {}'.format(self.irum,self.nai,self.su))
      
s=Salesman('손오공',29,1200000,5000000,0.25)
s.pay()
s.data_print()