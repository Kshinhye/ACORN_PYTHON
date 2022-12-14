#Module: 소스 코드의 재사용을 가능하게 할 수 있으며, 소스코드를 하나의 이름 공간으로 구분하고 관리하게 된다.
#하나의 파일은 하나의 모듈이 된다.
#표준 모듈, 사용자 작성 모듈, 제3자 모듈(Third party) 모듈

#모듈의 멤버: 전역변수, 실행문, 함수, 클래스, 모듈

a=10
print(a)

def abc():
    print('abc는 모듈의 멤버 중 함수')
    
abc()

#표준모듈(내장된 모듈 읽기)
import math #표준모듈을 로딩하고 있다.
print(math.pi) #.찍었을 때 ()가 있으면 func아니면 method /행위가 있다는거 없으면 멤버아님 전역변수(?)
print(math.sin(math.radians(30)))

import calendar
calendar.setfirstweekday(6) #0:월요일
calendar.prmonth(2022,10)

import os
print(os.getcwd())
print(os.listdir('/'))

print()
import random
print(random.random())
print(random.randint(1,10))

from random import random
print(random())

from random import randint,randrange
print(randint(1, 10))

from random import * #이러면 전부 다 올라오기 때문에 메모리 낭비라서 권장하지 않음

