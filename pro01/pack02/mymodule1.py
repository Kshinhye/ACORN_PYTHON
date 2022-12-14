#메인으로 사용하지 않고 다른 모듈에 호출 될 멤버를 기술하는 용도

price=12345

def listHap(*ar):
    print(ar)
    
    if __name__ == '__main__':
        print('나는 최상위 메인 모듈이야') #얘가 안뜨면 최상위가 아닌거임
    
def kbs():
    print('대한민국 대표 방송')
    
def mbc():
    print('만나면 좋은 친구')
    
