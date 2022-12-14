# MNIST dataset (손글씨 이미지 데이터)으로 숫자 이미지 분류 모델 작성
# softmax
# MNIST는 숫자 0부터 9까지의 이미지로 구성된 손글씨 데이터셋입니다. 
# 이 데이터는 과거에 우체국에서 편지의 우편 번호를 인식하기 위해서 만들어진 훈련 데이터입니다. 
# 총 60,000개의 훈련 데이터와 레이블, 총 10,000개의 테스트 데이터와 레이블로 구성되어져 있습니다. 
# 레이블은 0부터 9까지 총 10개입니다. 

import tensorflow as tf
import numpy as np

(x_train, y_train),(x_test, y_test)=tf.keras.datasets.mnist.load_data()
# print(x_train.shape,y_train.shape,x_test.shape, y_test.shape) #(60000, 28, 28) (60000,) (10000, 28, 28) (10000,)
# print(x_train[0])
# print(y_train[0])

# import sys
# for i in x_train[0]:
#     for j in i:
#         sys.stdout.write('%s  '%j) #표준 출력장치
#     sys.stdout.write('\n')
    
# import matplotlib.pyplot as plt
# plt.imshow(x_train[0])
# plt.show()

# Dense에 넣기 위해 차원축소
x_train = x_train.reshape(60000,784).astype('float32')
x_test = x_test.reshape(10000,784).astype('float32')
# print(x_train[0], x_train[0].shape) # (784,)

# feature data를 정규화
x_train /= 255.0
x_test /= 255.0
# print(x_train[0])
# print(y_train[0], set(y_train))

# label은 원핫 처리- softmax를 사용하기 위해서
y_train=tf.keras.utils.to_categorical(y_train,10)
y_test=tf.keras.utils.to_categorical(y_test,10)
print(y_train[0])

# train data의 일부를 validation data로 사용하기
x_val=x_train[50000:60000] # 10000개는 validation으로 사용할라고
y_val=y_train[50000:60000]
x_train=x_train[0:50000] #50000개는 train
y_train=y_train[0:50000]

print(x_val.shape, x_train.shape) #(10000, 784) (50000, 784)

# model
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Dropout

model=Sequential()
# model.add(Dense(units=128, input_shape=(784,)))
# model.add(Flatten(input_shape=(28,28))) #reshape를 하지않는경우 Flatten을 사용해 784로 차원변경
# model.add(Dense())
# model.add(Activation('relu'))
# model.add(Dropout(rate=0.2))
"""
# 입력층
model.add(Dense(units=128, input_shape=(784,)))
model.add(Activation('relu'))
# Dropout hidden layer에만 준다.
model.add(Dropout(rate=0.2))

# 출력층
model.add(Dense(units=10))
model.add(Activation('softmax'))
"""

model.add(Dense(units=128, input_shape=(784,), activation='relu'))
# model.add(Flatten(input_shape=(28,28))) #reshape 안했을 때
model.add(Dropout(rate=0.2))
model.add(Dense(units=128, activation='relu'))
model.add(Dropout(rate=0.2))
model.add(Dense(units=10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

history=model.fit(x_train, y_train, epochs=10, batch_size=128, validation_data=(x_val, y_val), verbose=2)
print(history.history.keys())
print('loss: ', history.history['loss'])
print('val_loss: ', history.history['val_loss'])
print('accuracy: ', history.history['accuracy'])
print('val_accuracy: ', history.history['val_accuracy'])

# 시각화
import matplotlib.pyplot as plt

plt.plot(history.history['loss'], 'b-', label='loss', alpha=0.6)
plt.plot(history.history['val_loss'], 'r--', label='val_loss',alpha=0.6)
plt.xlabel('epochs')
plt.legend()
plt.show()

plt.plot(history.history['accuracy'], 'b-', label='accuracy', alpha=0.6)
plt.plot(history.history['val_accuracy'], 'r--', label='val_accuracy', alpha=0.6)
plt.xlabel('epochs')
plt.legend()
plt.show()


# 모델평가
score=model.evaluate(x_test, y_test, batch_size=128, verbose=0)
print('final loss: ', score[0])
print('final accuracy: ', score[1])

# 모델 저장하기
model.save('cla07model.hdf5')

# 여기서부터는 저장된 모델로 새로운 데이터에 대한 이미지 분류 작업 진행
mymodel = tf.keras.models.load_model('cla07model.hdf5')

pred=mymodel.predict(x_train[:1])
print('pred: \n', pred) # [[7.8099335e-15 1.2187644e-07 3.2181058e-10 5.2697980e-03 9.7979022e-16  9.9473011e-01 1.9101461e-12 2.8172213e-11 7.3701539e-10 2.4806885e-08]]
print('예측값: \n', np.argmax(pred, 1)) # [5] # 확률값 중 가장 큰 인덱스를 분류 결과로 얻음
print('실제값: \n', y_train[:1]) # [[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]]
print('실제값: \n', np.argmax(y_train[:1])) # 5



