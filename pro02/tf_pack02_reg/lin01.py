# 모델의 정확도가 높을수록 비용함수 값은 낮아진다.

import numpy as np
import math
#--------------------------------------------------
real=[10,9,3,2,11] # y의 실제값이라고 가정
pred=[11,5,2,4,3] # y예측값(모델에의해 얻어진 값이라 가정)

cost=0
for i in range(5):
    cost += math.pow(pred[i]-real[i],2) #pow 거듭제곱
    print('cost',cost)
print('cost: ',cost/len(pred)) #cost:  17.2
#--------------------------------------------------
real=[10,9,3,2,11] # y의 실제값이라고 가정
pred=[11,8,4,4,11] # y예측값(모델에의해 얻어진 값이라 가정)

cost=0
for i in range(5):
    cost += math.pow(pred[i]-real[i],2) #pow 거듭제곱
    print('cost',cost)
print('cost: ',cost/len(pred)) #cost:  1.4
print()
print('--------------------------------------------------')
# 가중치(W(weight)와 비용함수(cost function/loss/손실/비용함수)의 변화 값을 시각화
import tensorflow as tf
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]
b=0 #간섭을 최소화하기위해 0으로 준다.

# hypothesis=x*w+b
# cost=tf.reduce_sum(tf.pow(hypothesis-y, 2))/len(x) #reduce_sum 합을 구하고 차원을 떨어뜨린다
# 비용함수 = 예측값 - 실제값에 제곱을 하고 그 합에 대한 평균

w_val=[]
cost_val=[]

for i in range(-30,50): #원래는 랜덤으로 들어오는데 예쁘게 그리려고 w값을 -50 ~ 50으로 줬다.
    feed_w=i*0.1
    # print(feed_w)
    # hypothesis=x*w+b # 추세선을 구하기 위한 1차 방정식
    hypothesis=tf.multiply(feed_w,x)+b
    cost=tf.reduce_mean(tf.square(hypothesis-y))
    cost_val.append(cost)
    w_val.append(feed_w)
    print(str(i)+''+', cost: '+str(cost.numpy())+', weight:'+str(feed_w))
    
plt.plot(w_val, cost_val)
plt.xlabel('w')
plt.ylabel('cost')
plt.legend()
plt.show()