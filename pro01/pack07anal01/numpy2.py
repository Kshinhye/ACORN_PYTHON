#numpy
import numpy as np

#list: 잡것들 다 들어올 수 잇다.
ss = ['tom','james','oscar',1] #<class 'list'> list타입의 클래스
print(ss,type(ss))

#array: 요소들의 타입이 일치해야한다.
ss2=np.array(ss) #ss를 형변환 시킴 <class 'numpy.ndarray'> numpy.ndarray 타입의 클래스 numpy모듈이 지원함
print(ss2,type(ss2))

print('-----메모리비교 (list vs numpy)-----')
print('----list 구조----')
li = list(range(1,11))
print(li[0],li[1],id(li[0]),id(li[1])) 
#별도의 객체 주소를 기억하고 있다.
#id(li[0]) 2654962542896  /  id(li[1]) 2654962542928 
print(li*10) #10번씩 출력

print('----numpy 구조----')
num_arr = np.array(li)
print(num_arr[0],num_arr[1],id(num_arr[0]),id(num_arr[1]))
#배열들의 요소들이 같은 주소를 기억하고 있다.
#id(num_arr[0]) 2407209535760  /  id(num_arr[1]) 2407209535760
print(num_arr*10)
print(type(num_arr), num_arr.dtype, num_arr.shape, num_arr.ndim, num_arr.size)
# 데이터 타입: int32(integer type) /배열크기: 몇행몇열(10,) /1차원 /10개의 요소

print('----2차원----')

b= np.array([[1,2,3],[4,5,6]])
print(b.ndim) #2차원
print(b[0],b[0][0],b[[0]]) #0행 #0행의0열 #0행의0열의 2차원

#zeros((행, 렬)) : 0으로 배열 채우기
c=np.zeros((2,2))
print(c)

#ones((행,렬)) : 1로 배열 채우기
d=np.ones((2,2))
print(d)

#full((행,렬), fill_value=채울 값 지정)
e=np.full((2,2),fill_value=7)
print(e)

#eye() 단위행렬
f=np.eye(3)
print(f)

print('----균등분포, 정규분포 차이----')
np.random.seed(0) #난수 붙잡기
#rand method는 0 이상 1 미만의 랜덤한 실수를 생성
#print(np.random.rand(5))  #균등 분포를 따르는 난수
print(np.mean(np.random.rand(50)))
#print(np.random.randn(5)) #정규 분포
print(np.mean(np.random.randn(50)))

print('----arange함수를 사용하면 수열을 구할 수 있다.---')
print(list(range(1,10)))
print(np.arange(10))

print('----슬라이싱 조금 더 볼까?----')
a=np.array([1,2,3,4,5])
print(a)
print(a[1:4]) #[2 3 4]
print(a[1:4:2])  #[2 4] 2는 증가치
print(a[1:]) #[2 3 4 5]
print(a[-4]) #2  R에서는 여집합이었다. 헷갈리지말기!


b=a #주소치환 : b가 바뀌면 a도 바뀐다.
print(a) #[1 2 3 4 5]
print(b) #[1 2 3 4 5]
b[0]=33
print(a) #[33  2  3  4  5]
print(b) #[33  2  3  4  5]

c=np.copy(a) #a와 똑같은 c객체가 새로 만들어짐 : c가 바껴도 a는 바뀌지 않음
c[0]=77
print(a) #[33  2  3  4  5]
print(c) #[77  2  3  4  5]

print('----2차원 보여줄게(리턴타입 잘 확인)----')
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print(a[:])
print(a[0],a[0][0],a[[0]]) #a의 0행, a의 0행 0열, 0행만 보여주는데 2차원으로 보여줌
print(a[[0][0]],a[0,0])  #a[0] == a[[0][0]],  a[0][0]==a[0,0]
print(a[1,0:2])

print('----서브배열을 수정하면 원본데이터도 바뀐다----')
print(a)
b=a[:2,1:3] #2행과 1열2열 *주의:0부터 시작함!!
print(b)
b[0,0]=88 #b의 0행0열에 88을 준다.
print(b)
print(a) #a의 0행0열도 바꼈다.

print('----슬라이싱만으로도 차원을  축소/확대 할 수 있다----')
a=np.array([[1,2,3],[4,5,6],[7,8,9]]) #3 by 3 행렬
print(a)
r1=a[1,:] #1차원
r2=a[1:2,] #2차원(차원유지)
print(r1,r1.shape)
print(r2,r2.shape)

print('----이번엔 열을 볼까요----')
c1=a[:,1] #전체행, 1열 슬라이싱
c2=a[:,1:2] #2차원(차원유지)
print(c1,c1.shape)
print(c2,c2.shape)

print('----boolean----')
bool_idx=(a>5)
print(bool_idx) # True/False 반환
print(a[bool_idx]) #[6 7 8 9]
print(a[a>5]) #[6 7 8 9]