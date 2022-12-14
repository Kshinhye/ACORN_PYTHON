# 이항분류는 뭐야? 시그모이드
# diabetes 데이터로 이항분류(sigmoid)와 다항분류(softmax)처리

from keras.models import Sequential
from keras.layers import Dense
import numpy as np

dataset=np.loadtxt("../testdata/diabetes.csv", delimiter=',')
# print(dataset[:1])
# print(dataset.shape) #(759, 9)
# print(dataset[:,-1])  #label 값 확인해보니, 0,1로 되어있다. 손을 댈 필요가 읎어요

from sklearn.model_selection import train_test_split
# 0~8열, 9열
x_train, x_test, y_train, y_test=train_test_split(dataset[:,0:8], dataset[:,-1], test_size=0.3, random_state=123)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(531, 8) (228, 8) (531,) (228,)

#===============================================================================
# # 이항분류 sigmoid / binary_crossentropy / 이항분류는 label을 0~1 사이의 값
#===============================================================================
model=Sequential()
model.add(Dense(units=64, input_dim=8, activation='relu'))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']) # 이항분류일 때 loss는 binary_crossentropy를 쓴다.
model.fit(x_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=0)
scores=model.evaluate(x_test, y_test) #마지막값만 볼까?
print('%s : %.2f'%(model.metrics_names[0], scores[0]))
print('%s : %.2f'%(model.metrics_names[1], scores[1]))

# 예측값 구하기
# print(x_train[0])
new_data=[[-0.0588235,0.20603,0.,0.,0.,-0.105812,-0.910333,-0.433333]]
pred=model.predict(new_data, batch_size=32, verbose=0)
print('sigmoid 예측결과: ',pred)
print('sigmoid 예측결과: ',np.where(pred>0.5,1,0))
# [[0.4277862]] 0.5를 기준으로 0과1을 분류

#===============================================================================
# # 다항분류 #softmax /categorical_crossentropy' 
# 레이블의 개수만큼 확률값으로 나온다.
# 다항분류일떄는 반드시 레이블에 대해 onehot처리를 해줘야한다.
#===============================================================================
# 다항분류 softmax
print(y_train[:3]) # onehot처리가 필요
from keras.utils import to_categorical #sklearn 에 onehot 사용가능

y_train=to_categorical(y_train)
y_test=to_categorical(y_test)
print(y_train[:3])

model2=Sequential()
model2.add(Dense(units=64, input_dim=8, activation='relu'))
model2.add(Dense(units=32, activation='relu'))
model2.add(Dense(units=2, activation='softmax'))
# label의 category 수 만큼 결과는 확률 값으로 출력된다

model2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) # 이항분류일 때 loss는 binary_crossentropy를 쓴다.
model2.fit(x_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=0)
scores2=model2.evaluate(x_test, y_test) #마지막값만 볼까?
print('%s : %.2f'%(model2.metrics_names[0], scores2[0]))
print('%s : %.2f'%(model2.metrics_names[1], scores2[1]))

new_data2=[[-0.0588235,0.20603,0.,0.,0.,-0.105812,-0.910333,-0.433333]]
pred2=model2.predict(new_data2, batch_size=32, verbose=0)
print('softmax 예측결과: ',pred2)
#softmax 예측결과:  [[0.6369634  0.36303654]] 
# 확률값이 가장 큰 지점의 index를 분류 결과로 취한다.
print('softmax 예측결과: ',np.argmax(pred2))