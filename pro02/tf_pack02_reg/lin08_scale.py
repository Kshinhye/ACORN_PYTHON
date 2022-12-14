# 다중선형회귀모델
# scaleing : feature간 단위의 차이가 클 경우 정규화/표준화 작업이 효과적 - label에는 적용하지않음
# 표준화: (요소값-평균)/표준편차
# 정규화: (요소값-최소값)/(최대값-최소값)

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler, minmax_scale, StandardScaler, RobustScaler

# StandardScaler: 표준화 / 이상치가 있으면 불균형
# MinMaxScaler: 정규화/ 이상치에 민감
# RobustScaler: 이상치의 영향을 최소화 함

data = pd.read_csv('../testdata/Advertising.csv')
del data['no'] # no열 지우기
print(data.head(3)) # 회귀 분석하기 딱 ^^
print(data.corr())
fdata=data[['tv','radio','newspaper']]
ldata=data[['sales']]

#===============================================================================
# 스케일링방법1: 정규화
#===============================================================================
# scaler=MinMaxScaler(feature_range=(0,1)) #0~1 사이의 값으로 맞춤
# fedata=scaler.fit_transform(fdata)
# print(fedata)

fedata=minmax_scale(fdata, feature_range=(0,1), axis=0, copy=True)
# print(fedata)
print(fdata.head(2))
print(fedata[:2])


#...

from sklearn.model_selection import train_test_split
x_train,x_test, y_train,y_test=train_test_split(fedata, ldata, shuffle=True, test_size=0.3, random_state=123)

model = Sequential()
model.add(Dense(20, input_dim=3, activation='linear')) # hidden에는 activation='relu'도 가능
model.add(Dense(10,  activation='linear'))
model.add(Dense(1, activation='linear'))

model.compile(optimizer='adam', loss='mse', metrics=['mse'])
print(model.summary()) #Total params: 301

# 모델 구조만 시각화
import tensorflow as tf
tf.keras.utils.plot_model(model, 'lin_model.png')

history=model.fit(x_train, y_train, epochs=100, batch_size=32, verbose=2,
                  validation_split=0.2) #validation_split: train 을 8:2로 쪼개서 8을 학습 를 검증으로 함

# 모델 평가 후 score확인
loss=model.evaluate(x_test, y_test, batch_size=32, verbose=0)
print('loss: ',loss[0])

# history값
print(history.history)
print(history.history['loss'])
#validation_split 를 하면 얘네가 추가로 생긴다.
print(history.history['val_loss'])
print(history.history['mse'])
print(history.history['val_mse'])

import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.legend()
plt.show()

# *** 전통적인 방법으로 선형회귀분석의 기존 가정 충족 조건 ***
# 1) 정규성 : 독립변수들의 잔차항이 정규분포를 따라야 한다.
# 2) 독립성 : 독립변수들 간의 값이 서로 관련성이 없어야 한다.
# 3) 선형성 : 독립변수의 변화에 따라 종속변수도 변화하나 일정한 패턴을 가지면 좋지 않다.
# 4) 등분산성 : 독립변수들의 오차(잔차)의 분산은 일정해야 한다. 특정한 패턴 없이 고르게 분포되어야 한다.
# 5) 다중공선성 : 독립변수들 간에 강한 상관관계로 인한 문제가 발생하지 않아야 한다.