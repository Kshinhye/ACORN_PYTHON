#가수 한명을 탄생

#방법1
#import pack2.cpack02
from pack2.class4 import SingerType

def process():
    #Monsta=pack2.cpack02.SingerType()
    Monsta=SingerType()
    print('몬스타엑스 타이틀 :',Monsta.title_song)
    Monsta.sing()

def process2():
    bts=SingerType() #생성자를 호출해서 객체를 넘김
    #bts=SingerType #주소를 치환
    bts.sing()
    bts.title_song= 'yet to come'
    bts.sing()
    bts.co="HIVE"
    print('소속사:', bts.co)
    print()
    blackpink=SingerType()
    blackpink.sing()
    blackpink.title_song='shutdown'
    blackpink.sing()
    #print('소속사:',blackpink.co) #err:AttributeError: 'SingerType' object has no attribute 'co'

#누가봐도 여기가 메인모듈이라구나 응용프로그램이 여기서 시작되는구나 하고 가독성 좋게 보임! 이걸 권장(급할 땐 안씀)
#process()
if __name__ == '__main__':
    process()
    print('-----')
    process2()
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        