#1 ~ 100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
i=0; hap=0
while i<100:
    i+=3
    if i%3==0 and i%2==1:
        print(i,end=' ')
        hap+=i
print()
print('합은{}'.format(hap))

#2 ~ 5 까지의 구구단 출력
i=2
while i<10:
    j=1
    while j<10:
        j+=1
        print('%d x %d = %d' %(i,j,i*j))
    i+=1
    if i==6:
        break
    
#-1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력
i=1;j=1;hap=0
while j<=99:
    if j%2 == 1:
        if (1+ 4*(i-1)) == j :
            hap-=j
            i+=1
        else:
            hap+=j
    j+=1
print('합은 {}'.format(hap))

print()
i = 1
cnt = 1
tot = 0

while i < 100:
    if cnt % 2 == 0:  # 짝수 위치 숫자 처리
        tot += i
        print(i, end = ' ')
    else:   # 홀수 위치 숫자 처리
        k = i * -1  # 부호 변경
        tot += k
        print(k, end = ' ')

    cnt += 1
    i += 2   # 증가치 2

print('\ntot : ', tot)

#1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
# 2~100 사이의 모든 소수 구하기 2
# 소수란 1과 자신만을 소수로 가지는 수입니다. 
num = 2
count = 0  # 소수의 개수를 세어줄 변수
while num <= 1000:
    i = 2  # 2 ~ num 까지 증가할 변수
    while num % i:  # 나누어질 떄까지 반복
        i += 1      # 1증가
    if i == num:  # 나누어진 수가 자기 자신이면 소수
        count += 1
    num += 1  # 100까지 증가
print(count)