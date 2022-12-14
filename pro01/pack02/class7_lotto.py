#클래스의 포함관계: 로또번호 출력기

import random

class LottoBall:
    def __init__(self,num):
        self.num=num

class LottoMachine:
    def __init__(self):
        self.ballList=[]
        for i in range(1,46):
            self.ballList.append(LottoBall(i)) #클래스의 포함 로또 머신에다가 로또볼 생성자를 부르고있다. 번호를 가져간다.
            
    def selectBalls(self):
        #볼 섞기 전 출력하기
        for a in range(45):
            print(self.ballList[a].num, end=' ')
        random.shuffle(self.ballList)
        print()
        for a in range(45):
            print(self.ballList[a].num,end=' ')
        
        return self.ballList[0:6]
        
class LottoUi:
    def __init__(self):
        self.machine=LottoMachine() #포함관계
    
    def playLotto(self):
        input('로또를 시작하려면 엔터키를 누르세요')
        selectedBalls=self.machine.selectBalls()
        print('당첨번호')
        for ball in selectedBalls:
            print('%d '%ball.num,end=' ')

if __name__ =='__main__':
    #lo=LottoUi()
    #lo.playLotto() 이 둘중을 아래 한줄로
    LottoUi().playLotto()