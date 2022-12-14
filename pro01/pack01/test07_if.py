#조건 판단문 if

#단순 if
var=10
if var>=3:
    print('크구나')
    print('참일 때')
    
print('end1')

#else
if var>=3:
    # print('크구나')
    # print('참일 때')
    pass
else:
    print('거짓 일 때')
    
print('end1')

#조건안에 조건
print()
money=1000
age=23

if money>=500:
    item='사과'
    if age<=30:
        msg='청춘이다'
    else:
        msg='오올드하다'
else:
    item='포도'
    if age>=30:
        msg='성인이다'
    else:
        msg='애다'
        
print(item,msg)

print()
jumsu=95
if jumsu>=90:
    print('우수')
else:
    if jumsu>=70:
        print('보통')
    else:
        print('저조')
        
print()
if jumsu>=90:
    print('우수')
elif jumsu>=70:
    print('보통')
else:
    print('저조')

print()
print(int('5')+5)
print(str(5)+'5')

#jum = int(input('점수입력:'))
jum=80
# print(jum, type(jum))
#if jum>=90 and jum<=100: 를 짧게 쓰면
if 90<=jum<=100:
    grade='우수함'
elif 70<=jum<90:
    grade='보통임'
else:
    grade='저조함'
    
print(grade)

#긍정
print()
names=['홍길동','신기해','이기자']
if '고길동' in names:
    print('친구 이름')
else:
    print('누구니?')
    
#부정 (프로그램을 짤 때는 속도가 느려져서 부정보단 긍정조건 권장)
print()
names=['홍길동','신기해','이기자']
if '고길동' not in names:
    print('친구 이름')
else:
    print('누구니?')

#한줄짜리 조건문 (참 if 거짓)
print()
a='kbs'
b=9 if a=='kbs' else 11
print(b)

a=11
b='mbc' if a==9 else 'kbs'
print(b)

print()
a=3
if a<5:
    print(0)
elif a<10:
    print(1)
else:
    print(2)
#위 표현을 다중 if 줄로 표현(이렇게는 잘 안해요)
print(0 if a<5 else 1 if a<10 else 2)

print(a*2 if a>5 else a+2)
#조건:[a>5] False면 0번째꺼(a+2)가 출력
print((a+2,a*2)[a>5])















