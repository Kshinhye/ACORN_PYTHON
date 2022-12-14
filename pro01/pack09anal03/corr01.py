# 워밍없이라고 생각하시고~
# 공분산 / 상관계수(공분산을 표준화한 값) 요 얘기를 한 번 해보도록 할~게~욤~

import numpy as np
import matplotlib.pyplot as plt

# 공분산 예
print(np.cov(np.arange(1,6),np.arange(2,7))) # 2.5 : 아, 이 둘은 양의관계가 있구나
print(np.cov(np.arange(10,60,10),np.arange(20,70,10))) # 250 : 아, 이 둘은 양의관계가 있구나
print(np.cov(np.arange(1,6),(3,3,3,3,3))) #0 : 서로 관계가 없다.
print(np.cov(np.arange(1,6),np.arange(6,1,-1))) # -2.5 : 아, 이 둘은 음의관계가 있구나
#2.5 250 -2.5 얘네들 표준화작업이 필요하다 -> 상관계수를 구한다.

print()
x=[8,3,6,6,9,4,3,9,3,4]
print('x의 평균', np.mean(x)) #5.5
print('x의 분산', np.var(x)) #5.45

#y=[6,2,4,6,9,5,1,8,4,5]
y=[600,200,400,600,900,500,100,800,400,500] #얘로 바꿔서 해봐도 상관계수는 똑같다(산점도 패턴도 똑같다)
print('y의 평균', np.mean(y)) #5.0
print('y의 분산', np.var(y)) #5.4

plt.scatter(x,y)
plt.show()

print('x,y 공분산: ',np.cov(x,y)[0,1])
print('x,y 상관계수: ',np.corrcoef(x,y)[0,1]) #피어쓴상관계수 #0.86636

#그냥 참고로 하는 얘기다
from scipy import stats
print(stats.pearsonr(x,y)) #파이쓴 상관계수(등간척도, 연속형일 때)
print(stats.spearmanr(x,y)) #스피어만 상관계수 (서열척도일때는 스피어만)

#★☆★☆주의: 공분산이나 상관계수는 선형데이터인 경우에 활용★☆★☆
#비선형일때 사용하면 안된다 (아래와 같이 제대로 판별이 안된다)
m=[-3,-2,-1,0,1,2,3]
n=[9,4,1,0,1,4,9]
plt.scatter(m,n)
plt.show()
print('m,n의 공분산: ',np.cov(m,n)[0,1]) #0.0
print('m,n의 공분산: ',np.corrcoef(m,n)[0,1]) #0.0