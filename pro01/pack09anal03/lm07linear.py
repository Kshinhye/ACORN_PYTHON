# 선형회귀 분석모델 작성 시 LinearRegression을 사용 : summary()함수 지원X (summary는 ols지원)
# 선형회귀 분석모델을 평가할 수 있는 score 알아보기 r2_score, explained_variance_score, mean_squared_error
# 특히나 , mean_squared_error는 딥러닝/텐서플로에서 나온다

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler #정규화 지원
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#데이터는 일부러 편차가 있는 표본데이터를 만들어볼까요
sample_size=100
np.random.seed(1)

print('--------두 변수의 표준편차가 같을 때: 분산이 작음-----------')
x=np.random.normal(0,10, sample_size) #정규분포를 따릅니다. 평균은0, 분산은10 100개의 샘플을 뽑는다.
y=np.random.normal(0,10, sample_size)+x*30
print(x[:5])
print(y[:5])
print('상관계수: ',np.corrcoef(x,y)) #0.99939357 현실세계에서는 볼 수 없는 값
#독립변수 x에대한 정규화를 한 번 진행해보께요옴
scaler=MinMaxScaler()
x_scaled=scaler.fit_transform(x.reshape(-1, 1)) #.inverse_transform 원상복구 #sklearn 에서 제공되는 애들은 매트릭스
print(x_scaled[:5])

# #시각화해볼게요
# plt.scatter(x_scaled,y)
# plt.show()
# #바짝 붙어서 난리났내요 뭐 뻔한거죠~

model=LinearRegression().fit(x_scaled,y)
y_pred=model.predict(x_scaled)
print('예측값:',y_pred[:5])
print('실제값:',y[:5])

#모델의 성능을 보고싶어 ols summary()쓰면안됨
#모델의 평가지표
print('--모델 성능 파악용 함수 작성--')
def RegScore_func(y_true,y_pred):
    print('r2_score(결정계수,설명력):{}'.format(r2_score(y_true, y_pred))) #1에가까우면 좋다
    print('explained_variance_score(설명분산점수):{}'.format(explained_variance_score(y_true, y_pred))) #1에가까우면 좋다
    #r2_score와 explained_variance_score가 다르게 나온다면 에러에 편향이생긴것이다.(학습이 잘못된것이다)
    print('mean_squared_error(MSE, 평균제곱오차):{}'.format(mean_squared_error(y_true, y_pred))) # 작을수록 좋다.
    #MSE: 평균제곱오차(Mean Squared Error, MSE)는 이름에서 알 수 있듯이 오차(error)를 제곱한 값의 평균
    #RMSE도 있다. 평균오차제곱근
    #평균제곱오차: 예측값에서 실제값(관찰값)을 뺀 값의 제곱의 합을 표본수로 나눈것
    
RegScore_func(y,y_pred)

print('---------두 변수의 표준편차가 다를 때: 분산이 큼---------')

x=np.random.normal(0,1, sample_size) #정규분포를 따릅니다. 평균은0, 분산은10 100개의 샘플을 뽑는다.
y=np.random.normal(0,500, sample_size)+x*30
print(x[:5])
print(y[:5])
print('상관계수: ',np.corrcoef(x,y)) #0.00401167

#독립변수 x에대한 정규화를 한 번 진행해보께요옴
scaler2=MinMaxScaler()
x_scaled2=scaler2.fit_transform(x.reshape(-1, 1)) #.inverse_transform 원상복구 #sklearn 에서 제공되는 애들은 매트릭스
print(x_scaled2[:5])

#시각화해볼게요
plt.scatter(x_scaled2,y)
plt.show()
#바짝 붙어서 난리났내요 뭐 뻔한거죠~

model2=LinearRegression().fit(x_scaled2,y)
y_pred2=model2.predict(x_scaled2)
print('예측값:',y_pred2[:5])
print('실제값:',y[:5])

#모델의 성능을 보고싶어 ols summary()쓰면안됨
#모델의 평가지표
print('--모델 성능 파악용 함수 작성--')
def RegScore_func2(y_true,y_pred2):
    print('r2_score(결정계수,설명력):{}'.format(r2_score(y_true, y_pred2))) #1에가까우면 좋다
    print('explained_variance_score(설명분산점수):{}'.format(explained_variance_score(y_true, y_pred2))) #1에가까우면 좋다
    #r2_score와 explained_variance_score가 다르게 나온다면 에러에 편향이생긴것이다.(학습이 잘못된것이다)
    print('mean_squared_error(MSE, 평균제곱오차):{}'.format(mean_squared_error(y_true, y_pred2))) # 작을수록 좋다.
    #MSE: 평균제곱오차(Mean Squared Error, MSE)는 이름에서 알 수 있듯이 오차(error)를 제곱한 값의 평균
    #RMSE도 있다. 평균오차제곱근
    #평균제곱오차: 예측값에서 실제값(관찰값)을 뺀 값의 제곱의 합을 표본수로 나눈것
    
RegScore_func2(y,y_pred2)