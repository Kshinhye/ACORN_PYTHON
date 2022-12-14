# 활성화 함수, 학습 조기 종료

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import boston_housing

# print(boston_housing.load_data()) # keras는 이미 feature와 label을 나눠놨다
(x_train, y_train), (x_test,y_test)=boston_housing.load_data()
print(x_train.shape, y_train.shape,x_test.shape,y_test.shape)
print(x_train[0])
print(y_train[0])

# 데이터 표준화 (정규화보다 얘가 수식이 짧으니 얘로 갈게요)
# 수식: (관찰값 - 평균)/표준편차
x_mean=x_train.mean(axis=0)
x_std=x_train.std(axis=0)
x_train -= x_mean
x_train /=x_std
x_test -= x_mean
x_test /=x_std

y_mean=y_train.mean(axis=0) # 사실 y값은 손대지않아도 됩니다.
y_std=y_train.std(axis=0)
y_train -= y_mean
y_train /=y_std
y_test -= y_mean
y_test /= y_std

print(x_train[0])
print(y_train[0])

# model
# units은 보통 4의 배수로 많이들 준다.
model=tf.keras.Sequential([
    tf.keras.layers.Dense(units=52, activation='relu', input_shape=(13,)),
    tf.keras.layers.Dense(units=35, activation='relu'),
    tf.keras.layers.Dense(units=24, activation='relu'),
    tf.keras.layers.Dense(units=1)  
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.07), loss='mse', metrics=['mse'])
model.summary()

# 활성화함수 비교 sigmoid
import math
def sigmoid(x):
    return 1/(1 + math.exp(-x))
x=np.arange(-5,5,0.01)
sigmoid_x=[sigmoid(z) for z in x]
tanh_x=[math.tanh(z) for z in x]
relu=[0 if z < 0 else z for z in x]

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.plot(x, sigmoid_x, 'b-', label='sigmoid')
plt.plot(x, tanh_x, 'r--', label='than')
plt.plot(x, relu, 'g.', label='relu')
plt.show()

history=model.fit(x_train, y_train, epochs=25, batch_size=32, validation_split=0.25)

#시각화를 해볼까요
plt.plot(history.history['loss'], 'b-', label='loss')
plt.plot(history.history['val_loss'], 'r--', label='val_loss')
plt.xlabel('epochs')
plt.legend()
plt.show()

print(model.evaluate(x_test, y_test))

# 주택가격(실제값, 예측값) 시각화
pred_y=model.predict(x_test)
plt.figure(figsize=(5,5))
plt.plot(y_test, pred_y, 'b.')
plt.xlabel('y_test')
plt.ylabel('pred_y')
plt.legend()
plt.show()



# 학습 조기종료
model2=tf.keras.Sequential([
    tf.keras.layers.Dense(units=52, activation='relu', input_shape=(13,)),
    tf.keras.layers.Dense(units=35, activation='relu'),
    tf.keras.layers.Dense(units=24, activation='relu'),
    tf.keras.layers.Dense(units=1)  
])

model2.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.07), loss='mse', metrics=['mse'])
history=model2.fit(x_train, y_train, epochs=100, batch_size=32, validation_split=0.25,
                   callbacks=[tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)]) # 실무에서는 patience 10+-a 정도 준다.

#시각화를 해볼까요
plt.plot(history.history['loss'], 'b-', label='loss')
plt.plot(history.history['val_loss'], 'r--', label='val_loss')
plt.legend()
plt.show()

print(model2.evaluate(x_test, y_test))