#클래스의 이해

kor=100 #전역변수 모듈 소속이야

def abc(): #함수 모듈 소속이야
    a=10 #지역변수 abc 함수의 소속이야
    print('함수')
    
class MyClass: #MyClass() 굳이 쓰지는 마세요 #클래스 모듈 소속이야
    kor=90 #멤버 변수 MyClass의 소속이야

    '''
    #클래스는 반드시 생성자가 있어야하지만 생성자에 쓸 내용이 없어? 생략해도 돼(그냥 쓰지 않을 뿐)
    def __init__(self):
        pass
    '''
    
    def abc(self):
        print('이거는 메소드햐아 소속이 어디야 MyClass햐아') #클래스에 소속되어있으니 function이 아니라 method
    
    def show(self):
        kor=80 #지역변수
        print(self.kor) #90 #kor=90 얘 일수도 있고 아닐수도 있어, 근데 지금은 얘야
        print(kor) #80 #위위에 kor=80 을 주석처리하면 전역변수 kor=100을 참조함
        self.abc() #메소드를 콜
        abc() #함수를 콜
        
my=MyClass()
my.show()