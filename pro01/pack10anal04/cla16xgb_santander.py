# 산탄데르 은행 고객 만족여부 분류 모델
# label: TARGET: 0(만족), 1(불만족)

import numpy as mp
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("train_san.csv", encoding='latin-1')
print(df.head(2))
print(df.shape) #(76020, 371)
print(df.info())
#만족불만족 비율을 볼 수 있겠다.
print()
print(df['TARGET'].value_counts()) #0 : 73012 #1 : 3008
# print((df['TARGET']==0).sum()) #만족: 73012
# print((df['TARGET']==1).sum()) #불만족: 3008

unsatifired_cnt=df[df['TARGET'] == 1].TARGET.count()
total_cnt=df.TARGET.count()
print('불만족비율은 {0:.2f} '.format(unsatifired_cnt/total_cnt)) #0.04 
# pd.set_option('display.max_columns',None)
# print(df.describe()) #var3변수에 이상치 의심
df['var3'].replace(-999999,2,inplace=True)
# print(df.describe())
df.drop('ID',axis=1, inplace=True)

x_features=df.iloc[:,:-1] #TARGET을 뺀 나머지
y_label=df.iloc[:,-1]
# print(x_features.shape, y_label.shape) #(76020, 369) #(76020,)

#train, val, test 으로 데이터셋 분리
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x_features, y_label, test_size=0.2, random_state=12)
# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(60816, 369) (15204, 369) (60816,) (15204,)

train_cnt=y_train.count()
test_cnt=y_test.count()
print('trian 데이터 레이블 분포 비율 : \n', y_train.value_counts()/train_cnt) #0:0.9602 1:0.0397
print('label 데이타 레이블 분포 비율 : \n', y_test.value_counts()/test_cnt) #0: 0.9611 1:0.0388

# model을 만들어서 해봅시다.
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score

xgb_clf=XGBClassifier(n_estimators=5, random_state=12)
#n_estimator : 의사결정나무 갯수  #n_estimators=5 데이터가 많아서 트리갯수 조금 줌 사실 더 많이 줘야됨
xgb_clf.fit(x_train, y_train, eval_metric='auc', early_stopping_rounds=2,
            eval_set=[(x_train, y_train),(x_test, y_test)]) #eval_metrix(평가지표값)='auc'
# cost가 떨어지면( 0에 가까이 갈수록) auc(정확도)는 올라간다.

xgb_roc_curve=roc_auc_score(y_test, xgb_clf.predict_proba(x_test)[:,1])
print('ROC AUC: {0:.4f}'.format(xgb_roc_curve)) #1에 가까이 갈수록 좋다.
pred=xgb_clf.predict(x_test)
print('예측값: ', pred[:5])
print('실제값: ',y_test[:5].values)

from sklearn import metrics
acc=metrics.accuracy_score(y_test, pred)
print('분류정확도: ', acc) #0.9611 양호

# GridSearchCV로 최적의 파라미터를 구한 후 모델 작성
# 중요변수를 알아내 독립변수(feature)를 줄이는 작업
# 또는 주성분 분석을 통해 성격이 유사한 변수들에 대해 차원축소를 통해 독립변수(feature)를 줄이는 작업 가능 등이 있다.