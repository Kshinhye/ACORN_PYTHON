# KNN

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

cancer=load_breast_cancer()

x_train, x_test, y_train, y_test=train_test_split(cancer.data,cancer.target, stratify=cancer.target, random_state=66)
#stratify 데이터 나눌 때 쏠림 방지, 값을 target으로 지정하면, 각각의 class 비율을 train / test(validation)에 유지하여, 한 쪽에 쏠려서 분배되는 것을 방지 
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(426, 30) (143, 30) (426,) (143,)

#n_neighbors 값을 조정하면서 성능비교
train_acc=[]
test_acc=[]

neighbors_setting=range(1,15)

for n_neigh in neighbors_setting:
    clf=KNeighborsClassifier(n_neighbors=n_neigh)
    clf.fit(x_train, y_train)
    train_acc.append(clf.score(x_train, y_train))
    test_acc.append(clf.score(x_test, y_test))
    
import numpy as np
print('train 분류 평균 정확도: ', np.mean(train_acc))
print('test 분류 평균 정확도: ', np.mean(test_acc))
# 위 두개의 평균 차이가 크면 오버피팅이다.

# 변화 시각화로 보기
plt.plot(neighbors_setting, train_acc, label='train acc')
plt.plot(neighbors_setting, test_acc, label='test acc')
plt.ylabel('acc')
plt.xlabel('k')
plt.legend()
plt.show()