# Support Vector Machine(SVM)
# 분류와 회귀분석을 위해 주로 사용한다. 두 카테고리 중 어느 하나에 속한 데이터의 집합이 주어졌을 때,
# SVM 알고리즘은 주어진 데이터 집합을 바탕으로 하여 새로운 데이터가 어느 카테고리에 속할지 판단하는
# 비확률적 이진 선형분류 모델을 만든다. 만들어진 분류 모델은 데이터가 사상된 공간에서 경계로
# 표현되는데 SVM 알고리즘은 그 중 가장 큰 폭을 가진 경계를 찾는 알고리즘이다.
# SVM은 선형 분류와 더불어 비선형 분류에서도 사용될 수 있다.
# 커널 트릭을 사용함으로써 저차원의 데이터를 고차원으로 변형한 후 분류 및 회귀분석을 할 수도 있다.

# SVM으로 XOR 연산처리
x_data=[
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics

x_df=pd.DataFrame(x_data)
print(x_df)
feature=np.array(x_df.iloc[:,0:2])
label=np.array(x_df.iloc[:,2])
print()
print(feature)
print(label)

model1=LogisticRegression().fit(feature, label)
pred=model1.predict(feature)
print('LogisticRegression 예측값: ',pred)
print('LogisticRegression 정확도: ', metrics.accuracy_score(label, pred))

print('-----------------')
# model2=svm.SVC().fit(feature, label)
model2=svm.SVC(C=1).fit(feature, label) #c:과적합방지 (작으면 작을수록 패널티가 강해진다)
# model2=svm.LinearSVC().fit(feature, label)
pred2=model2.predict(feature)
print('svm 예측값: ',pred2)
print('svm 정확도: ', metrics.accuracy_score(label, pred2))