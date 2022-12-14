#함수 만들기
#def 함수명(매개변수,...):~

print('뭔가를 하다가1...')

def DoFunc1(): #함수의 생성
    print('DoFunc1 수행')
    #return None #생략 가능/ 함수는 반드시 return 값이 있다.
    
print('뭔가를 하다가2 ...')
DoFunc1() #함수의 호출
print('뭔가를 하다가3 ...')
DoFunc1() #함수의 호출
print(DoFunc1) #함수명도 객체, 변수명도 객체
DoFunc2=DoFunc1
DoFunc2()
print(DoFunc1()) #None

def doFunc():
    pass # 수행 할 내용 없을 때

def doFunc3(para1,para2):
    result=para1+para2
    return result

print(doFunc3(10,20))
aa=doFunc3(10,20)
print(aa)
print(id(doFunc3),doFunc3,doFunc3(1,2))
print('현재 파일(모듈)이 사용중인 객체 목록: ',globals())

print(doFunc3('대한','민국'))
#print(doFunc3('대한',1)) #TypeError: can only concatenate str (not "int") to str
#print(doFunc3(1)) #TypeError: doFunc3() missing 1 required positional argument: 'para2'
#print(doFunc3(1,2,3)) #TypeError: doFunc3() takes 2 positional arguments but 3 were given

print()
def doFunc4(arg1,arg2):
    if (arg1+arg2)%2==1:
        return #None을 들고나간다(빈손으로 탈출)
    else:
        aa=doFunc5(arg1,arg2) #함수 내에서 다른 함수 호출
        print(aa)

def doFunc5(arg1,arg2):
    return arg1+arg2

doFunc4(5,6)
doFunc4(6,6)

print()
def swapfunc(a,b):
    return b,a #return (b,a) tuple type으로 묶여 하나의 값으로 반환
    #return [b,a]

a=10; b=20
print(swapfunc(a, b))

#내부함수
print()
def func1():
    print('func1 함수 멤버')
    def func2():
        print('func1의 내부 함수인 func2 멤버')
    func2()
func1()
#func2() #이러면 모듈의 함수를 부르는거 func1의 멤버의 func2를 부르는게 아님

print()
#if 조건식 안에서 함수 사용하기
def isOdd(para):
    #홀수인지만 확인하는 함수
    return para%2==1

print(isOdd(5)) #True
print(isOdd(6)) #False
mydict={x:x*x for x in range(11) if isOdd(x)} #if의 조건으로 함수를 씀 0부터 10까지
print(mydict)

print('함수 연습용 게임---')
import random
import time

def gmaeSijak():
    print('보물을 찾아 여행을 떠나자. 동굴 문은 두개다.')
    print('동굴 속에는 착한 용과 맛있는 용가리 치킨이 있다')
    print('운에 따라 동굴을 선택해 용가리치킨을 얻으면 배가 부르고, 착한 용을 만나면 황천길을 간다.')
    
def chooseCave():
    cave=''
    while cave != '1' and cave != '2':
        print('동굴( 1또는 2)을 선택')
        cave = input()
    return cave
def chkCave(selectNum):
    print('동굴에 도착')
    time.sleep(2)
    rndNum=random.randint(1, 2) #1 아니면 2

    if selectNum==str(rndNum):
        print('와우 맛있는 용가리 치킨을 획득하셨습니다.')
    else:
        print('그 후 그를 본 사람은 아무도 없었다....')

playAgain='y'
while playAgain=='y':
    gmaeSijak()
    caveNumber=chooseCave()
    chkCave(caveNumber)
    print('계속 할까요?? (y / n)')
    playAgain=input()
