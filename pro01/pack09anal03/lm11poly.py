# 선형회귀 모델을 다항회귀모델로 변환
# 선형 가정이 신뢰도가 떨어질 경우 대처방법으로 다항식을 추가할 수 있다.

import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([4,2,1,3,7])

print(np.corrcoef(x,y))

# plt.scatter(x,y)
# plt.show()

# 선형회귀모델 작성
from sklearn.linear_model import LinearRegression

x=x[:,np.newaxis] #모든행에 대해서 newaxis -> 차원확대
# print(x)

model=LinearRegression().fit(x,y)
ypred=model.predict(x)
print(ypred)

# plt.scatter(x,y)
# plt.plot(x,ypred,c='red')
# plt.show()

# 조금 더 복잡한 형태의 모델을 필요 : 다항식 특징(변수, feature)을 추가한 다항회귀모델을 만들 수 있다.
from sklearn.preprocessing import PolynomialFeatures

poly=PolynomialFeatures(degree=3, include_bias=False) #degree: 열의개수(늘릴수록 비선형 오버핏팅 가능성이 높아진다) include_bias: 절편값은 생각하지 않겠다
x2=poly.fit_transform(x) #특징행렬 작성
print(x2)

#다시 모델을 만들게요
#특징행렬값(x2)로 다시 학습
model=LinearRegression().fit(x2,y)
ypred2=model.predict(x2)
print(ypred2)

plt.scatter(x,y)
plt.plot(x,ypred2,c='red')
plt.show()
