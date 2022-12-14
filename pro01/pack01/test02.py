#연산자, 출력 서식
from hamcrest.core.core.isnone import none

#연산자
v1=2 #치환 #왼쪽에 변수 오른쪽에 값을 준다.
v1=v2=v3=v4=5
print(v1,v2,v3,v4)
v1=1,2,3
print(v1)
v1,v2=10,20
print(v1,v2)
v2,v1=v1,v2
print(v1,v2)

print('값 할당 packing')
#v1, *v2=1,2,3,4,5 
*v1,v2=1,2,3,4,5
#*v1,*v2=1,2,3,4,5  #err
print(v1)
print(v2)

v1,v2,*v3=1,2,3,4,5
print(v1,v2,v3)

print()
print('---------------------')
print('\n연산자(산술,관계,논리)')
print(5+3,5-3,5*3,5/3)
print(5//3,5%3,divmod(5,3)) #//은 몫만 %는 나머지 divmod()는 몫과 나머지를 집합형태로

print('연산자 우선순위',3+4*5,(3+4)*5)
#소괄호() 1등 > 산술연살자(** > *,/ > +,-) > 관계연산자 > 논리연산자 > 치환(=)

print('관계연산자')
print(5>3, 5==2, 5!=3)
print('논리연산자')
print(5>3 and 4<3, 5>5 or 4<3, not(5>=3))

print('문자열 더하기 연산자')
print('파이썬'+'만'+'세')
print('파이썬'*5)

print('누적')
a=10
a=a+1
a+=1
print('a:',a)

print()
print(a,a*-1,-a,--a)

print('bool:',True,False,type(True))
print(bool(True),bool(1),bool(-23.4),bool('kbs'))
print(bool(False),bool(0.0),bool(''),bool(None),bool([]),bool(()),bool({}))

print('***'*10)
#출력서식 카페 게시글50번
#쓰임이 많지는 않아요
#print(출력데이타,서식)
print(format(123.45678, '10.3f'))
print(format(123.45678, '10.3')) 
print(format(123, '10d'))
# 소수점 이하 셋째 자리까지 부동 소수점(f) 숫자 표기 (0.333)
print ('{0:.3f}'.format(1.0/3))
# 밑줄(_)로 11칸을 채우고 가운데 정렬(^)하기 (___hello___)
print ('{0:_^11}'.format('hello'))
#요거는 좀 많이 쓰여요
print('이름:{0}, 가격:{1}'.format('마우스', 5000))
print('이름:{}, 가격:{}'.format('마우스', 5000))
print('이름:{0}, 가격:{1}'.format('마우스', 5000, '마우스', 5000))
print('이름:{0}, 가격:{1} 이름:{0}, 가격:{1}, 가격:{1}'.format('마우스', 5000))
print('이름은 {0}, 나이는 {1}'.format('한국인', 33))
print('이름은 {}, 나이는 {}'.format('신선해', 33))
print('이름은 {1}, 나이는 {0}'.format(34, '강나루'))
#요것도 많이 쓰여요
print('나는 나이가 %d 이다.'%23)
print('나는 나이가 %s 이다.'%'스물셋')
print('나는 나이가 %d 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 나이가 %s 이고 이름은 %s이다.'%(23, '홍길동'))
print('나는 키가 %f이고, 에너지가 %d%%.'%(177.7, 100))
#raw string
print('~~~~~'*10)
print('aa\tbb')
print(r'aa\tbb') #raw string을 선행하면 이스케이프 기능이 해제된다
print("c:\aa\bbc\nbc.txt")
print(r"c:\aa\bbc\nbc.txt")
#print는 java에서 println같은애라서 라인스킵이 있다.
print('aa',end=', ') #그게 싫으면 end='' 속성을 사용하면 된다.
print('bb')





