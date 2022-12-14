'''
[GaussanNB 문제] 
독버섯(poisonous)인지 식용버섯(edible)인지 분류
https://www.kaggle.com/datasets/uciml/mushroom-classification

feature는 중요변수를 찾아 선택, label:class

데이터 변수 설명 : 총 23개 변수가 사용됨.

여기서 종속변수(반응변수)는 class 이고 나머지 22개는 모두 입력변수(설명변수, 예측변수, 독립변수)
'''

import pandas as pd
import numpy as np
from sklearn.model_selection._split import train_test_split
import xgboost as xgb
from xgboost import plot_importance
from sklearn import metrics
from sklearn.preprocessing._encoders import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

df=pd.read_csv("../testdata/mushrooms.csv")
# print(df.info())
# print(df.shape) #(8124, 23)

features=df.iloc[:,1:] #(8124, 22)
features=features.apply(LabelEncoder().fit_transform)
label=df.iloc[:,0].apply(lambda x:1 if x== 'p' else 0)

# print(features.shape) #(8124, 22)
# print(label.shape) #(8124,)

model = xgb.XGBClassifier(booster = 'gbtree', max_depth = 6, n_estimators=500 ).fit(features, label)
model.fit(features,label)

fi = model.feature_importances_
# 중요도를 데이터프레임형식으로 만들어서 보기좋게 하기
f_df=pd.DataFrame(fi, index=model.feature_names_in_).sort_values(by=0, ascending= False)
#gill-color, population, stalk-shape,stalk-color-above-ring,gill-size
print(f_df)

# fig, ax = plt.subplots(figsize = (10, 5))
# # plot_importance(model, ax = ax, importance_type="gain")
# # #gill-color, population, stalk-shape,stalk-color-above-ring,gill-size
# # plot_importance(model, ax = ax, importance_type="cover")
# # #stalk-color-above-ring, gill-color, ring-number, stalk-surface-below-ring, stalk-root
# plot_importance(model, ax = ax, importance_type="weight")
# # spore-print-color, odor, gill-size, cap-color
# plt.xlabel("importance_type=gain") 
plt.show()