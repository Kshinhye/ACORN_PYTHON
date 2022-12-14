'''
여러 줄 주석
파이썬은 큰따옴표 작은따옴표 구분하지 않는다.
'''

"""
얘도 여러 줄 주석
하지만 짝은 같아야한다.
"""
# 얘는 한 줄 주석

var1='안녕'
var1=5
print(var1)
#변수 선언 시 type을 선언하지 않음
#파이썬 파일은 모두 모듈이야
print()
a=10
b=12.5
c=b
print(a,'',b,'',c)
print('주소출력:',id(a),'',id(b),'',id(c))
print(a is b,a==b) #주소비교 , 값비교
print(c is b,c==b)

aa=[1000]
bb=[1000]
print(aa==bb,aa is bb)
print(id(aa),'',id(bb))

print('-------------')
A=1; a=2;
print('A+a',A+a,id(A),id(a))

print()
import keyword
print('키워드(예약어) 목록 : ', keyword.kwlist)
#변수명으로 쓸 수 있는건 언더바 영문자 숫자??

print()
print(10,oct(10),hex(10),bin(10))
print(10,0o12,0xa,0b1010)

print('자료형')
print(3,type(3))
print(3.4,type(3.4))
print(3+4j,type(3+4j))
print(True,type(True))
print('good',type('good'))

print((1,),type((1,)))
print([1],type([1]))
print({1},type({1}))
print({'k':1},type({'k':1}))

print(isinstance(1,int))
print(isinstance(1.2,int))