# 선형회귀 모형 : 수식 사용 (keras 안쓰고 해볼게요)
# tensorflow사용

import tensorflow as tf
import numpy as np
from keras.optimizers import SGD, RMSprop, Adam #경사하강법을 지원하는 클래스

# 요번 예제에서는 GradientTape (자동으로 미분을 해주는 함수) 구경을 해두셔야해요. 언젠가는 써먹을 날이 올거야
x=[1.,2.,3.,4.,5.]
y=[1.2,2.8,3.0,3.5,6.0]
print(np.corrcoef(x,y)) #0.9371 # 두변수의 상관관계는 매우 높다
# 인과관계가 있다고 가정하고 회귀분석 작업을 진행

#w와b값은 이렇게 랜덤하게 들어온다.
tf.random.set_seed(123) #선생님과 같은 결과를 위해 난수를 붙잡음
w=tf.Variable(tf.random.normal((1,))) #정규분포를 따르는 난수 발생
b=tf.Variable(tf.random.normal((1,))) #정규분포를 따르는 난수 발생
print(w.numpy(),'',b.numpy())

# 이제 cost는 최소화하는 작업을 할거에요
# 선형회귀식을 얻기 위해 cost를 줄여가는 작업을 할거에요
opti=SGD()

@tf.function #안써도 되는데 얘를쓰면 더 빨라
def train_func(x,y):
    with tf.GradientTape() as tape: # 경사 기록 장치 : 이 안에서 수행되는 연산의 경사가 기록된다.
        hypo=tf.add(tf.multiply(w,x),b) #y=wx+b #(가설, 예측)
        loss=tf.reduce_mean(tf.square(tf.subtract(hypo,y)))

    grad=tape.gradient(loss, [w,b]) #자동 미분을 해줌
    opti.apply_gradients(zip(grad,[w,b])) #경사하강법을 지원
    
    return loss
    
w_vals=[]
cost_vals=[]

for i in range(1,101): # epochs 100회
    loss_val=train_func(x, y)
    cost_vals.append(loss_val.numpy())
    w_vals.append(w.numpy())
    # if i % 10 == 0:
    #     print(loss_val)
    
# print('cost: ',cost_vals) #100번 돌았으니까 100개가 들어가있겠지~
# print('w: ',w_vals)
print()
# w 와 cost를 시각화
import matplotlib.pyplot as plt
plt.plot(w_vals, cost_vals, marker='o', alpha=0.2,color='purple')
plt.xlabel('w')
plt.ylabel('cost')
plt.show()

print('cost가 최소일 때 w값을 볼까요: ', w.numpy()) #[0.90847826]
print('cost가 최소일 때 b값을 볼까요: ', b.numpy()) #[0.6487321]
# yhat=0.90847826*x + 0.6487321

# 선형회귀 식이 만들어졌다!! 이번에는 선형회귀식으로 시각화해볼까요
y_pred=tf.add((tf.multiply(x,w)),b)
print('y_pred: ',y_pred)
print('y: ',y)

plt.scatter(x, y,label='real')
plt.plot(x,y_pred, 'r-',label='pred')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

print()
# 새 값으로 정량적 예측
new_x=[3.5,9.7]
new_pred=tf.add((tf.multiply(new_x,w)),b)
print('새로운 예측값: ', new_pred.numpy())