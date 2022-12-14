# 논리게이트 중 XOR은 복수의 뉴런(노드)를 사용해야한다.

import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam
from scipy.constants.constants import pt

# 논리회로 분류 모델 생성
x=np.array([[0,0],[0,1],[1,0],[1,1]])
print(x)
y=np.array([0,1,1,0]) # xor

model=Sequential()
'''
model.add(Dense(units=5, input_dim=2))
# 두개가 들어와 5개 노드로 나간다 (완전열결체)
model.add(Activation('relu')) #hidden layer에서 활성화함수는 relu를 사용한다.
model.add(Dense(units=1))
# 그다음 노드 하나로 빠져나간다 (완전 곱하기를 한다)
model.add(Activation('sigmoid'))
'''

# model.add(Flatten(input_dim=2)) # Flatten을 안써도 차원은 떨어진다. 하지만 가끔 명시적으로 써야할때도 있다.
# model.add(Dense(units=5, input_dim=2, activation='relu'))
# model.add(Dense(units=5, input_dim=2, activation='relu')) #위 두줄과 같다

#input_dim , input_shape 은 같으나 shape으로 쓸때는 튜플로 써줘야한다.
model.add(Dense(units=5, input_dim=2, activation='relu'))
# model.add(Dense(units=5, input_shape=(2, ), activation='relu'))
model.add(Dense(units=5, activation='relu'))
model.add(Dense(units=1,  activation='sigmoid'))

print(model.summary()) # 설계된 모델의 layer, parameter 확인할 때 사용
# 노드와 레이어를 늘려주면 Total params 값도 커진다.
# Trainable params: 참여개수

model.compile(optimizer=Adam(0.01),loss='binary_crossentropy',  metrics=['accuracy']) #클래스를 사용하면 learning_rate를 설정할 수 있다

history=model.fit(x,y, epochs=100, batch_size=1,verbose=0)
print('history loss:', history.history['loss'])
print('history acc:', history.history['accuracy'])
# epochs : 전체 데이터셋을 몇 번 반복학습할지 설정합니다.
# batch_size:몇 개의 샘플로 가중치를 갱신할 것인지 설정합니다.
# ex)batch_size=1 : 10문제라고하면 1문제풀고 답맞추고 해서 가중치가 10번 일어나고
# ex)batch_size=2 : 10문제라고하면 2문제풀고 답맞추고 해서 가중치가 5번 일어나고
# batch_size를 줄이면 가중치 횟수가 줄면 속도가 빨라지지만 적당히 주는것이 중요하다

loss_metrics= model.evaluate(x,y)
print('loss: ', loss_metrics[0],'acc: ',loss_metrics[1])

pred=(model.predict(x) > 0.5).astype('int32')
print(pred.flatten())
print(pred.ravel())

print()
print(model.input)
print(model.output)
# 그냥 참고야
print(model.weights) #kernel, bias 값 확인 가능 #weight는 w값

# 모델이 어떻게 움직이는지 확인하는 법
# history 시각화
import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['accuracy'], label='train acc')
plt.legend()
plt.xlabel('epochs')
plt.show()