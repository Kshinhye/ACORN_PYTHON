# Fashion MNIST로 CNN 처리
# Functional api사용

import tensorflow as tf
from keras import datasets, layers, models

(x_train, y_train),(x_test, y_test)=datasets.fashion_mnist.load_data()
print(x_train.shape, y_train.shape,x_test.shape,y_test.shape )
#(60000, 28, 28) (60000,) (10000, 28, 28) (10000,)

# 정규화
# 이미지 분류에서는 가급적 정규화나 표준화를 추천합니다(이래야 잘 나와요)
x_train=x_train/255.0 # 0~1 사이로 가두기
x_test=x_test/255.0 # 0~1 사이로 가두기

# CNN은 채널을 사용하기 때문에 3차원 데이터를 4차원으로 변경
x_train=x_train.reshape(-1, 28, 28, 1) 
# 맨뒤에 1은 채널(흑백은 채널이 한개), 맨앞에 60000대신 -1을쓰면 알아서 몇열인지 해준다.
x_test=x_test.reshape(-1, 28, 28, 1)
# 예) x_test[3,12,13,1] -> 3번쨰 인덱스에서 12행 13열 위치에 있는 1(흑백)채널값을 의미

# 그림 한 번 구경할까?
import matplotlib.pyplot as plt
# plt.figure()
# for i in range(16): #4행4열짜리에 돌려볼게요
#     plt.subplot(4,4,i+1)
#     plt.imshow(x_train[i], cmap='gray')
#
# plt.show()

# model
# Functional api
input_shape=(28,28,1)
img_input=layers.Input(shape=input_shape)

net=layers.Conv2D(filters=16, kernel_size=(3,3), activation='relu')(img_input)
net=layers.MaxPool2D(pool_size=(2,2))(net)

net=layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu')(net)
net=layers.MaxPool2D(pool_size=(2,2))(net)

net=layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu')(net)
net=layers.MaxPool2D(pool_size=(2,2))(net)

net=layers.Flatten()(net)

net=layers.Dense(units=64, activation='relu')(net)
net=layers.Dense(units=32, activation='relu')(net)
outputs=layers.Dense(units=10, activation='softmax')(net)

model=tf.keras.Model(inputs=img_input, outputs=outputs)

print(model.summary())

# 나머지는 이전 실습과 동일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 조기종료도 해볼까요
from keras.callbacks import EarlyStopping
es=EarlyStopping(monitor='val_loss', patience=3) #patience원래는 많이줘야하는데 급하니까 적게줄게요
history=model.fit(x_train, y_train, batch_size=128, epochs=1000, verbose=2, validation_split=0.2,callbacks=[es])

# history 저장
import pickle
history=history.history
with open('cnn02history.pickle', 'wb') as f:
    pickle.dump(history, f)

# 모델평가 (그냥 한번에 해볼게)
# 이 둘의 차이가 크면 좋은거 아니다.(차이가 크면 오버피팅이다)
train_loss, train_acc=model.evaluate(x_train, y_train)
test_loss, test_acc=model.evaluate(x_test, y_test)
print('train_loss:{} ,train_acc:{}'.format(train_loss,train_acc))
print('test_loss:{} ,test_acc:{}'.format(test_loss,test_acc))

# 모델 저장
model.save('cnn02model.h5')

print()
# -------학습된 모델로 작업-------------------------------
mymodel=tf.keras.models.load_model('cnn02model.h5')

# predict
import numpy as np
print('예측값: ', np.argmax(model.predict(x_test[:1])))
# print('예측값: ', np.argmax(model.predict(x_test[0])))
print('실제값: ', y_test[0])

# 시각화
import matplotlib.pyplot as plt

with open('cnn02history.pickle', 'rb') as f:
    history=pickle.load(f)

def plot_acc_func(title=None):
    plt.plot(history['accuracy'], label='accuracy')
    plt.plot(history['val_accuracy'], label='val_accuracy')
    plt.title(title)
    plt.xlabel('epochs')
    plt.ylabel(title)
    plt.legend()

plot_acc_func('accuracy')
plt.show()

def plot_loss_func(title=None):
    plt.plot(history['loss'], label='loss')
    plt.plot(history['val_loss'], label='val_loss')
    plt.title(title)
    plt.xlabel('epochs')
    plt.ylabel(title)
    plt.legend()

plot_acc_func('loss')
plt.show()








