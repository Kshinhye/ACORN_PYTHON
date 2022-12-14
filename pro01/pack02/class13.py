#상속
#카페 파이썬 24번 2번 문제
#ElecProduct의 sub class 두개를 만들고 volumeContro()을 overriding하여 다형성을 구현하시오

#추상클래스는 부모로써의 의미만 있다.
#자식은 추상클래스를 바로 오버라이딩 해야한다.
class ElecProduct:
    volume=0
    
    def volumeControl(self,volume):
        pass
    
class ElecTv(ElecProduct):
    def volumeControl(self, volume):
        self.volume +=volume
        print('ElecTV 소리 크기: ',self.volume)    
        
class ElecRadio(ElecProduct):
    def volumeControl(self, volume):
        imsi=self.volume+volume
        self.volume = imsi
        print('ElecRadio 소리 크기: ',self.volume)
        
tv=ElecTv()
radio=ElecRadio()
abc=tv #tv.하고 불러도되고 이렇게 불러도 되고
abc.volumeControl(3)

abc=radio
abc.volumeControl(3)

