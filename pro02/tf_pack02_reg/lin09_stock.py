# 다중선형회귀
# 주식 데이터로 예측 모형 작성 전일 데이터로 익일 종가 예측

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import matplotlib.pyplot as plt


# 나는 pandas로 데이터플임 말고 바로 벡터(metrix)로 읽고싶어!! loadtxt사용
xy=np.loadtxt("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/stockdaily.csv", 
              delimiter=",", skiprows=1) 

print(xy[:2], xy.shape) # (732, 5)

x_data=xy[:,0:-1]
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
x_data=scaler.fit_transform(x_data)

print(x_data[:2])
y_data=xy[:,[-1]]
print(y_data[:2])
print(x_data.shape)
# 전일 Open High Low Volume 과 익일 Close를 한 행으로 만들기
x_data=np.delete(x_data, -1, axis=0)
y_data=np.delete(y_data,0)
print(x_data[0], y_data[0])
print()

#===============================================================================
# 분리 없이 그냥 검정해보자
#===============================================================================
print('--------------')
model=Sequential()
model.add(Dense(units=1, input_dim=4, activation='linear'))

model.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model.fit(x_data, y_data, epochs=200, verbose=0)
print('train/test split 없이 평가: ', model.evaluate(x_data, y_data, verbose=0))
# 임의의 자료로 예측값과 실제값 비교
print(x_data[10]) # 엇 1차원이네요 2차원으로 reshape 시켜볼까?
test=x_data[10].reshape(-1,4)
print('실제값: ', y_data[10]) #열번째것만 볼게요 
print('예측값: ',model.predict(test, verbose=0))
print()
#성능확인
pred=model.predict(x_data)
from sklearn.metrics import r2_score
print('train/test split 없이 결정계수 확인: ', r2_score(y_data, pred)) #0.993 WOW!! 과적합이 의심된다


# train/test 전 모델로 시각화
plt.plot(y_data, 'b')
plt.plot(pred, 'r--')
plt.show()

#===============================================================================
# train/test 분리 
print('\n 과적합 방지를 목적으로 학습/검정 데이터로 분리')
#===============================================================================
# 시계열 데이터는 셔플링되면 안된다. 
# 시계열 데이터는 일정한 시간 간격으로 측정되었거나 특정 시간 간격으로 수집된 주기적인 시간 간격을 따른다.
# 아래 방법이 번거롭다면 sklearn의 train_test_split 사용하여 shuffle=False을 적용하면된다. 
print(len(x_data)) #731
train_size=int(len(x_data) * 0.7) #511  220
test_size=len(x_data)-train_size
print(train_size,'', test_size)
x_train, x_test=x_data[0:train_size], x_data[train_size:len(x_data)]
y_train, y_test=y_data[0:train_size], y_data[train_size:len(y_data)]
print(x_train[:2], x_train.shape)
print(x_test[:2], x_test.shape)

model2=Sequential()
model2.add(Dense(units=1, input_dim=4, activation='linear'))

model2.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model2.fit(x_train, y_train, epochs=200, verbose=0)
print('train/test split 적용 후 평가: ', model2.evaluate(x_test, y_test, verbose=0))

#성능확인
pred2=model.predict(x_test)
from sklearn.metrics import r2_score
print('train/test split 없이 결정계수 확인: ', r2_score(y_test, pred2)) #0.959

#train/test 후 모델로 시각화
plt.plot(y_test, 'b')
plt.plot(pred2, 'r--')
plt.show()


#===============================================================================
# validation_split /  fit() 속성으로 가능 validation_split
#===============================================================================

model3=Sequential()
model3.add(Dense(units=1, input_dim=4, activation='linear'))

model3.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model3.fit(x_train, y_train, epochs=200, verbose=0,validation_split=0.15 )
print('train/test validation_split 후 평가: ', model3.evaluate(x_test, y_test, verbose=0))

#성능확인
pred3=model3.predict(x_test)

print('train/test split 없이 결정계수 확인: ', r2_score(y_test, pred3)) #0.84155 # 과적합 없음

#train/test 후 모델로 시각화
plt.plot(y_test, 'b')
plt.plot(pred3, 'r--')
plt.show()

# 머신러닝의 이슈: 모델의 최적화(optimization)와 일반화(포용성, generalization|꼬리가 없는 고양이도 고양이로 분류 돼야해) 사이의 줄다리기 -yg.park-
# 분산은 애증의 대상이다.