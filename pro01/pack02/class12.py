#다중상속: 순서가 중요(누구를 먼저 받았냐)

class Tiger:
    def cry(self):
        print('호랑이는 야옹')
    
    def eat(self):
        print('맹수는 생닭 츄르를 좋아해요')
    
class Lion:
    data="사자 세상"
    
    def cry(self):
        print('사자는 으르렁')
        
    def hobby(self):
        print('백수의 왕은 낮잠을 즐겨요')
        
class Liger1(Tiger,Lion): #다중상속
    pass

a1=Liger1()
a1.cry()
a1.eat()
a1.hobby()
print(a1.data)

print('-------------------------')
class Liger2(Lion,Tiger):
    data='라이거 만세'
    
    def hobby(self):
        print('라이거는 자바를 조아해')
        
    def showData(self):
        print(self.data, '',super().data)
        self.hobby()
        super().hobby()
        #hobby() #얘는 모듈의 함수를 부르는거 위에 두개애들은 메소드를 부르는거 구분해야합니다!!
        
a2=Liger2()
a2.cry()
a2.eat()
a2.hobby()
a2.showData() #라이거만세  #사자 세상
