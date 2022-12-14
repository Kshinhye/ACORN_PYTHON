'''
[문항1] 집합형 자료를 이용해 리스트 타입의 li 변수가 기억하고 있는 값의 중복을 제거한 후 계속해서 리스트 타입의 값을 유지하려고 한다.
자료구조의 형식을 변경하는 함수를 이용하려고 할 때, 아래의 빈 칸을 순서대로 채우시오.

li = [1, 2, 2, 2, 3, 4, 5, 5, 5, 2, 2] 
print(li)
im = set(li)
li = list(im)
print(li)
'''

'''
아래의 코드를 수행한 결과와 그 결과가 나온 이유를 간단하게 적으시오.

for i in {1, 2, 3, 4, 5, 5, 5, 5}:
  print(i, end = ' ')
#다시
###i가 set type을 돌기 때문에 중복은 제외하고 나온다.

'''

'''
[문항4] 파이썬에서 사용하는 제어문 중 반복 처리를 위해 사용할 수 있는 명령문을 아는 대로 적으시오 (배점:5)
'''

'''
[문항5] 파이썬에서 아래에 적은 나눗셈 연산자의 차이를 설명하시오.
주의 : 연산 결과가 아니라 차이를 설명해야 함.
1) 5 / 3
2) 5 // 3
3) 5 % 3 (배점:5)
'''

'''
[문항6] 아래 Bar 함수에서 c 는 전역, b는 Foo 함수의 b를 취하려고 한다.
빈 칸에 알맞은 키워드를 차례대로 적으시오. (배점:5)

a = 1; b = 2; c = 3;
def Foo():
    a = 20
    b = 30
    def Bar():
        global c
        nonlocal b
        print('Bar 내의 a:{}, b:{}, c:{}'.format(a, b, c))
        c = 40
        b = 50
    Bar()
Foo()
'''
'''
[문항7] 아래와 같은 명령문을 수행한 후의 결과를 적으시오.
'*' 연산자의 기능도 간단히 적으시오.


*v1, v2, v3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(v1)
print(v2)
print(v3)
'''

''' 
[문항8] 아래의 코드를 람다함수를 이용해 코드를 적으시오. (배점:5)

def Hap(m, n):
    return m + n * 5
print(Hap(5,4))
print((lambda m, n:m+n*5)(5,4))
'''
'''
[문항9] 아래와 같이 range()를 이용하여 리스트 타입의 객체 자료를 출력하려고 한다.
출력 결과를 적으시오.

print(list(range(1, 6, 2))) 
'''

'''
[문항10] 아래 코드에서 키보드를 통해 0이 입력되면 에러가 발생하게 된다.
예외처리를 위한 코드 try ~ except를 이용하여 0 이외의 정수 값은 정상 실행되고 0은 에러 메세지를 출력하도록 변경된 코드를 적으시오.

try:
    aa = int(input('나눌 숫자 입력:'))
    bb = 10 / aa
    print('결과: ',bb)
except ZeroDivisionError:
    print('err: 0으로는 나눌 수 없습니데이')

'''
'''
[문항11] while문을 사용하여 아래와 같은 모양의 *(별 문자)을 출력하는 코드를 작성하시오. 

a=10
while a<=10:
    print(' '*(10-a),'*'*a)
    a-=1
    if a==0: break
'''
'''
[문항12]
if문을 이용하여 프로그램을 작성
james가 키보드를 이용하여, 연도를 입력해 실행
-------------
연도 입력:2020
2020년은 윤년
연도 입력:2022
2020년은 평년
--------------
처리 조건 : 연도는 4의 배수이고 100의 배수가 아니거나 400의 배수이면 윤년이다.

a=int(input('연도 입력:'))
if(a%4==0 and a%100!=0) or a%400==0:
    print('%d년은 윤년'%a)
else:
    print('%d년은 평년'%a)
'''

'''
[문항13] while 문을 사용 : 1 ~ 100 사이의 정수 중에서 3으로 끝나는 숫자만 출력하는 코드를 작성 하시오.
출력 결과는 아래와 같다.
3 13 23 33 43 53 63 73 83 93

i = 0
while True:
    if i%10!=3:
        i += 1
        continue       
               
    if i > 100: break 
                 
    print(i, end=' ')
    i += 1
'''
'''
[문항14]
아래의 출력 예와 같이 키보드로 직급을 입력받아 해당 직급의 직원을 출력하는 코드를 작성하시오.
출력 대상은 직원번호(jikwon_no), 직원명(jikwon_name), 직급(jikwon_jik), 부서번호(buser_num) 이다.
조건 : 테이블은 MariaDB의 jikwon을 사용하기로 한다.

import MySQLdb

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}
def jikwon():
    try:
        conn=MySQLdb.connect(**config)
        cursor=conn.cursor()
        jik=input('직급입력: ')        
        sql="""
            SELECT jikwon_no,jikwon_name,jikwon_jik,buser_num
            FROM jikwon
            WHERE jikwon_jik='{}'
        """.format(jik)

        cursor.execute(sql)
        datas=cursor.fetchall()
        
        if len(datas)==0:
            print('['+jik+']에 해당되는 자료는 없어요')
            return #return은 함수 탈출 sys.exit(0) 프로그램 강제 종료
        
        for jikwon_no,jikwon_name,jikwon_jik,buser_num in datas:
            print(jikwon_no,jikwon_name,jikwon_jik,buser_num)

    except Exception as e:
        print('err: ',e)
    finally:
        cursor.close()
        conn.close()

if __name__=='__main__':
    jikwon()
'''

'''
[문항15] 아래 코드가 동작하도록 자전거 클래스(class)를 정의하시오.
조건 : 바퀴 가격은 바퀴수 * 가격이다.
길동님 자전거 바퀴 가격 총액은 100000원 입니다


class Bicycle():
    
    def __init__(self,name,wheel,price,):
        self.name=name
        self.wheel=wheel
        self.price=price
        
    
    def display(self):
        print('{}님의 자전거 바퀴 가격 총액은 {}원 입니다'.format(self.name,self.price*self.wheel))
    
    

gildong = Bicycle('길동', 2, 50000) # name, wheel, price
gildong.display()

'''







