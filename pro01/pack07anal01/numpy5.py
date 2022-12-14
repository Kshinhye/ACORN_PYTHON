import numpy as np

x=np.array([1,2,3])
y=np.array([4,5,6])
print(x)
print(y)
print()
print('---배열에서 조건 연산 where(조건, 참, 거짓)---')
condionData = np.array([True,False,True])
result=np.where(condionData, x, y) #참일때는 x, 거짓일때는 y
print(result) #[1 5 3]

print()
aa = np.where(x>=2)
print(aa) #인덱스값으로 나옴
print(x[aa])
print(np.where(x>=2,'T',"F"))
print(np.where(x>=2,x+10,x*5))

print('---numpy.concatenate([]) : 배열결합---')
kbs=np.concatenate([x,y])
print(kbs)
print('---split을 이용한 배열분할---')
x1,x2 = np.split(kbs,2)
print(x1)
print(x2)

print()
a=np.arange(1,17).reshape(4,4)
print(a)
x1,x2 = np.hsplit(a,2)
print(x1)
print(x2)
x1,x2 = np.vsplit(a,2)
print(x1)
print(x2)

print('----sampling / 복원,비복원----')
li=np.array([1,2,3,4,5,6,7])
#복원 추출
for _ in range(5):
    print(li[np.random.randint(0,len(li)-1)]) #같은 번호가 중복해서 나온다

#비복원 추출(통계에서는 비복원추출이 기본)
import random
print(random.sample(list(li),k=5))
print(random.sample(range(1,46),k=6)) #오늘의 로또 번호

print()
#choice()
print(list(np.random.choice(range(1,7),6))) #복원
print(list(np.random.choice(range(1,7),6,replace=True))) #복원
print(list(np.random.choice(range(1,7),6,replace=False))) #비복원

print()
#가중치주기
datas='air book cat d e f god'
ar =datas.split(sep=' ')
print(ar)
print(np.random.choice(ar,3,p=[0.1,0.1,0.1,0.1,0.1,0.1,0.4])) #p=[] 각각 확률값주기

















