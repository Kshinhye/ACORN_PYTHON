#배열연산

import numpy as np
from scipy.constants.constants import pt

# x=np.array([[1,2],[3,4]]) #2 by 2
# print(x, x.dtype)  #int32 : integer type

x=np.array([[1,2],[3,4]], dtype=np.float64)
print(x, x.dtype)
#reshape(행,렬) :구조 바꾸기
y=np.arange(5,9).reshape(2,2)
#astype : 형변환
y=y.astype(np.float64)
print(y,y.dtype)


print('---더하기(sum)----')
print(x+y) #그냥 더하기
print(np.add(x,y)) #함수로 더하기
#떠오르면 안되는데 떠올려버렸다. -영권쌤-
#python 과 numpy 연산함수 속도 차이
imsi=np.random.rand(1000000)
print(imsi)
print(sum(imsi)) #파이썬의 함수 #느리고
print(np.sum(imsi)) #numpy의 함수 #빠르다
print('---빼기(subtract)---')
print(x-y)
print(np.subtract(x,y))
print('---나누기(divide)---')
print(x-y)
print(np.divide(x,y))
print('---곱하기(multiply)---')
print(x-y)
print(np.multiply(x,y))


#벡터 간 내적 연산 (행렬곱) : dot (R에서는 %*%을 사용했다)
print('---dot():내적 연산 함수---')
print('--1차원 * 1차원 = 스칼라--')
v=np.array([9,10])
w=np.array([11,12])
print(v*w)  #[ 99 120]
print(v.dot(w)) #v[0]*w[0] + v[1]*w[1]  #219
print(np.dot(v,w)) #속도는 얘가 빠르다 #219

print('--2차원 * 1차원 = 1차원--')
print(x) #2차원
print(v) #1차원
print(np.dot(x,v)) #[29. 67.]
#x[0][0]*v[0] + x[0][1]*v[1] =29
#x[1,0]*v[0] + x[1,1]*v[1] =67

print('--2차원 * 2차원 = 2차원--')
print(x)
print(y)
print(np.dot(x,y)) # [[19. 22.]    [43. 50.]] 2by2
#x[0,0]*y[0,0] + x[0,1]*y[1,0] = 19

print('--누적합, 누적곱-')
print(np.sum(x))
print(np.mean(x))
#np.cunsum() : 누적합 
print(np.cumsum(x)) #[ 1.  3.  6. 10.]
#np.cumprod() : 누적곱 
print(np.cumprod(x)) #[ 1.  2.  6. 24.]

print('--중복배제, 교집합, 합집합--')
names1=np.array(['tom','james','tom','oscar'])
names2=np.array(['tom','page','john'])
#np.unique() : 중복배제
print(np.unique(names1))  #['james' 'oscar' 'tom']
#np.intersect1d(): 교집합
# assume_unique:중복허용
print(np.intersect1d(names1,names2)) #['tom']
print(np.intersect1d(names1,names2 ,assume_unique=True)) #['tom' 'tom']
#np.union1d():  #합집합
print(np.union1d(names1,names2)) #['james' 'john' 'oscar' 'page' 'tom']

print()
print('--Transpose전치--')
print(x)
print(x.T)
print(x.transpose())
print(x.swapaxes(0,1))

print()
print('--Broadcast 연산--')
#크기가 다른 배열간의 연산을하면 작은 배열이 큰 배열의 크기를 자동으로 따라감
x=np.arange(1,10).reshape(3,3) #reshape(3,4) -> err
print(x)
y=np.array([1,0,1]) #x만큼 y를 늘려준다.
print(y)
print(x+y)

print()
print('--파일 저장하고 불러오기--')
print(x)
np.savetxt('my.txt',x)
imsi=np.loadtxt('my.txt')
print(imsi)
imsi2=np.loadtxt('my2.txt',delimiter=',') #delimiter 구분자 주기
print(imsi2)






