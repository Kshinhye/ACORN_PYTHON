# 특성공학 기법 중 차원축소(PCA - 주성분 분석)
# 예) n개의 관측치와 p개의 변수로 구성된 데이터를 상관관계가 최소화된 k개의 변수로 축소된 데이터를 만든다.
# 데이터의 분산을 최대한 보존하는 새로운 축을 찾고 그 축에 데이터를 사영시키는 기법 (직교)
# 목적: 독립변수(x, feature)의 개수를 줄임. 이미지의 차원 축소로 용량을 최소화

# iris dataset으로 PCA를 진행

import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris

iris=load_iris()
n=10
x=iris.data[:n,:2]
print(x, x.shape, type(x))
print(x.T)
"""
# #시각화
# plt.plot(x.T, 'o:')
# plt.xticks(range(2))
# plt.grid()
# plt.legend(['표본{}'.format(i) for i in range(n)])
# plt.show()

# #산점도
# df=pd.DataFrame(x)
# ax=sns.scatterplot(0,1,data=pd.DataFrame(x), marker='s', s=100, color='silver')  #축 / 데이터의 0번쨰, 데이터의 1번째
# for i in range(n): #텍스트도 같이 띄워줄게요
#     ax.text(x[i,0]-0.05, x[i,1]-0.07, '표본{}'.format(i+1))
# plt.xlabel('꽃받침 길이')
# plt.xlabel('꽃받침 너비')
# plt.axis('equal')
# plt.show()

# PCA
from sklearn.decomposition import PCA
pca1=PCA(n_components=1) #n_components: 변환할 차원의 수(2차원에서 1차원으로)
x_low=pca1.fit_transform(x) #1차원 근사데이터의 집합을 만들어 근사값을 찾는다. (비지도학습이라 타겟을 지정하지 않는다.)
print('x_low: \n',x_low, '', x_low.shape)

# inverse_transform() 차원이 축소된 근사 데이터 원복
x2=pca1.inverse_transform(x_low)
print('원복된 결과: \n',x2, x2.shape)
print(x)
print('차원축소:',x_low[0])
print('차원축소 원복/근사행렬값:',x2[0,:])
print('원데이터: ',x[0])

#시각화
df=pd.DataFrame(x)
ax=sns.scatterplot(0,1,data=pd.DataFrame(x), marker='o', s=70)  #축 / 데이터의 0번쨰, 데이터의 1번째
for i in range(n): #텍스트도 같이 띄워줄게요
    d= 0.01 if x[i,1] > x2[i,1] else -0.09 #실제 데이터 표시
    ax.text(x[i,0]-0.02, x[i,1]-d, '표본{}'.format(i+1))
    plt.plot([x[i,0],x2[i,0]], [x[i,1],x2[i,1]], '--') #x축, y축
    
plt.plot(x2[:,0],x2[:,1], 'o-', color='silver', markersize=2)

plt.xlabel('꽃받침 길이')
plt.xlabel('꽃받침 너비')
plt.axis('equal')
plt.show()
"""

# 본격적으로 간다
# iris 4개의 열을 모두 참여시켜서 줄여봅시다.
# 4개의 열을 2개의 열로 줄여볼게요
# 어떻게 축소될지는 알 수 없어
# PCA 에서는 explained_variance_ratio_를 보여주는것이 좋다.
# scaling하면 더 잘 나온다

x=iris.data
pca2=PCA(n_components=2)
x_low2=pca2.fit_transform(x)
print('x_low2(차원축소): \n',x_low2[:3], ' ', x_low2.shape)
#전체 변동성에서 개별 PCA결과(개별Component)별로 차지하는 변동성 비율을 제공
print('변동성비율(중요, 꼭 봐야함): ', pca2.explained_variance_ratio_)
# [0.92461872 0.05306648] 두개 합치면 0.9776852
# 첫번째 데이터가 원본데이터를 92.4%, 두번째 데이터는 5.3% 설명한다(보장한다). 
# 두개의 주성분으로 원본의 데이터를 97.7%나 설명한다고 할 수 있다. (정확도 이런 주책떨지말고 설명하고 있다고 해야한다.)
x4=pca2.inverse_transform(x_low2)
print('최초자료:', x[0])
print('차원축소:', x_low2[0]) #누가누가 붙었는지는 모른다. 짐작할 수 밖에 없다
print('차원복귀:', x4[0]) #PCA를 통해 근사행렬로 변환된다
print()
iris2=pd.DataFrame(x_low2,columns=['f2','f2'])
print(iris2.head(3))
