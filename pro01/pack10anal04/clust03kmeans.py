# 2) 비계층적 군집분석 :
# 군집의 수를 정한 상태에서 설정된 군집의 중심에서 가장 가까운 개체를 하나씩 포함해 나가는 방법으로
# 많은 자료를 빠르고 쉽게 분류할 수 있지만 군집의 수를 미리 정해 줘야 하고 
# 군집을 형성하기 위한 초기값에 따라 군집의 결과가 달라진다는 어려움이 있기 때문에
# 계층적 군집분석을 통해 대략적인 군집의 수를 파악하고 이를 초기 군집 수로 설정한다.
# 방법: k-means clustering

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing.tests.test_data import n_features

# 군집분석이므로 y가 의미가 없다.
# n_features 가 올라가면(차원이 올라가면) 군집분석이 어려워진다.
x,_=make_blobs(n_samples=150, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=0)
# print(x)

# plt.scatter(x[:,0],x[:,1],s=80,c='purple',marker='o', alpha=0.3)
# plt.grid(True)
# plt.show()

# 우리의 목적은 K-means입니다.
# 비계층적 군집분석 중 가장 많이 사용 (데이터의 분포가 비선형인경우 정확도가 떨어진다.)
from sklearn.cluster import KMeans

# 최초의 중심점 설정하는 방법
# init_centroid: 중심점='방법'
init_centroid='k-means++' #default 가능한 거리를 떨어트림
# init_centroid='random'  #붙어있을 수 있다.

kmodel=KMeans(n_clusters=3, init=init_centroid, random_state=0)
pred=kmodel.fit_predict(x) #학습하면서 바로 clustring이 되는 것이다.
print(set(pred)) #0 1 2 세개의 군집으로 분류됨
print(x[pred==0]) #0인 애들만 뽑아보기
print('centroid (중심점의 위치): \n', kmodel.cluster_centers_)

#시각화
plt.scatter(x[pred == 0,0],x[pred == 0,1],s=80,c='pink',marker='o', alpha=0.3, label='cluster1')
plt.scatter(x[pred == 1,0],x[pred == 1,1],s=80,c='blue',marker='s', alpha=0.3, label='cluster2')
plt.scatter(x[pred == 2,0],x[pred == 2,1],s=80,c='green',marker='v', alpha=0.3, label='cluster3')
plt.scatter(kmodel.cluster_centers_[:,0],kmodel.cluster_centers_[:,1],s=100,c='red',marker='+',label='center')
plt.grid(True)
plt.legend()
plt.show()


# k-means 에서 k를 정하는것이 가장 중요한 문제 중 하나
# 방법1: 계층적 군집분석 (dendrogram)으로 k값 유출
# 방법2: 엘보우(elbow) 기법 - 클러스터간 SSE의 차이를 이용
# 방법3: 실루엣 기법사용 - 클러스터 간 실루에 계수값을 수평막대그래프로 표현

# 방법2
# 외울필요없어 복붙했다가 쓰시면 됩니다~
def elbow(x):
    sse=[]
    for i in range(2,11):
        km=KMeans(n_clusters=i, init=init_centroid, random_state=0).fit(x) # 예측할거 아니니까 그냥 fit 쓰셔도 돼요
        sse.append(km.inertia_)
    plt.plot(range(2,11),sse, marker='o')
    plt.xlabel('count of cluster')
    plt.ylabel('SSE')
    plt.show()
    
elbow(x)
# 3에서 뚝 떨어졌잖아 k-means 3으로 쓰라는거야

# 방법3
# '''
# 실루엣(silhouette) 기법
#   클러스터링의 품질을 정량적으로 계산해 주는 방법이다.
#   클러스터의 개수가 최적화되어 있으면 실루엣 계수의 값은 1에 가까운 값이 된다.
#   실루엣 기법은 k-means 클러스터링 기법 이외에 다른 클러스터링에도 적용이 가능하다
# '''
from sklearn.metrics import silhouette_samples
import numpy as np

# 데이터 X와 X를 임의의 클러스터 개수로 계산한 k-means 결과인 y_km을 인자로 받아 각 클러스터에 속하는 데이터의 실루엣 계수값을 수평 막대 그래프로 그려주는 함수를 작성함.
# y_km의 고유값을 멤버로 하는 numpy 배열을 cluster_labels에 저장. y_km의 고유값 개수는 클러스터의 개수와 동일함.

def plotSilhouette(x, pred):
    cluster_labels = np.unique(pred)
    n_clusters = cluster_labels.shape[0]   # 클러스터 개수를 n_clusters에 저장
    sil_val = silhouette_samples(x, pred, metric='euclidean')  # 실루엣 계수를 계산
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []

    for i, c in enumerate(cluster_labels):
        # 각 클러스터에 속하는 데이터들에 대한 실루엣 값을 수평 막대 그래프로 그려주기
        c_sil_value = sil_val[pred == c]
        c_sil_value.sort()
        y_ax_upper += len(c_sil_value)

        plt.barh(range(y_ax_lower, y_ax_upper), c_sil_value, height=1.0, edgecolor='none')
        yticks.append((y_ax_lower + y_ax_upper) / 2)
        y_ax_lower += len(c_sil_value)

    sil_avg = np.mean(sil_val)         # 평균 저장

    plt.axvline(sil_avg, color='red', linestyle='--')  # 계산된 실루엣 계수의 평균값을 빨간 점선으로 표시
    plt.yticks(yticks, cluster_labels + 1)
    plt.ylabel('클러스터')
    plt.xlabel('실루엣 개수')
    plt.show() 

'''
그래프를 보면 클러스터 1~3 에 속하는 데이터들의 실루엣 계수가 0으로 된 값이 아무것도 없으며, 실루엣 계수의 평균이 0.7 보다 크므로 잘 분류된 결과라 볼 수 있다.
'''
X, y = make_blobs(n_samples=150, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=0)
km = KMeans(n_clusters=3, random_state=0) 
y_km = km.fit_predict(X)

plotSilhouette(X, y_km)