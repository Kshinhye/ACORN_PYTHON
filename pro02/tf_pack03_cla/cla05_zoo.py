# 동물 타입 분류
# zoo animal dataset으로 동물의 type분류

from keras.models import Sequential
from keras.layers import Dense
import numpy as np

xy=np.loadtxt("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/zoo.csv", delimiter=',')
# print(xy[0], xy.shape) #(101, 17)
x_data=xy[:, 0:-1]
y_data=xy[:,-1]
# print(x_data[0])
# print(y_data[0], '', set(y_data)) #종류는 총 7가지

# train/test 생략 중요한것만 하고 갑니다. 우리는 시간이 없어요

# # label은 one-hot 처리필요
# from keras.utils import to_categorical
# y_data=to_categorical(y_data)
# print(y_data[0])

model=Sequential()
model.add(Dense(units=32, input_shape=(16,), activation='relu'))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=7, activation='softmax'))

print(model.summary())

# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


history=model.fit(x_data, y_data, epochs=100, batch_size=10, validation_split=0.3, verbose=0)
print('evaluate:', model.evaluate(x_data, y_data, batch_size=10, verbose=0))


# loss, acc를 시각화
import matplotlib.pyplot as plt
history_dict=history.history
loss=history_dict['loss']

val_loss=history_dict['val_loss']
acc=history_dict['accuracy']
val_acc=history_dict['val_accuracy']

plt.plot(loss, 'b-', label='loss', alpha=0.6)
plt.plot(val_loss, 'r--', label='val_loss',alpha=0.6)
plt.xlabel('epochs')
plt.legend()
plt.show()
plt.plot(acc, 'b-', label='acc', alpha=0.6)
plt.plot(val_acc, 'r--', label='val_acc', alpha=0.6)
plt.xlabel('epochs')
plt.legend()
plt.show()

print()
# 예측
pred_data=x_data[:1]
print('한개 예측값: ', np.argmax(model.predict(pred_data)))

pred_datas=x_data[:5]
preds=[np.argmax(i) for i in model.predict(pred_datas)]
print('여러개 예측값: \n', preds)
print('실제값: \n', y_data[:5])