import tensorflow as tf
from keras.models import Sequential # 네트워크
from keras.layers import Dense # 완전연결층
from keras import optimizers
import numpy as np

x_data = [1.,2.,3.,4.,5.]
y_data = [1.2,2.0,3.0,3.5,5.5]
# 회귀분석이니까 상관계수를 봐야지~
print('상관계수: ', np.corrcoef([x_data, y_data])) #양의상관관계가 매우 높다.

#모델구성
model=Sequential()
model.add(Dense(units=1, input_dim=1, activation='linear')) # (노드하나)한개로 빠져나갈거야 #linear: 별다른 계산없이 그대로 빠져나간다

model.compile(optimizer='sgd', loss='mse', metrics=['mse']) #mse: 평균제곱오차
#논리회로로 만들거랑 차이(activation, loss(엔트로피계열이 아니라 mse사용함)

model.fit(x_data, y_data, batch_size=1, epochs=100, verbose=0)
print(model.evaluate(x_data, y_data)) #[0.10984816402196884, 0.10984816402196884]

pred=model.predict(x_data)
print('예측값: ', pred.flatten())
print('실제값: ',y_data)

#결정계수(상관계수를 제곱한 값)
from sklearn.metrics import r2_score
print('결정계수(설명력): ', r2_score(y_data, pred))

#시각화
import matplotlib.pyplot as plt
plt.plot(x_data, y_data, 'bo', alpha=0.5)
plt.plot(x_data, pred, 'r')
plt.show()

#새로운값으로 예측해보기
new_x=[1.5,2.5,3.3]
print('예측결과: ', model.predict(new_x).flatten())
# [1.4759394 2.4660892 3.258209 ]
