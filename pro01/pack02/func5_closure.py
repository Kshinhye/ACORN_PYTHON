#클러저(closure): scope에 제약을 받지 않는 변수를 포함하고 있는 코드 블록이다.
#내부함수의 주소를 반환함으로써 함수 내의 지역변수를 함수 밖에서 참조 가능
from sympy.physics.units import amount

#아직 클로져 들어가기전에 선행학습
def funcTimes(a,b):
    c=a*b
    return c

print(funcTimes(2, 3))

kbs=funcTimes(2, 3)
print(kbs)
kbs=funcTimes #함수의 이름이 주소를 가지고 있다.
print(kbs)
print(kbs(2,3))
print(id(kbs),id(funcTimes))

del funcTimes
#funcTimes() #얘는 err 정의도 안됐는데 뭘 실행해 NameError: name 'funcTimes' is not defined
print(kbs(2, 3))

mbc=sbs=kbs #변수명과 함수명은 어떻게보면 하는일이 가태~
print(mbc(2,3))
#-------------------------------------------------
'''
print('클로저를 사용하지 않는 경우')
def out():
    count=0  #out의 카운트
    def inn():
        count+=1  #inn의 카운트 값이 없는애한테 1을 주면 에러 #UnboundLocalError: local variable 'count' referenced before assignment
    inn()
out() 
'''
print('클로저를 사용하지 않는 경우')
def out():
    count=0  
    def inn():
        nonlocal count
        count+=1
        return count
    #print(inn())
    imsi=inn()
    return imsi
#print(count)#err 전역이 아님 로컬이라서 에러
#out()
#out()
print(out())

print('클로저를 사용한 경우')
def outer():
    count=0  
    def inner():
        nonlocal count
        count+=1
        return count
    return inner  #<==요게 클로저: 내부 함수의 주소를 반환하는 것

var1=outer() #inner이 주소를 리턴받음
print(var1)
print(var1())
print(var1())
print(var1())

print('***수량*단가*세금을 계산하는 함수 만들기***')
#주소의 개념을 이용해 함수 밖에서 함수안에있는 애를 이용하고 있다.
#분기별로 세금은 동적이다.
def outer2(tax): #함수 안에서 선언한거니까 지역변수
    def inner2(su,dan):
        amount=su*dan*tax
        return amount
    #inner2() 여기서 이렇게 객체를 만들어 버리면 안됨!
    #return inner2() #이렇게하면 결과를 리턴
    return inner2 #이렇게 주소를 리턴해야함!!

#1분기에는 tax가 0.1(10%) 부과
q1=outer2(0.1) #q1은 inner2의 주소를 기억한다.
result1=q1(5,50000)
print('result1:',result1)
result2=q1(1,10000)
print('result2:',result2)

#2분기에는 tax가 0.05(5%) 부과
q2=outer2(0.05) #q1은 inner2의 주소를 기억한다.
result3=q2(5,50000)
print('result3:',result3)
result4=q2(1,10000)
print('result4:',result4)


















