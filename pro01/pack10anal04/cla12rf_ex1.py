'''
[Randomforest 문제1] 
kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)
dataset은 winequality-red.csv 
https://www.kaggle.com/sh6147782/winequalityred?select=winequality-red.csv
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df=pd.read_csv("../testdata/winequality-red.csv")
df_x=df.drop(['quality'],axis=1)
df_y=df.loc[:,'quality']
# print(df_x.shape)
# print(df_x.head(3))
# print(df_x.columns)
# print(df_x.info())
# print(df_x.isnull().sum())
# print(df_y.unique()) #[5 6 7 4 8 3]

train_x, test_x, train_y, test_y = train_test_split(df_x, df_y, test_size=0.3, random_state=13)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape) #(1197, 11) (399, 11) (1197,) (399,)

#model
model = RandomForestClassifier(n_estimators=500, criterion='entropy') # n_estimators: 생성할 트리 개수
model.fit(train_x, train_y)

pred=model.predict(test_x)
print('예측값: ', pred[:5]) #예측값:  [7 6 6 5 7]
print('실제값: ', np.array(test_y[:5])) #실제값:  [7 5 6 5 7]

#정확도
print('acc: ',accuracy_score(test_y, pred)) #acc:  0.696875

#중요변수
# print('특성(변수) 중요도: ', model.feature_importances_) #칼럼에 대한 수치를 제공함

#시각화
import matplotlib.pyplot as plt
def plot_importance(model):
    n_features=df_x.shape[1] #이러면 6이 들어오겠지
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), df_x.columns)
    plt.xlabel('feature_importances')
    plt.ylabel('feature')
    plt.show()

plot_importance(model)