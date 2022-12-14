# 다중선형회귀모델 작성 후 텐서보드(모델의 구조 및 학습과정/결과를 시각화) 갱쟝히 중요한 기능이야. 꼭 써먹어야할 기능이야
# 다중선형회귀(입력값, feature가 여러개)

from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.metrics import r2_score

# 5명의 학생이 3회 시험 점수 예측
x_data=np.array([[70,85,80],[71,89,78],[50,80,60],[66,20,60],[50,30,10]])
y_data=np.array([73,82,72,57,34])

print('Sequential api 사용')
model=Sequential()
# model.add(Dense(1,input_dim=3, activation='linear')) #layer 1개짜리

model.add(Dense(6,input_dim=3, activation='linear', name='a')) #layer 3개짜리 #name: 설계도의 이름
model.add(Dense(3, activation='linear', name='b'))
model.add(Dense(1, activation='linear', name='c'))

print(model.summary())
# 일반적으로 (백프로 믿으면안된다) 층의 뉴런(노드) 개수를 늘리기보다는 층수(레이어)를 늘리는것이 이득이 많다.

opti=tf.keras.optimizers.Adam(learning_rate=0.01)
model.compile(optimizer=opti, loss='mse', metrics=['mse'])
history=model.fit(x_data, y_data, batch_size=1, epochs=30, verbose=0)

# plt.plot(history.history['loss'])
# plt.xlabel('epochs')
# plt.ylabel('loss')
# plt.show()

loss_metrics=model.evaluate(x_data, y_data, batch_size=1, verbose=0)
print('모델 학습 후 최종 loss', loss_metrics)
print('설명력: ', r2_score(y_data, model.predict(x_data, batch_size=1, verbose=0)))

print('funcional api')
from keras.layers import Input
from keras.models import Model

inputs=Input(shape=(3,))
output1=Dense(6, activation='linear', name='a')(inputs)
output2=Dense(3, activation='linear', name='b')(output1)
output3=Dense(1, activation='linear', name='x')(output2)

model2=Model(inputs, output3)


opti=tf.keras.optimizers.Adam(learning_rate=0.01)
model2.compile(optimizer=opti, loss='mse', metrics=['mse'])

#===============================================================================
# 텐서보드(TensorBoard): 
# 알고리즘을 시각화한다.복잡한 모델의 수행도중 발생하는 논리적 오류 등을 개선하기 위한 도구
#===============================================================================
from keras.callbacks import TensorBoard

tb=TensorBoard(log_dir='./my', histogram_freq=1, write_graph=True, write_images=False, update_freq='epoch', profile_batch=2, embeddings_freq=1)
#fit에다가 callback을 추가해주면된다.
history=model2.fit(x_data, y_data, batch_size=1, epochs=30, verbose=0, callbacks=[tb])
# Tensorboard실행방법
# cmd에서 해당 .py 파일이 있는 디렉토리에 이동 후 tensorboard --logdir my/ 실행

print(model2.summary())

loss_metrics=model2.evaluate(x_data, y_data, batch_size=1, verbose=0)
print('모델 학습 후 최종 loss', loss_metrics)
print('설명력: ', r2_score(y_data, model2.predict(x_data, batch_size=1, verbose=0)))
