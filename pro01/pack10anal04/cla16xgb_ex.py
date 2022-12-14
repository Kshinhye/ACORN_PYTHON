'''
[XGBoost 문제] 
kaggle.com이 제공하는 'glass datasets'
유리 식별 데이터베이스로 여러 가지 특징들에 의해 7 가지의 label(Type)로 분리된다.
RI    Na    Mg    Al    Si    K    Ca    Ba    Fe     Type
glass.csv 파일을 읽어 분류 작업을 수행하시오.
'''

import numpy as np
import pandas as pd
import xgboost as xgb
from xgboost import plot_importance
from xgboost.sklearn import XGBClassifier
import matplotlib.pyplot as plt
from sklearn.metrics._classification import accuracy_score

df=pd.read_csv("../testdata/glass.csv")
print(df.head(2),df.shape) #(214, 10)
print(df.info())

x_features=df.iloc[:,:-1]
y_label=df.iloc[:,-1]
# 범주형 데이터를 쉽게 수치형 데이터로 형변환 방법1
y_labels=y_label.astype('category').cat.codes
print(y_labels.unique()) #[1 2 3 5 6 7] -> [0 1 2 3 4 5]
# 범주형 데이터를 쉽게 수치형 데이터로 형변환 방법2
# from sklearn.preprocessing import LabelEncoder
# y_labels = LabelEncoder().fit_transform(y_label)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x_features, y_labels, test_size=0.3, random_state=12)

model = xgb.XGBClassifier(booster='gbtree', n_estimators=500, random_state=12)
model.fit(x_train,y_train)
print(model.feature_importances_)

pred=model.predict(x_test)
print('분류 정확도: ', accuracy_score(y_test, pred))
print(model.feature_importances_)

f_df=pd.DataFrame({'f_name':model.feature_names_in_,'f_im':model.feature_importances_})
print(f_df.sort_values(by='f_im', ascending=True))



# 중요변수 시각화
fig, ax=plt.subplots(figsize=(10,5))
plot_importance(model, ax=ax, color=['red', 'green'])

# from xgboost import plot_importance
# plot_importance(model)
plt.show()