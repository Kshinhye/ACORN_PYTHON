# iris dataset으로 지도학습(KNN) / 비지도학습(K-Means) 정리

from sklearn.datasets import load_iris

iris_dataset=load_iris()
print('iris_dataset["data"] \n', iris_dataset['data'][:3])
print('iris_dataset["feature_names"] \n',iris_dataset['feature_names'])

#train/test splite
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y=train_test_split(iris_dataset['data'],iris_dataset['target'], random_state=42)

#===============================================================================
# 지도학습 (KNN)
#===============================================================================
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics._classification import accuracy_score

knnModel=KNeighborsClassifier(n_neighbors=5)
knnModel.fit(train_x, train_y) #feature, label 둘 다 사용

predict_label=knnModel.predict(test_x)
print('predict_label \n',predict_label)
print('acc: ',accuracy_score(test_y, predict_label))

#===============================================================================
# 비지도 학습(K-means)
#===============================================================================
from sklearn.cluster import KMeans
kmeansModel=KMeans(n_clusters=3, init='k-means++', random_state=0)
kmeansModel.fit(train_x) #feature만 준다.

print('kmeansModel.labels_',kmeansModel.labels_)
print('o cluster',train_y[kmeansModel.labels_==0])
print('1 cluster',train_y[kmeansModel.labels_==1])
print('2 cluster',train_y[kmeansModel.labels_==2])

pred_cluster=kmeansModel.predict(test_x)
print('pred_cluster: \n', pred_cluster)

# 성능을 좀 볼까요
import numpy as np
np_arr=np.array(pred_cluster)

#array to list로 변형
pred_label=np_arr.tolist()
print('test acc: {:.2f}'.format(np.mean(pred_label == test_y)))