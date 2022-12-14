'''
문제2)
https://github.com/pykwon/python/tree/master/data
자전거 공유 시스템 분석용 데이터 train.csv를 이용하여 대여횟수에 영향을 주는 변수들을 골라 다중선형회귀분석 모델을 작성하시오.
모델 학습시에 발생하는 loss를 시각화하고 설명력을 출력하시오.
새로운 데이터를 input 함수를 사용해 키보드로 입력하여 대여횟수 예측결과를 콘솔로 출력하시오.
'''

import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/data/train.csv",parse_dates=['datetime']) #csv는 sep=',' 안써도된다.
print(df.info())
df.drop(columns='datetime', inplace=True)
print(df.info())

#상관계수 확인
co_re=df.corr()
print(co_re['count'].sort_values(ascending=False))

x= df.loc[:,['registered','casual','temp','humidity']] 
#temp와 atemp는 상관관계가 높은 것 같다. 긍분산성, 다중분산성 문제가 발생할 가능성이 높다. 둘 중 하나만 사용하는것도 고려
y= df.iloc[:,-1]

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
x=scaler.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train,y_test=train_test_split(x,y,test_size=0.3)
# print(x_train.shape, x_test.shape, y_train.shape,y_test.shape)
# (7620, 5) (3266, 5) (7620,) (3266,)

from keras.models import Sequential
from keras.layers import Dense
model=Sequential()
model.add(Dense(units=1, input_dim=4)) #activation='linear' default

model.compile(optimizer='sgd', loss='mse', metrics=['mse'])
history=model.fit(x_train, y_train, epochs=20, verbose=0, validation_split=0.15) #조기종료를 시키면 epochs 신경 안써도된다.
print(history.history['loss'])

#시각화
import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label='train loss')
plt.xlabel('epochs')
plt.show()

#설명계수
from sklearn.metrics import r2_score
pred=model.predict(x_test)
print('설명력',r2_score(y_test, pred)) #설명력 0.924356 #epochs=10
# 99정도 나왔다 하면 문제가 있지만 설명력은 참고자료일 뿐이다. 

# 실제값 예측값 비교해봐도 좋습니다.
