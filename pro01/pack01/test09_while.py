#반복문 continue, break
a=0
while a<10:
    a+=1
    if a ==3:continue
    if a ==5:break
    print(a)
#while문이 강제종료됐는지 정상종료 됐는지 확인 가능(옵션)
else:
    print('while문 정상 수행')
    
print('while 수행 후 %d'%a)

print()
#난수 발생
import random
#random.seed(1) #개발 과정 중 랜덤한 값을 원하기는 하지만 우선 고정할 때 사용
num=random.randint(1, 10)
'''
#print(num)
while True: #무한 루프에 빠트리기(true)
    print('1~10 사이의 컴이 가진 예상 숫자 입력')
    guess=int(input())
    if guess==num: #guess가 컴퓨터가 가진 num과 같다면
        print(' *성공* '*5)
        break #빠져나간다
    elif guess<num:
        print('더 큰 수 입력')
    elif guess>num:
        print('더 작은 수 입력')
'''        

#의사 난수(pseudo random)
friend=['tom','john','oscar']
print(friend)
print(random.choice(friend)) #하나만 랜덤하게 선택
print(random.sample(friend,2)) #개수를 정해서 일부만 표본을 뽑는것
random.shuffle(friend) #순서 랜덤
print(friend)














