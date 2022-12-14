# 이미지보강
# 이미지가 부족한 경우 기존 이미지를 변형시켜 이미지 수를 늘림

import tensorflow as tf
from keras.datasets import fashion_mnist
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint, EarlyStopping
import matplotlib.pyplot as plt
import numpy as np

(x_train, y_train),(x_test, y_test)=fashion_mnist.load_data()
x_train=x_train.reshape(-1,28,28,1).astype('float32') / 255
x_test=x_test.reshape(-1,28,28,1).astype('float32') / 255

# 원핫처리
y_train=to_categorical(y_train)
y_test=to_categorical(y_test)

# plt.figure(figsize=(10,10))
# for c in range(100):
#     plt.subplot(10,10,c+1)
#     plt.axis('off') # x축y축 다 빼버리기
#     plt.imshow(x_train[c].reshape(28,28), cmap='gray')
# plt.show()
'''
#===============================================================================
# # 이미지보강만 먼저 연습해볼게요
#===============================================================================
# x_train[0] Ankle boot로 연습
from keras.preprocessing.image import ImageDataGenerator

# rotation_range : 이미지회전값
# zoom_range : 이미지일부확대
# shear_range : 이미지기울기
# width_shift_range : 좌우(수평)이동
# height_shift_range : 상하(수직)이동
# horizontal_flip : 이미지가로뒤집기
# vertical_flip : 이미지세로뒤집기

img_generator=ImageDataGenerator(
    rotation_range=10,  #이미지회전값
    zoom_range=0.1,     #이미지일부확대/축소
    shear_range=0.5,    #이미지기울기로 회전
    width_shift_range=0.1,  #좌우(수평)이동
    height_shift_range=0.1, #상하(수직)이동
    horizontal_flip=True,   #이미지가로뒤집기
    vertical_flip=True  #이미지세로뒤집기
)

augument_size=100
x_augument=img_generator.flow(np.tile(x_train[0].reshape(28*28),100).reshape(-1,28,28,1),
                              np.zeros(augument_size), batch_size=augument_size,
                              shuffle=False).next()[0]
                              
plt.figure(figsize=(10,10))
for c in range(100):
    plt.subplot(10,10,c+1)
    plt.axis('off') # x축y축 다 빼버리기
    plt.imshow(x_augument[c].reshape(28,28), cmap='gray')
plt.show()
'''

# model
model=tf.keras.models.Sequential([
    # 이미지 데이터 특징 추출로 용량을 줄이기
    tf.keras.layers.Conv2D(filters=32, kernel_size=3, input_shape=(28,28,1),padding='same',activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=2),
    tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Conv2D(filters=64, kernel_size=3,padding='same',activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=2),
    tf.keras.layers.Dropout(0.3),
    
    # 벡터로 데이터 한 줄로 세우기(차원축소)
    tf.keras.layers.Flatten(),
    
    # 이미지 분류기
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(64,activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(32,activation='softmax'),
    tf.keras.layers.Dropout(0.3),
    
    tf.keras.layers.Dense(10, activation='softmax')
])

model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

# 베스트 파라미터값을 저장해봅시다.
import os
MODEL_DIR='./mymnist/'
if not os.path.exists(MODEL_DIR): # MODEL_DIR이 존재하지 않는다면 
    os.mkdir(MODEL_DIR) # 만든다.

modelpath='./mymnist/{epoch:02d}-{val_loss:.3f}.hdf5'
chkpoint=ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=0, save_best_only=True)

es=EarlyStopping(monitor='val_loss', patience=5)

history=model.fit(x_train, y_train, validation_split=0.2, epochs=100, batch_size=64, verbose=2, callbacks=[es, chkpoint])

print('evaluate acc: %.4f'%(model.evaluate(x_test, y_test,batch_size=64, verbose=0)[1]))

history=history.history
# 1열
plt.subplot(1,2,1)
plt.plot(history['acc'],marker='o', c='red',  alpha=0.3,label='accuracy')
plt.plot(history['val_acc'],marker='s', c='blue',  alpha=0.3, label='val_accuracy')
plt.xlabel('epochs')
plt.legend()
# 2열
plt.subplot(1,2,2)
plt.plot(history['loss'],marker='o', c='red',  alpha=0.3,label='loss')
plt.plot(history['val_loss'],marker='s', c='blue',  alpha=0.3, label='val_loss')
plt.xlabel('epochs')
plt.legend()
plt.show()
