# 단순선형회귀모델 작성: 방법3가지 경험하기
import tensorflow as tf
from keras.models import Sequential # 네트워크
from keras.layers import Dense, Activation # Dense완전연결층(자연어처리, 이미지처리도 얘로함)
from keras import optimizers
import numpy as np

# 공부시간에 따른 성적 결과
x_data=np.array([1,2,3,4,5], dtype=np.float32)
y_data=np.array([5,32,55,61,80], dtype=np.float32)
print('상관계수(r)= ', np.corrcoef(x_data, y_data)[0][1])

print('------방법1: Sequential api 사용: 가장 단순함. 레이어에 노드를 순서대로 쌓아올린 완전 연결층-------')
model=Sequential()
# # 하나로 들어와서 하나의 노드로 빠져나감
# model.add(Dense(units=1, input_dim=1, activation='linear'))

#레이어를 복수로 사용할 경우
# 하나로 들어와서 두개의 노드를 거쳐서 하나로 빠져나감 (근데 회귀분석에서는 큰 영향은 없다)
model.add(Dense(units=2, input_dim=1, activation='relu'))
model.add(Dense(units=1,activation='linear'))


#여러개써보고 가장 성능이 좋은애로 선택한다.
opti=optimizers.Adam(learning_rate=0.1)
model.compile(optimizer=opti, loss='mse', metrics=['mse']) #adam class를 사용하여 cost를 minimize한다
#학습
history=model.fit(x_data, y_data, batch_size=1, epochs=100, verbose=0)
loss_metrics=model.evaluate(x_data, y_data, verbose=0) #fit의 제일 마지막값을 가지고있다.
print('loss_metrics: ', loss_metrics)
#모델 성능을 자세히 알고 싶으면 r2_score를 사용해야한다.
from sklearn.metrics import r2_score
print('설명력: ', r2_score(y_data, model.predict(x_data, verbose=0)))
print('실제값: ', y_data)
print('예측값: ', model.predict(x_data, verbose=0).flatten())

new_data=[1.5,2.3,5.7]
print('성적예측값: ',model.predict(new_data).flatten())

import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
# loss 시각화(mse하고 똑값은값이죠~)
plt.plot(history.history['mse'], label='평균제곱오차')
plt.xlabel('학습횟수')
plt.show()
#추세선
plt.plot(x_data, model.predict(x_data), 'r', x_data, y_data, 'ko')
plt.show()

print()
print('------방법2: Functional API: Sequential보다는 유연한 구조를 가지고있다.(웅통성있다)-------')
from keras.layers import Input
from keras.models import Model

#각층은 일종의 함수처럼 처리함
inputs=Input(shape=(1,)) # input클래스를 만들고 입력크기를 지정한다.
#바로 내보낼것이라면
# outputs=Dense(units=1, activation='linear')(inputs)  #함수의 파라미터를 주듯이 다음층 함수의 이볅으로 사용하도록 변수에할당. 이전층(네트워크)들을 준다

# 복수사용법
output1=Dense(units=2, activation='relu')(inputs)
output2=Dense(units=1, activation='linear')(output1)

model2=Model(inputs, output2) #모델의 파라미터로 입력네트워크와 출력네트워크를 주낟.

#이하는 방법1과 동일

#여러개써보고 가장 성능이 좋은애로 선택한다.
opti=optimizers.Adam(learning_rate=0.1)
model2.compile(optimizer=opti, loss='mse', metrics=['mse']) #adam class를 사용하여 cost를 minimize한다
#학습
history=model2.fit(x_data, y_data, batch_size=1, epochs=100, verbose=0)
loss_metrics=model2.evaluate(x_data, y_data, verbose=0) #fit의 제일 마지막값을 가지고있다.
print('loss_metrics: ', loss_metrics)
#모델 성능을 자세히 알고 싶으면 r2_score를 사용해야한다.
print('loss_metrics: ', loss_metrics)
from sklearn.metrics import r2_score
print('설명력: ', r2_score(y_data, model2.predict(x_data, verbose=0)))

print()
print('------방법3: sub classing사용:동적인 구조가 필요한 경우, 메소드를 통해 분석가의 생각을 프로그래밍화-------')
print('-----multi-input, multi-output 다중입력출력 모델이다. 데이터 흐름이 순차적이지 않은 경우에도 사용이 가능하다-----')
# 단순

# 공부시간에 따른 성적 결과
x_data=np.array([[1],[2],[3],[4],[5]], dtype=np.float32)
y_data=np.array([5,32,55,61,80], dtype=np.float32)

class MyModel(Model):#모델 클래스를 상속받는다.
    def __init__(self):
        super(MyModel, self).__init__() # 모델생성자를 부르면서 모델을 넘겨준다
        # 네트워크형성
        # 생성자 내에서 필요한 layer를 생성한 후 call 메소드에서 수행하려는 연산을 적어줌
        self.d1=Dense(2,activation='linear') #proto타입아님
        self.d2=Dense(1,activation='linear')
        
    def call(self, x): #input 매개ㅁ변수 x를 준다. call은 자동호출이다,시스템에서 호출됨(callback)
        inputs=self.d1(x) #d1에 입력값을 준다. 
        return self.d2(inputs) #메소드라서 파라미터를 준다.
    
model3=MyModel()

#여러개써보고 가장 성능이 좋은애로 선택한다.
opti=optimizers.Adam(learning_rate=0.1)
model3.compile(optimizer=opti, loss='mse', metrics=['mse']) #adam class를 사용하여 cost를 minimize한다
#학습
history=model3.fit(x_data, y_data, batch_size=1, epochs=100, verbose=0)
loss_metrics=model3.evaluate(x_data, y_data, verbose=0) #fit의 제일 마지막값을 가지고있다.
#모델 성능을 자세히 알고 싶으면 r2_score를 사용해야한다.
print('loss_metrics: ', loss_metrics)
from sklearn.metrics import r2_score
print('설명력: ', r2_score(y_data, model3.predict(x_data, verbose=0)))

print()
print('------방법3-1: sub classing사용:동적인 구조가 필요한 경우, 메소드를 통해 분석가의 생각을 프로그래밍화-------')
from keras.layers import Layer

# Custom Layer 작성: 케라스의 정의된 레이어 이외의 새로운 연산을 위한 레이어 혹은 편의를 목적으로 여러 레이어를 하나로 묶어 처리할 경우
class MyLinear(Layer): 
    def __init__(self, units=1):
        super(MyLinear, self).__init__()
        self.units=units
    
    def build(self, input_shape): # 모델의 가중치, 편향과 관련된 내용을 기술
        self.w=self.add_weight(shape=(input_shape[-1], self.units), initializer='random_normal', trainable=True)
        #input_shape[-1]: -1을 주면 지알아서 크기를 찾는다. #trainable: True로 설정하면 BackPropagation 한다.
        # initializer='random_normal',: w값은 정규분포를 따르는 랜덤값으로 초기화된다.
        # (shape=(input_shape[-1], self.units) 입력값과 출력값
        
        self.b=self.add_weight(shape=(self.units,), initializer='zeros',trainable=True)
        
    def call(self, inputs): #정의된 값들을 이용하여 해당 층의 로직을 기술
        #여기서 y=wx+b를 만들어준다.
        return tf.add(tf.matmul(inputs, self.w),self.b)  #matmul(행렬곱)
    
    #build가 call을 부른다.
    
class MyMLP(Model):
    def __init__(self):
        super(MyMLP, self).__init__()
        # 레이어(노드) 하나짜리
        # self.linear1 = MyLinear(1) #레이어를 상속받은 mylinear 호출 
        # 레이어 두개짜리
        self.linear1=MyLinear(2)
        self.linear2=MyLinear(1)
        
        
    def call(self, inputs): #모델의 콜 이 call은 build를 부른다. 모델에서 fit, evaluate, predict 될때마다 호출된다.
        # return self.linear1(inputs)
        net=self.linear1(inputs) # 레이어 두개짜리
        return self.linear2(net)

model4=MyMLP()

# 이하는 방법1과 동일
opti = optimizers.Adam(learning_rate=0.1) 
model4.compile(optimizer=opti, loss='mse', metrics=['mse'])
model4.fit(x=x_data, y=y_data, batch_size=1, epochs=100, verbose=0)
loss_metrics = model4.evaluate(x=x_data, y=y_data, verbose=0)
print('loss_metrics4 :', loss_metrics)
print('설명력4 :', r2_score(y_data, model4.predict(x_data, verbose=0)))
print(model4.summary())