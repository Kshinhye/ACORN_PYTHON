# 다항회귀: Polynomial Regression : 비선형 데이터인 경우 다항식을 이용하여 다항회귀 처리 가능
# tensorflow를 이용하여 2차함수 회귀서 ㄴ그리기

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import random
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

"""
# 워밍업

# 다항 회귀 연습용 데이터 : 지역별 인구증가율과 고령인구비율(통계청 시각화 자료에서 발췌)
x = [0.3, -0.78, 1.26, 0.03, 1.11, 0.24, -0.24, -0.47, -0.77, -0.37, -0.85, -0.41, -0.27, 0.02, -0.76, 2.66]
y = [12.27, 14.44, 11.87, 18.75, 17.52, 16.37, 19.78, 19.51, 12.65, 14.74, 10.72, 21.94, 12.83, 15.51, 17.14, 14.42]


# a, b, c 세 개의 변수 선언
a = tf.Variable(random.random())
b = tf.Variable(random.random())
c = tf.Variable(random.random())

# 잔차 제곱 평균 반환 함수
def compute_loss():
    y_pred=a * x * x +b * x + c #yhat=ax^2 + bx +c
    loss=tf.reduce_mean((y-y_pred)**2) #잔차= 실제값-예측값
    return loss

optimizer=tf.keras.optimizers.Adam(learning_rate=0.05)

for i in range(1000):
    optimizer.minimize(compute_loss, var_list=[a,b,c])
    
    if i % 100==99:
        print(i, 'a:', a.numpy(), ',b: ', b.numpy(), ',c: ', c.numpy(),',loss: ', compute_loss().numpy())

line_x=np.arange(min(x), max(x), 0.01)
line_y=(a*line_x * line_x) + (b * line_x) +c  ##yhat=ax^2 + bx +c

plt.plot(line_x, line_y, 'r-')
plt.plot(x,y, 'bo')
plt.show()
"""

# 다항 회귀 연습용 데이터 : 지역별 인구증가율과 고령인구비율(통계청 시각화 자료에서 발췌)
pop_inc = [0.3, -0.78, 1.26, 0.03, 1.11, 0.24, -0.24, -0.47, -0.77, -0.37, -0.85, -0.41, -0.27, 0.02, -0.76, 2.66]
pop_old = [12.27, 14.44, 11.87, 18.75, 17.52, 16.37, 19.78, 19.51, 12.65, 14.74, 10.72, 21.94, 12.83, 15.51, 17.14, 14.42]

# # plt.plot(pop_inc, pop_old, 'ro')
# # plt.xlabel('지역별 인구증가율')
# # plt.ylabel('고령인구비율')
# # plt.show()
#
# print('------최소제곱법을 사용해 회귀선을 그어보자-------------------')
# # 절편과 기울기 구하기
# x_mean=sum(pop_inc)/len(pop_inc)
# y_mean=sum(pop_old)/len(pop_old)
#
# #기울기, 절편 계산
# # 기울기, 절편 계산 : a=sum(x - mean(x))(y - meany(y)) / sum(x-mean(x))^2
# a= sum([(y-y_mean)*(x-x_mean) for y, x in list(zip(pop_old, pop_inc))])
# a /= sum([(x-x_mean)**2 for x in pop_inc])
# b= y_mean - x_mean * a
#
# print('a: ',a, ',b: ',b)
#
# # 이걸로 그래프를 그려볼까요
#
# line_x=np.arange(min(pop_inc), max(pop_inc), 0.01)
# line_y=a*line_x + b 
#
# plt.plot(pop_inc, pop_old, 'bo', alpha=0.4)
# plt.plot(line_x, line_y, 'r-')
# plt.xlabel('지역별 인구증가율')
# plt.ylabel('고령인구비율')
# plt.show()
#
# print()
# print('------------ tf 사용해 회귀선을 그어보자----------------------')
# # 기울기와 절편은 랜덤하게 시작해 최소화된다.
# a=tf.Variable(random.random()) #기울기
# b=tf.Variable(random.random()) #절편
#
# # y=ax+b
# def compute_loss():
#     ypred=a*pop_inc + b
#     loss=tf.reduce_mean((pop_old - ypred)**2)
#     return loss
#
# optimizer=tf.keras.optimizers.Adam(learning_rate=0.05)
#
# for i in range(1,1001):
#     optimizer.minimize(compute_loss, var_list=[a,b])
#
#     if i % 100==0:
#         print(i, 'a:', a.numpy(), ',b: ', b.numpy(),'loss: ', compute_loss().numpy())
#
# line_x=np.arange(min(pop_inc), max(pop_inc), 0.01)
# line_y=a*line_x + b 
#
# plt.plot(pop_inc, pop_old, 'bo', alpha=0.4)
# plt.plot(line_x, line_y, 'r-')
# plt.xlabel('지역별 인구증가율')
# plt.ylabel('고령인구비율')
# plt.show()
#
#
# print()
# print('------------ 다항회귀: 비선형일 경우 사용----------------------')
# # a, b, c 세 개의 변수 선언
# a = tf.Variable(random.random())
# b = tf.Variable(random.random())
# c = tf.Variable(random.random())
#
# # 잔차 제곱 평균 반환 함수
# # #yhat=ax^2 + bx +c 
# def compute_loss2():
#     y_pred=(a * pop_inc * pop_inc) + (b * pop_inc) + c #yhat=ax^2 + bx +c
#     loss=tf.reduce_mean((pop_old-y_pred)**2) #잔차= 실제값-예측값
#     return loss
#
# optimizer=tf.keras.optimizers.Adam(learning_rate=0.05)
#
# for i in range(1000):
#     optimizer.minimize(compute_loss2, var_list=[a,b,c])
#
#     if i % 100==99:
#         print(i, 'a:', a.numpy(), ',b: ', b.numpy(), ',c: ', c.numpy(),',loss: ', compute_loss2().numpy())
#
# line_x=np.arange(min(pop_inc), max(pop_inc), 0.01)
# line_y=(a*line_x * line_x) + (b * line_x) +c  ##yhat=ax^2 + bx +c
#
# plt.plot(pop_inc, pop_old, 'bo', alpha=0.4)
# plt.plot(line_x, line_y, 'r-')
# plt.xlabel('지역별 인구증가율')
# plt.ylabel('고령인구비율')
# plt.show()


print('------------ 다항회귀: 딥러닝 네트워크 사용----------------------')
model=tf.keras.Sequential([
    tf.keras.layers.Dense(units=64, input_shape=(1,), activation='relu'),
    tf.keras.layers.Dense(units=32, activation='relu'),
    tf.keras.layers.Dense(units=1)
])

model.compile(optimizer='sgd', loss='mse')
model.summary()

model.fit(pop_inc, pop_old, epochs=100)
print(model.predict(pop_inc).flatten())

line_x=np.arange(min(pop_inc), max(pop_inc), 0.01)
line_y=model.predict(line_x)  ##yhat=ax^2 + bx +c

plt.plot(pop_inc, pop_old, 'bo', alpha=0.4)
plt.plot(line_x, line_y, 'r--')
plt.xlabel('지역별 인구증가율(%)')
plt.ylabel('고령인구비율(%)')
plt.show()