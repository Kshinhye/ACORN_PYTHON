#함수: argument와 parameter 키워드로 matching 하기
#매개변수 유형
#위치 매개변수: 인수와 순서대로 대응
#기본값 매개변수: 매개변수에 입력값이 없으면 기본값 사용
#키워드 매개변수: 인수와 매개변수를 동일이름으로 대응
#가변 매개변수: 인수의 갯수가 동적인 경우

def showGugu(start,end=5):
    for dan in range(start,end+1):
        print(str(dan)+'단 출력')
        
showGugu(2,3)
print()
showGugu(3)
print()
showGugu(start=2,end=3)
print()
showGugu(end=3,start=2) #이름에 의한 매칭이기 때문에 에러가 아니다
print()
showGugu(2,end=3) #순서,이름에 의한 매칭이기 때문에 에러가 아니다
print()
#showGugu(start=2,3) #SyntaxError: positional argument follows keyword argument 문법오류
#showGugu(end=3,2)  #SyntaxError: positional argument follows keyword argument
#상수를 주면 안된다.

#패킹연산이 파라미터에도 적용된다.
print('\n가변인수 처리')
def func1(*ar):
    #print(ar)
    for i in ar:
        print('밥:'+i)

print()
func1('비빔밥','공기밥')
func1('비빔밥','공기밥','김밥')

#def func2(*ar,a):  #TypeError: func2() missing 1 required keyword-only argument: 'a'
def func2(a,*ar):
    print(a)
    for i in ar:
        print('밥:'+i)

print()
func2('비빔밥','공기밥')
func2('비빔밥','공기밥','김밥')

print()
def calcProcess(op,*ar):
    if op == 'sum':
        re=0
        for i in ar:
            re+=i
    elif op == 'mul':
        re=1
        for i in ar:
            re*=i
    return re

print(calcProcess('sum',1,2,3,4,5))
print(calcProcess('mul', 1,2,3,4,5))
print(calcProcess('mul', 1,2,3,4,5,1,2,3,4,5))

print()
#dict형 처리
#** 여기저기서 써먹을거얌 특히 DB연동할 때 많이 써먹을거얌4
#변수=값 형식으로 입력하면 파라미터가 dict로 받아들인다. 변수:값으로 넘기면 err
def func3(w,h,**other):
    print('w:{},h:{}'.format(w,h))
    print(other)

func3(55,160)
func3(55,160,irum='홍길동') #dict에 값을 넣어줄 땐 이렇게 써야해
func3(55,160,irum='홍길동',nai=23)

#종합형
print()
def func4(a,b,*c,**d): #*c 
    print(a,b)
    print(c)
    print(d)
#func4(1) #err
func4(1,2)
func4(1,2,3) #*c 가 받아서 1 2 (3,) 이렇게 나옴
func4(1,2,3,4,5,x=6,y=7) #1 2  (3, 4, 5)  {'x': 6, 'y': 7}


























