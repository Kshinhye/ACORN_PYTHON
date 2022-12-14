'''#자드
class CoinIn:
    
    def culc(self):
        self.coin=int(input('동전을 넣어주세요 '))
        return self.coin
    
class Machine:
    
    def showData(self):
        print('커피는 한잔에 200원 입니다')
        self.coin=CoinIn().culc()
        self.cupCount=int(input('몇잔을 원하세요? '))
        
        if 200*self.cupCount > self.coin:
            print('요금이 부족합니다')
        elif 200*self.cupCount <= self.coin:
            refund=self.coin-(200*self.cupCount)
            print('커피 %d잔과'%self.cupCount,'잔돈 %d원'%refund)
        
if __name__=='__main__':
    Machine().showData()
    
class CoffeeMachine:
        
    def getCoffee(self, cupCount, change):
        print('커피 {}잔, 잔돈 {}원 입니다'.format(cupCount, change))
'''

'''#이란
class Coinin:  
    coin = 0
    change = 0      
    price = 200
    def __init__(self):
        self.machine = CoffeeMachine()
    
    def buyCoffee(self):
        
        self.coin = int(input('동전을 입력하세요: '))
        
        if self.coin < self.price:
            print('요금이 부족합니다.')    
        else:
            cupCount = int(input('몇잔을 원하시나요?: '))
            if self.coin < self.price*cupCount:
                print('요금이 부족합니다.')   
            elif self.coin >= self.price*cupCount:
                self.change = self.coin -self.price*cupCount
                self.machine.getCoffee(cupCount, self.change)


if __name__ =='__main__':
    Coinin().buyCoffee()
'''