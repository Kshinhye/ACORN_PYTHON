#배열에 행/열 추가

import numpy as np

print('---행을 열로 변환----')
#배열만들기: numpy.eye()
aa=np.eye(3) #3 by 3 2차원 배열 만들어짐
print(aa,aa.shape)

#열추가 : numpy.c_[] 
bb=np.c_[aa,aa[2]] #aa배열에 aa의 3열과 동일한 열 추가 #aa[2] array타입
print(bb,bb.shape)

#행추가 : numpy.r_[]
cc=np.r_[aa,[aa[2]]] #[aa[2]] : list타입
print(cc,cc.shape)

a=np.array([1,2,3]) #파이썬의 list array로 형변환
print('a=','\n',a)
print(np.c_[a]) #행을 열로 변환 #2차원 
print(a.reshape(3,1)) #행을 열로 변환 #2차원

print('---1차원에서의 append, insert, delete---')
print(a) #[1 2 3]

#append 뒤에 갖다 붙이는거
#axis =0(열방향으로 채우기 기준은 행)/1차원에서는 안써도 됨  #지금은1차원이라서 axis =1 하면 err
b=np.append(a,[4,5], axis=0)
print(b) #[1 2 3 4 5]
#insert 넣는거
c=np.insert(a,1,[6,7],axis=0) #[1 2 3], 1번째 자리에 [6,7]을 넣겠다
print(c) #[1 6 7 2 3]
#delete 지우기
d=np.delete(a,[1,2])#[1 2 3] 에서 1,2번째를 지우겠다.
print(d) #[1 3]

print('---2차원에서의 append, insert, delete---')
print('--방향을 주지않으면 차원이 축소된다--')
#axis=0 / 열방향 행기준
#axis=1 / 행방향 열기준
aa=np.arange(1,10).reshape(3,3)
print(aa)
print('--numpy.insert--')
#numpy.insert
print(np.insert(aa,1,99)) #aa배열을 차원 축소 후 1번째 지점에 99을 추가
print(np.insert(aa,1,99, axis=0))
print(np.insert(aa,1,99, axis=1))
print('--numpy.append--')
#append
print(aa)
bb=np.arange(10,19).reshape(3,3)
print(bb)
cc=np.append(aa,bb,axis=0)
print(cc)
cc=np.append(aa,bb,axis=1)
print(cc)
print('--numpy.delete--')
print(np.delete(aa,1)) #1번째 요소 '2' 삭제
print(np.delete(aa,1,axis=0)) #1행 삭제
print(np.delete(aa,1,axis=1)) #1열 삭제















