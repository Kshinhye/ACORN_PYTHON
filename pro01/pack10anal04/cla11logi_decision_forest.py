# titanic dataset으로 LogisticRegression, DecisionTree 분류 모델 비교

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from nltk.classify.decisiontree import DecisionTreeClassifier

df = pd.read_csv("../testdata/titanic_data.csv")
df.drop(columns=['PassengerId','Name','Ticket'], inplace=True)
# print(df.describe())
# print(df.info())
# print(df.isnull().sum()) #Age 177 / Cabin(방호수) 687 / Embarked(탑승지) 2

# NULL 처리 : 평균, 0, 'N(임의의문자)' 등으로 변경
df['Age'].fillna(df.Age.mean(), inplace=True)
df['Cabin'].fillna('N', inplace=True)
df['Embarked'].fillna('N', inplace=True)
# print(df.head(2))
# print(df.isnull().sum())  #0 #0 #0

# ## 데이터 가공이 중요한겁니다.
# #Dtype: object/Sex, Cabin,Embarked 값들의 상태를 분류해서 보기
# print('Sex:',df['Sex'].value_counts()) # male:577 female:314
# print('Cabin:',df['Cabin'].value_counts())
# #Cabin 값들이 너무 복잡함으로 간략하게 정리 (원본에 영향을 주면 안됨) : 앞글자만 사용하기로 하자
# print('Embarked:',df['Embarked'].value_counts())

# Cabin데이터가공 해볼까요
df['Cabin'] = df['Cabin'].str[:1]
print(df.head(5))

print()
#성별이 생존확률에 어떤 영향을 주었나?
print(df.groupby(['Sex','Survived'])['Survived'].count())
print(233/(81+233))  #여성 생존률 74.2%
print(109/(468+109)) #남성 생존률 18.9%

#성별 생존 확률에 대한 시각화 한 번 해볼까요
# sns.barplot(x='Sex',y='Survived', data=df, ci=95) #ci:신뢰구간 95%
# plt.xlabel('Sex')
# plt.ylabel('Survived')
# plt.show()
#나이별, Pclass가 생존확률에 어떤 영향을 주었나?...

print('----------------')
#문자열(object) 데이터(범주형 데이터)를 숫자형으로 변환
from sklearn import preprocessing #전처리 너~무나 중요하다.

# print(set(df['Cabin']))

def labelFunc(datas):
    cols=['Cabin','Sex','Embarked']
    for c in cols:
        lab = preprocessing.LabelEncoder()
        lab = lab.fit(datas[c])
        datas[c] = lab.transform(datas[c])
    return datas

df = labelFunc(df)

print(df.head(3))
print(df['Cabin'].unique()) # [ 7 2 4 6 3 0 1 5 8]
print(df['Sex'].unique())  # [1 0]
print(df['Embarked'].unique()) # [3 0 2 1]

#일단 쪼개놓고 가볼까요.
print()
feature_df = df.drop(['Survived'], axis='columns')  #axis='columns'
print(feature_df.head(2))
label_df = df['Survived']
print(label_df.head(2))

x_train, x_test, y_train, y_test = train_test_split(feature_df, label_df, test_size=0.2, random_state=1)
print(x_train.shape,x_test.shape,y_train.shape, y_test.shape) #(712, 8) (179, 8) (712,) (179,) feature(특성)은 여덟게 label은 하나

print('---------우리가 하려는게 요거야------------')
#LogisticRegression, DecisionTree,RandomForest 분류 모델 비교
logmodel = LogisticRegression(solver='lbfgs', max_iter=500).fit(x_train, y_train)
# solver='lbfgs' 알고리즘의 이름을 줄여쓴것. Limited-memory Broyden–Fletcher–Goldfarb–Shanno
# max_iter 반복횟수
decmodel = DecisionTreeClassifier().fit(x_train, y_train)
rfmodel = RandomForestClassifier().fit(x_train, y_train)


logpredict = logmodel.predict(x_test)
print('LogisticRegression acc: {0:.5f}'.format(accuracy_score(y_test, logpredict)))
decpredict = decmodel.predict(x_test)
print('DecisionTree acc: {0:.5f}'.format(accuracy_score(y_test, decpredict)))
rfpredict = rfmodel.predict(x_test)
print('RandomForest acc: {0:.5f}'.format(accuracy_score(y_test, rfpredict)))