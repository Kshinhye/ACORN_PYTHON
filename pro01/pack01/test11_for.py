#for + range
#range: 수열을 생성해준느 함수


#list 타입으로 반환 #1씩증가(1일 때는 생략 가능)
print(list(range(1,6,1))) #[1, 2, 3, 4, 5]
print(set(range(1,6))) #{1, 2, 3, 4, 5}
print(tuple(range(1,6))) #(1, 2, 3, 4, 5)
print(list(range(1,11,2))) #[1, 3, 5, 7, 9]
print(list(range(6))) #[0, 1, 2, 3, 4, 5
print(list(range(0,6,1))) #[0, 1, 2, 3, 4, 5
print(list(range(-10,-100,-20))) #[-10, -30, -50, -70, -90]
print()
for i in range(6):
    print(i,end=' ') #0 1 2 3 4 5 
print()

for _ in range(6):
    print('안녕',end=' ') #안녕 안녕 안녕 안녕 안녕 안녕 
    #pass # 블럭 내에서 아무것도 수행할게 없을 때
print()

for i in range(1,10):
    print('{0}*{1}={2}'.format(2,i,2*i),end=' ')
print()

print()
tot=0
for i in range(1,11):
    tot+=i
print('합은 '+str(tot))
print('합은',sum(range(1,11)))

# 문1)2~9단까지 출력
for n in range(2,10):
    for i in range(0,10):
        print('{}*{}={}'.format(n,i,n*i))
        
# 문2) 1~100 사이의 3의 배수이면서 5의 배수의 합 출력
tot=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        tot+=i
print()
print('합은{}'.format(tot))

# 문3) 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 두 수 출력
#출력 예) 1 3
#       2 2 ...
for i in range(1,7):
    for j in range(1,7):
        if (i+j)%4 ==0:
            print(i,j)
            
print()
#n-gram : 문자열에서
text='hello'

for i in range(len(text)-1):
    print(text[i:i + 3])