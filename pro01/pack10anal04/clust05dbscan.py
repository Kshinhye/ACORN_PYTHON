# DBSCAN: 밀도기반 클러스터링
# 데이터가 비선형인 경우 K-means(일반적인 계층적, 비계층정 클러스터링)가 불가.
# 이를 해결하기 위한 방안이다.

import matplotlib.pylab as plt
from matplotlib import style
import numpy as np
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, DBSCAN

# 샘플데이터 생성 (y는 의미없어요)
x,_=make_moons(n_samples=200, noise=0.05, random_state=0) #noise: 퍼짐정도(표준편차)
print(x)

# 군집 수 확인해볼까요
print('실제 군집 id: ', set(_)) #{0, 1} 두개로 분류하네요~ (모양이 흩어져 있지만 두개의 군집으로 분리 되는거죠~)

# 모양을 한 번 볼게요~
# plt.scatter(x[:,0], x[:,1])
# plt.show() # 비선형 , 커브모양이다. 
# 커브 하나를 하나의 클러스터로 하고싶다. 그런데 안된다..... 진짜 볼까요?
# KMeans로 군집분류를 해보자
km=KMeans(n_clusters=2, random_state=0) #n_clusters k값 두개준거임
pred1=km.fit_predict(x)
print('예측 군집 id: ', set(pred1)) #{0, 1}
# 잘나눠진 것 같은데 시각화 한 번 해봅시당
# KMeans 군집결과(함수사용)
def plotFunc(x, pr):
    plt.scatter(x[pr==0,0],x[pr==0,1], s=30, alpha=0.3, c='b', marker='o', label='cluster1')
    plt.scatter(x[pr==1,0],x[pr==1,1], s=30, alpha=0.3,  c='r', marker='s', label='cluster2')
    # centroid(중심점, k-means의 k값)
    plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1], s=60, c='k', marker='+', label='centroid')
    plt.legend()
    plt.show()
    
plotFunc(x, pred1)
# 역시나 내가 원하는 완전한 분리가 안됨
# 요때는 DBSCAN이 직빵이다.

# DBSCAN으로 군집분류
#eps: 두 샘플간의 최대거리. #min_samples: 점에대한 이웃의 샘플 수 #metric: 거리계산 방법 #n_jobs: 내콤퓨타에 CPU 몇개 달려있어?
ds=DBSCAN(eps=0.2, min_samples=5, metric='euclidean')
pred2=ds.fit_predict(x)
plotFunc(x, pred2)

