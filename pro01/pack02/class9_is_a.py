#클래스의 상속: 다형성을 구사 가능 자원의 재활용을 목적으로 하는거지
#원래 부모 클래스는 별도의 파일에 따로 만들어두고 자식에서 import한 후 사용해야하지만 공부를 위해 한곳에 작성한다.
class Animal:
    def __init__(self):
        print('Animal 생성자(부모)') #자식클래스에 생성자가 있으면 자식 클래스의 생성자만 호출된다.
    def move(self): #메소드
        print('움직이는 생물')

class Dog(Animal): #상속 #Animal의 파생 클래쓰가 되어따.
    def __init__(self):
        print('Dog 생성자(자식)') #자식클래스에 생성자가 있으면 자식 클래스의 생성자만 호출된다.
    def my(self): #메소드
        print('난 댕댕이~')

dog1=Dog()
#dog1. #점을 찍어도 안나오는 이유는 class에 아무것도 없어서 (그냥 class Dog: pass)적어뒀을 때
dog1.move()  #움직이는 생물
dog1.my()

print()
class Horse(Animal):
    pass

horse1=Horse()
horse1.move()