# XGBoost로 분류모델 작성
# breast_cancer dataset사용
# pip install xgboost
# pip install lightgbm

import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
import xgboost as xgb
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier #xgboost 보다 성능이 우수함, 대용량 처리에 효과적 (데이터가 적을 경우 과적합 발생 우려가 매우 있다.)
from xgboost import plot_importance
import matplotlib.pyplot as plt

dataset=load_breast_cancer()
x_featrue=dataset.data
y_label=dataset.target

cancer_df=pd.DataFrame(data=x_featrue, columns=dataset.feature_names)
print(cancer_df.head(5), cancer_df.shape) #(569, 30)
print(dataset.target_names) #['malignant'양성 'benign'음성]
print(np.sum(y_label == 0)) #212 'malignant'양성
print(np.sum(y_label == 1)) #357 'benign'음성

x_train, x_test, y_train, y_test=train_test_split(x_featrue, y_label, test_size=0.2, random_state=12)
# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)  #(455, 30) (114, 30) (455,) (114,)

# model만들기
#방법 1 
model=xgb.XGBClassifier(booster='gbtree', max_depth=6, n_estimators=500).fit(x_train, y_train) # booster 모델 파라미터
# print(model) # 기본값들 보여준다.
# 방법 1 
# model=LGBMClassifier().fit(x_train, y_train)


pred=model.predict(x_test)
print('예측값: ', pred[:10])
print('실제값: ', y_test[:10])

from sklearn import metrics
acc=metrics.accuracy_score(y_test, pred)
print('분류정확도: ', acc)

print()
cl_rep=metrics.classification_report(y_test, pred)
print('classification_report \n', cl_rep)

# 중요변수 시각화
fig, ax=plt.subplots(figsize=(10,12))
plot_importance(model, ax=ax) # randomforest랑 다르게 plot_importance를 지원한다.
plt.show()