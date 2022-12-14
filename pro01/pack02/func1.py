#function(함수)
#클래스를 설명할 수 있어야한다 (1~2분)
#여러개의 수행문을 하나의 이름으로 묶은 실행단위(unit)
#반복 소스의 재활용(단순화)
#디버깅이 쉽다. 유지보수비가 적다.

#내장함수, 사용자 정의 함수
#내장함수: maker가 제공
a=3
print(a)
print(sum([3,5]))
print(bin(8)) #10진수 8을 2진수로 보여줄래?
print(int(1.6), float(3))

a=10
b=eval('a+5') #eval함수:텍스트 문자열 또는 숫자 식 결과를 계산
print(b)

#...c:anaconda3/lib/sqlite
print(round(1.2),round(1.6)) #반올림
import math
print(math.ceil(1.2),math.ceil(1.6)) #정수 근사치 중 큰수
print(math.floor(1.2),math.floor(1.6)) #정수 근사치 중 작은 수

print()
b_list=[True,1,False]
print(all(b_list)) #모든 값이 참이면 참
print(any(b_list)) #하나라도 참이면 참

b_list=[1,3,2,5,7,6,16]
print(all(a<10 for a in b_list))
print(any(a<10 for a in b_list))

print()
x=[10,20,30]
y=['a','b']
for i in zip(x,y): #자주쓰임, 짝을 만들어 줌
    print(i)