import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler #정규화 지원
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# 공부시간에 따른 시험점수 예측모델작성
df=pd.DataFrame({'study_time':[3,4,5,8,10,5,8,6,3,6,10,9,7,0,1,2],'score':[76,74,74,89,95,84,82,70,60,88,80,50,85,50,60,79]})
print(df)

#train/test split : dataset분리 (목적: Overfitting(과적합)을 방지)
#test_size 6대4로 분리 shuffle=T 기본, random_state=1 randomseed랑 같은 역할
train,test=train_test_split(df,test_size=0.4,shuffle=True, random_state=12)
x_train=train[['study_time']] #가공 조금 해볼게요
y_train=train['score'] #가공 조금 해볼게요
x_test=test[['study_time']] #가공 조금 해볼게요
y_test=test['score'] #가공 조금 해볼게요
print(x_train)
print(y_train)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
#(9, 1) (7, 1) (9,) (7,)

print()
#모델을 만들어볼게요
model=LinearRegression()
model.fit(x_train, y_train)

y_pred=model.predict(x_test)
print('예측값:\n', y_pred)
print('실제값:\n', y_test.values)

#결정계수 구하기
print('결정계수로 모델 성능확인')
print('결정계수:', r2_score(y_test,y_pred)) #특징: testdata를 사용

#참고 : 결정계수는 표본 데이터가 많을수록 그 수치 또한 증가한다.
def linearFunc(df,test_size):
    train,test=train_test_split(df,test_size=test_size,shuffle=True, random_state=12)
    x_train=train[['study_time']]
    y_train=train['score'] 
    x_test=test[['study_time']] 
    y_test=test['score'] 
    # print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
    # (14, 1) (2, 1) (14,) (2,)
    # (12, 1) (4, 1) (12,) (4,)
    # (11, 1) (5, 1) (11,) (5,)
    # (9, 1) (7, 1) (9,) (7,)
    # (8, 1) (8, 1) (8,) (8,)
    model=LinearRegression().fit(x_train,y_train)
    y_pred=model.predict(x_test)
    print('결정계수:', r2_score(y_test,y_pred).round(2))
    print('test data 비율: 전체 데이터의 {}%'.format(i*100))
    
    #시각화
    sns.scatterplot(x=df['study_time'],y=df['score'],color='green')
    sns.scatterplot(x=test['study_time'],y=y_test,color='red')
    sns.lineplot(x=x_test['study_time'],y=y_pred,color='blue')
    plt.show()
    #r2(결정계수값)은 데이터의 수에 따라 적절한 값을 찾아가게된다
    
    
test_size=[0.1,0.2,0.3,0.4,0.5] #test_size 비율값 다르게 줘볼게요
for i in test_size:
    linearFunc(df, i)