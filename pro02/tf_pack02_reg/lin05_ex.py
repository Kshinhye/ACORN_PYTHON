'''
문제1)
http://www.randomservices.org/random/data/Galton.txt

data를 이용해 아버지 키로 아들의 키를 예측하는 회귀분석 모델을 작성하시오.
train / test 분리
Sequential api와 function api 를 사용해 모델을 만들어 보시오.
train과 test의 mse를 시각화 하시오
새로운 아버지 키에 대한 자료로 아들의 키를 예측하시오.
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras.models import Sequential # 네트워크
from keras.layers import Dense, Activation # Dense완전연결층(자연어처리, 이미지처리도 얘로함)
from keras.optimizers import SGD,RMSprop, Adam
from sklearn.metrics import r2_score


df=pd.read_csv("http://www.randomservices.org/random/data/Galton.txt", sep="\t", usecols=['Father','Gender','Height'])
data=df[df['Gender']=='M'].drop('Gender',axis=1)
x=data['Father']
y=data['Height']
print(x.shape, y.shape)
print(np.corrcoef(x,y)[0][1]) #0.3913173
# print(df.info())
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.3, random_state=1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
#(325,) (140,) (325,) (140,)

#===============================================================================
# 방법1: Sequential api 사용
#===============================================================================
model1=Sequential()
model1.add(Dense(units=5, input_dim=1, activation='linear'))
model1.add(Dense(units=1,activation='linear'))

opti=Adam(learning_rate=0.001)
model1.compile(optimizer=opti, loss='mse', metrics=['mse'])

history=model1.fit(x_train, y_train, batch_size=4, epochs=50, verbose=0)
loss_metrics=model1.evaluate(x_test, y_test, verbose=0)
print('loss_metrics1: ', loss_metrics)

print('실제값 : ', y_test.head().values)
print('예측값 :', model1.predict(x_test).flatten()[:5])

# 시각화
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.plot(x_train, model1.predict(x_train), 'b', x_train, y_train, 'ko') # train
plt.show()

plt.plot(x_test, model1.predict(x_test), 'b', x_test, y_test, 'ko')  # test
plt.show()

plt.plot(history.history['mse'], label='평균제곱오차')
plt.xlabel('학습 횟수')
plt.show()

#===============================================================================
# 방법2: function api 사용
#===============================================================================
from keras.layers import Input
from keras.models import Model

inputs=Input(shape=(1,))
output1=Dense(units=5, activation='linear')(inputs)
output2=Dense(units=1, activation='linear')(output1)

model2=Model(inputs, output2)
opti=Adam(learning_rate=0.001)
model2.compile(optimizer=opti, loss='mse', metrics=['mse'])

history2=model2.fit(x_train, y_train, batch_size=4, epochs=50, verbose=0)
loss_metrics=model2.evaluate(x_train, y_train, verbose=0)
print('loss_metrics2: ', loss_metrics)

new_data = [75, 70, 80]
print('새로운 예측 키 값: ', model2.predict(new_data).flatten())