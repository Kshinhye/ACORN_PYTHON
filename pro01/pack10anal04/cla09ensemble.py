# Ensemble Learning : 개별적인 여러 모델들을모아 종합적으로 취합 후 최종 분류 결과를 출력
# 앙상블 대표는 랜덤포레스트
# 대표적인 방법:  bagging, voting, boosting
# breast_caencer dataset을 사용
# 이름은 LOgistricRegression (분류 모델), DecisionTree, KNN을 사용하여 voting 분류기를 만들어보자.

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
#LOgistricRegressiond은 Classifier만 가능하지만 DecisionTree, KNN은 Classifier, Regression 다 가능하다
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 시각화도 중요하다 꼭 써줘야하는거에요

cancer=load_breast_cancer()
#sklean은 dataframe으로 가져오지 않느넫 target으로 가져온다.
data_df=pd.DataFrame(cancer.data, columns=cancer.feature_names)
# print(data_df.head(2)) #그냥 한 번 본거야 [2 rows x 30 columns]
# 종양에 영향을주는 독립변수 30게

# train/test split
x_train, x_test, y_train, y_test=train_test_split(cancer.data, cancer.target, random_state=1, test_size=0.2)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(455, 30) (114, 30) (455,) (114,)
print(x_train[:3])
print(y_train[:3],set(y_train)) #{0, 1} 0:양성, 1:음성

#Ensemble model(VotingClassifier) 만들기 : LOgistricRegressiond + DecisionTree + KNN
logi_regression=LogisticRegression()
knn=KNeighborsClassifier(n_neighbors=3)
demodel=DecisionTreeClassifier()

voting_model=VotingClassifier(estimators=[('LR',logi_regression),('KNN',knn),('Decision',demodel)], voting='soft')
#voting: hard(다수결) /soft(확률합산)


classifiers=[logi_regression, knn, demodel]
# 1. 개별 모델의 학습 및 평가
for classifier in classifiers:
    classifier.fit(x_train, y_train)
    pred=classifier.predict(x_test)
    class_name=classifier.__class__.__name__
    print('{0} 정확도: {1:.4f}'.format(class_name, accuracy_score(y_test, pred)))


# 2. 앙상블 모델 학습 및 평가
voting_model.fit(x_train, y_train)
vpred=voting_model.predict(x_test)
vacc=accuracy_score(y_test,vpred)
print('앙상블 모델의 분류 정확도: {0:.4f}'.format(vacc))