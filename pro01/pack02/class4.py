#class: 새로운 타입을 생성

print('가수 관련 클래스')

class SingerType:
    title_song='LOVE'
    
    def sing(self):
        msg='노래는'
        print(msg,self.title_song+'사랑이 뭐라고 생각해?')
