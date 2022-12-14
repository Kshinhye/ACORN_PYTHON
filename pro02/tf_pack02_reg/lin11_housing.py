# 선형회귀용 다층(Perceptron) 분류모델/ Sequential, Functional api

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Input, Concatenate
from keras import Model
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics._scorer import r2_scorer

housing=fetch_california_housing()
print(housing.keys())
print(housing.data[:2])
print(housing.target[:2])
print(housing.feature_names) #['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
print(housing.target_names) #['MedHouseVal']

# train/test 
x_train_all, x_test, y_train_all, y_test=train_test_split(housing.data, housing.target, random_state=12)
print(x_train_all.shape, x_test.shape, y_train_all.shape, y_test.shape) #(15480, 8) (5160, 8) (15480,) (5160,)

# validation_split 같이 해보기
x_train, x_valid, y_train, y_valid=train_test_split(x_train_all, y_train_all, random_state=12)
print(x_train.shape, x_valid.shape, y_train.shape, y_valid.shape) #(11610, 8) (3870, 8) (11610,) (3870,)

# scale 조정 : 표준화
scaler=StandardScaler()
x_train = scaler.fit_transform(x_train)
x_valid = scaler.fit_transform(x_valid)
x_test = scaler.fit_transform(x_test)
# sclaer 원복은 | scaler.inverse_transtorm(x_test)
print(x_train[:2])

print('-------Sequential api : 단순한 네트워크(설계도) 구성-------')
model=Sequential()
model.add(Dense(units=30, activation='relu', input_shape=x_train.shape[1:])) #(11610, 8) 여기서 8을 의마하는거임
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mse', metrics=['mse'])
history=model.fit(x_train, y_train, epochs=20, batch_size=32, validation_data=(x_valid, y_valid), verbose=2)
print('eveluate: ', model.evaluate(x_test, y_test, batch_size=32, verbose=0))



print('-------Functional api1: 이전 방법보다 복잡하고 유연한 네트워크(설계도) 구성-------')
input_=Input(shape=x_train.shape[1:])
net1=Dense(units=30, activation='relu')(input_) # 이걸보고 functional api다!! 라는걸 알아야한다.
net2=Dense(units=30, activation='relu')(net1)
concat=Concatenate()([input_, net2]) #마지막 은닉층의 출력과 입력층을 연결(Concatenate 층을 만듦)
output=Dense(units=1)(concat) #1개의 노드와 activation function이 없는 출력층

model2=Model(inputs=[input_],outputs=[output] )

model2.compile(optimizer='adam', loss='mse', metrics=['mse'])
history2=model2.fit(x_train, y_train, epochs=20, batch_size=32, validation_data=(x_valid, y_valid), verbose=0)
print('eveluate: ', model2.evaluate(x_test, y_test, batch_size=32, verbose=0))

#predict
x_new=x_test[:3]
y_pred2=model2.predict(x_new)
print('예측값: ', y_pred2.ravel())
print('실제값: ', y_test[:3])

#시각화
plt.plot(range(1,21),history2.history['mse'], c='b', alpha=0.3, label='mse')
plt.plot(range(1,21),history2.history['val_mse'], c='r',alpha=0.3, label='mse')
plt.xlabel('epoch')
plt.show()

print('-------Functional api3: 유연한 네트워크(설계도)구성- 일부는 짧은경로, 일부는 긴 경로 ------')
# 여러개의 입력층 사용
# 예) 5개(0~4)의 특성은 짧은경로, 나머지는 6개(2~7)로 긴 경로 사용 (중복가능)
input_a=Input(shape=[5], name='wide_input') # 짧은경로

input_b=Input(shape=[6], name='deep_input') # 긴경로
net1=Dense(units=30, activation='relu')(input_b)
net2=Dense(units=30, activation='relu')(net1)

concat=Concatenate()([input_a, net2])
output=Dense(units=1, name='output')(concat)

model3=Model(inputs=[input_a, input_b], outputs=[output])

model3.compile(optimizer='adam', loss='mse', metrics=['mse'])

#여기도 바껴야한다.
#fit 처리시 입력값이 하나가 아닌 복수이다.
x_train_a, x_train_b=x_train[:,:5], x_train[:, 2:] #train 용 #모든행의 5개, 모든행의 두번쨰 이후 (짧은경로 긴경로)
x_valid_a, x_valid_b=x_valid[:,:5], x_valid[:, 2:] #train 용
x_test_a, x_test_b=x_test[:,:5], x_test[:, 2:] # evaluate 용
x_new_a, x_new_b=x_test_a[:3], x_test_b[:3] # predict 용


history3=model3.fit(x=(x_train_a,x_train_b) , y=y_train, epochs=20, batch_size=32, validation_data=((x_valid_a,x_valid_b), y_valid), verbose=0)
print('eveluate: ', model3.evaluate((x_test_a,x_test_b), y_test, batch_size=32, verbose=0))

#predict
y_pred3=model3.predict(x=(x_new_a,x_new_b))
print('예측값: ', y_pred3.ravel())
print('실제값: ', y_test[:3])

#시각화
plt.plot(range(1,21),history3.history['mse'], c='b', alpha=0.3, label='mse')
plt.plot(range(1,21),history3.history['val_mse'], c='r',alpha=0.3, label='mse')
plt.xlabel('epoch')
plt.show()