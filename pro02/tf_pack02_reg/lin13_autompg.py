# AutoMPG dataset으로 자동차 연비 예측 모델
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from keras import layers

dataset=pd.read_csv("../testdata/auto-mpg.csv", na_values='?') #na_values=  : ?는 na로 대체하겠다
# print(dataset.head(3))
del dataset['car name']
# 찜찜한 칼럼 날려볼게요
print(dataset.corr())
dataset.drop(['acceleration', 'origin'], axis='columns', inplace=True)

# print(dataset.info())
# print(dataset.corr())

# print(dataset.isna().sum()) #horsepower      6
dataset=dataset.dropna()
# print(dataset.isna().sum())

# # 시각화 잠시 해볼게
# sns.pairplot(dataset[['mpg','displacement','horsepower','weight','acceleration']], diag_kind='kde')
# plt.show()

train_dataset=dataset.sample(frac=0.7, random_state=123)
test_dataset=dataset.drop(train_dataset.index)
# print(train_dataset.shape,test_dataset.shape) #(274, 8) (118, 8)

# 표준화 작업
train_stat=train_dataset.describe()
# print(train_stat)
train_stat.pop('mpg') #mpg는 label로 사용할 것이므로 뽑아버리기
train_stat=train_stat.transpose() #행렬 위치바꿈
# print(train_stat)


# label : mpg만 뽑아 가져오기
train_label=train_dataset.pop('mpg')
test_label=test_dataset.pop('mpg')

def st_func(x): #표준화 함수
    return (x - train_stat['mean']) /train_stat['std']

# print(st_func(10)) # 관찰값 10을 줘본다.
# print(train_dataset[:3])
# print(st_func(train_dataset[:3]))

# feature
st_train_data=st_func(train_dataset) 
st_test_data=st_func(test_dataset)
print(train_dataset.columns)

print()
# model
from keras.models import Sequential
from keras.layers import Dense

def build_model():
    # 설계도 
    network=Sequential([
        Dense(units=64, activation='relu', input_shape=[5]),
        Dense(units=64, activation='relu'),
        Dense(units=1, activation='linear')
    ])
    
    opti=tf.keras.optimizers.RMSprop(0.001)
    network.compile(optimizer=opti, loss='mean_squared_error', metrics=['mean_absolute_error','mean_squared_error']) #metrics 모델성능점수확인을 위해
    
    return network

model=build_model()
print(model.summary())

# fit() 전에 모델을 실행해되 됨, 다만 성능은 신경쓰지 않는다.
print(model.predict(st_train_data[:1]))

#훈련에 들어가보자
epochs=10000
early_stop=tf.keras.callbacks.EarlyStopping(monitor='val_loss', mode='auto', patience=5) 
#학습을 검정하는 목적인 validation data가 참여하기 때문에 val_loss # patience: val_loss가 5번이상 떨어지지않으면 조기종료

history=model.fit(st_train_data, train_label, batch_size=32, epochs=epochs, validation_split=0.2, verbose=2, callbacks=[early_stop])

#히스토리의 결과를 데이터 프레임에 담아볼까요?
df=pd.DataFrame(history.history)
print(df.head(3))

import matplotlib.pyplot as plt
# matplotlib inline

def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch

  plt.figure(figsize=(8,12))
  plt.subplot(2,1,1)
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [MPG]')
  plt.plot(hist['epoch'], hist['mean_absolute_error'],label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_absolute_error'],label = 'Val Error')
  plt.legend()

  plt.subplot(2,1,2)
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error [$MPG^2$]')
  plt.plot(hist['epoch'], hist['mean_squared_error'],label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_squared_error'],label = 'Val Error')
  plt.legend()
  plt.show()
plot_history(history)

# 모델 평가
loss, mae, mse=model.evaluate(st_test_data, test_label)
print('loss: {:.3f}'.format(loss))
print('mae: {:.3f}'.format(mae))
print('mse: {:.3f}'.format(mse))

from sklearn.metrics import r2_score
print('설명력: ', r2_score(test_label, model.predict(st_test_data)))