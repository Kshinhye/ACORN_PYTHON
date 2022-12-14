# 자, 워밍없이야
# Keras 큰개념:라이브러리(작은개념:모듈)로 모델 생성 네트워크 구성하기

# 케라스의 가장 핵심적인 데이터 구조는 "모델" 이다.
# 케라스에서 제공하는 시퀀스 모델을 이용하여 레이어(뉴런)를 순차적으로 쉽게 쌓을 수 있다.
# 케라스는 Sequential에 Dense 레이어(fully-connected layers 완전히 연결된 레이어)를 쌓는 스택 구조를 사용한다.

import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, activation 
from keras.optimizers import SGD,RMSprop, Adam

# 케라스 모델링 순서 
# 논리회로 분류 모델 생성
#===============================================================================
# 1) 데이터 수집 및 가공
#===============================================================================
x=np.array([[0,0],[0,1],[1,0],[1,1]])
print(x)
y=np.array([0,1,1,1]) # or로 줌

#===============================================================================
# 2)모델(네트워크) 구성
# 시퀀스 모델을 생성한 뒤 필요한 레이어를 추가하며 구성한다.
#===============================================================================
# model=Sequential()
# model.add(Dense(units=1,input_dim=2)) #input_dim(입력 뉴런의수, 입력의 차원): 두개가 들어와서 / units=1: 1개로 빠져나감. 
# model.add(activation('sigmoid')) #activation: 활성화함수
model=Sequential([
    Dense(units=1,input_dim=2,activation='sigmoid')
]) #activation: 활성화 함수, 분류니까 시그모이드, 만약에 세개이상의 범주였으면 소프트맥스를 썼을거야

#===============================================================================
# 3)모델 학습 프로세스 생성
# 학습하기 전, 학습에 대한 설정을 수행한다. 손실 함수 및 최적화 방법을 정의. compile() 함수를 사용한다.
#===============================================================================
# model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
# model.compile(optimizer=SGD(learning_rate=0.01, momentum=0.9), loss='binary_crossentropy', metrics=['accuracy']) # 관성을 줌으로써 국소최저해에 빠지는걸 방지한다.
# model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
# model.compile(optimizer=RMSprop(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy']) 
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.compile(optimizer=Adam(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy']) 
# optimizer : 훈련 과정을 설정하는 옵티마이저를 설정. 'adam'이나 'sgd'와 같이 문자열로 지정할 수도 있다.
# sgd: 확률적 경사 하강법(Stochastic Gradient Descent, SGD) (원래는 클래스인데 객체로 만들어둠)
# loss      : 훈련 과정에서 사용할 손실 함수(loss function)를 설정.
# metrics   : 훈련을 모니터링 하기 위한 모델의 성능 지표를 선택/분류일 땐 acc

#===============================================================================
# 4)모델 학습시키기 = ML에서 학습이란 더 나은 표현(출력/output)을 찾는 자동화 과정이다.
# 훈련셋을 이용하여 구성한 모델로 학습 시킨다. fit() 함수를 사용한다.
#===============================================================================
model.fit(x=x,y=y, batch_size=1, epochs=100, verbose=0)

#===============================================================================
# 5) 모델 평가
# 준비된 시험셋으로 학습한 모델을 평가한다. eval‎uate() 함수를 사용
#===============================================================================
loss_metrics=model.evaluate(x,y,batch_size=1, verbose=0)
print('loss_metrics', loss_metrics)
# [0.4785129427909851, 0.75] [loss, accuracy]
#===============================================================================
# 6) 모델 사용하기
# 임의의 입력으로 모델의 출력을 얻는다. predict() 함수를 사용한다.
#===============================================================================
pred=model.predict(x, batch_size=1, verbose=0)
print('pred \n',pred)
# 보기 좋게하고싶다면
print('pred:',pred.flatten()) #flatten() 차원축소
pred1=(model.predict(x) > 0.5).astype('int32') # 0.5보다 크면1, 작으면 0으로 분류
print('pred1:',pred1.flatten())

#===============================================================================
# 7) 최적의 모델이 만들어졌다면 저장하기
#===============================================================================
model.save('tf05.hdf5') #Sequential 제공

# 저장한 모델 읽어보기
from keras.models import load_model
model=load_model('tf05.hdf5')
pred1=(model.predict(x) > 0.5).astype('int32') # 0.5보다 크면1, 작으면 0으로 분류
print('pred1:',pred1.flatten())