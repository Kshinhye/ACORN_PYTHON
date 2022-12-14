# Clustering(군집화) : 사전정보(label)가 없는 자료에 대해 컴퓨터가 스스로 패턴을 찾아 여러개의 군집을 형성함
# 비지도학습

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

np.random.seed(123)
var=['x','y']
labels=['점0','점1','점2','점3','점4']
x=np.random.random_sample([5,2])*10 #5행2열
# print(x)
df=pd.DataFrame(x, columns=var, index=labels)
print(df)

# plt.scatter(x[:,0],x[:,1], s=100, c='red', marker='o',alpha=0.2)
# plt.grid(True)
# plt.show()

# 데이터간 거리보기
# 유클리디안 거리 함수
from scipy.spatial.distance import pdist, squareform
dist_vec=pdist(df, metric='euclidean') #데이터(배열)에 대해 각 요소간 거리를 계산한 후 1차원 배열로 반환해준다
print(dist_vec)

# 보기편하게 squareform에 넣어볼게요
row_dist=pd.DataFrame(squareform(dist_vec), columns=labels, index=labels)
print(row_dist)

# 우리의 찐 목적은 거리를 보는게 아니라 군집화 하려는거야
# 계층적 군집분석(비지도학습)
from scipy.cluster.hierarchy import linkage
row_clusters=linkage(dist_vec, method='complete') #method(연결방법) complete(완전연결법) (방법의 차이일 뿐 결과는 거의 비슷하다)

df=pd.DataFrame(row_clusters, columns=['군집id1', '군집id2','거리','멤버수'])
print(df)

# dendrogram으로 row_clusters를 시각화
from scipy.cluster.hierarchy import dendrogram
low_dend=dendrogram(row_clusters,labels=labels)
plt.ylabel('유클리드 거리')
plt.show()