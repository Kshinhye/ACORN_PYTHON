# 정규화(regularized) 선형회귀 방법은
# 선형회귀 계수(weight)에 대한 제약 조건을 추가함으로써 모형이 과도하게 최적화되는 현상,즉 과최적화를 막는 방법이다.

# Regularized Method, Penalized Method, Contrained Least Squares 이라고도 불리운다.
# 모형이 과도하게 최적화되면 모형 계수의 크기도 과도하게 증가하는 경향이 나타난다.
# 따라서 정규화 방법에서 추가하는 제약 조건은 일반적으로 계수의 크기를 제한하는 방법이다.
# 일반적으로 다음과 같은 세가지 방법이 사용된다.

# Ridge 회귀모형 : 가중치들의 제곱합(squared sum of weights)을 최소화하는 것을 추가적인 제약 조건
# Lasso 회귀모형 : 가중치의 절대값의 합을 최소화하는 것을 추가적인 제약 조건
# Elastic Net 회귀모형 : 가중치의 절대값의 합과 제곱합을 동시에 제약 조건

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error

iris = load_iris() #sklearn으로 load하면 처음부터 matrix
print(iris)
print(iris.keys())
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df["target"] = iris.target
iris_df["target_names"] = iris.target_names[iris.target]
print(iris_df[:3])

# train dataset, test dataset으로 나누기
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(iris_df, test_size = 0.3,random_state=12)

# 회귀분석 방법 1 - LinearRegression
from sklearn.linear_model import LinearRegression
print(train_set.iloc[:, [2]])  # petal length (cm), 독립변수
print(train_set.iloc[:, [3]])  # petal width (cm), 종속변수

# 학습은 train dataset 으로 작업
model_linear = LinearRegression().fit(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])
print('slope : ', model_linear.coef_)  # 0.42259168
print('bias : ', model_linear.intercept_)  # -0.39917733

# 모델 평가는 test dataset 으로 작업
pred = model_linear.predict(test_set.iloc[:, [2]])
print('예측값 : ', np.round(pred[:5].flatten(),1))
print('실제값 : ', test_set.iloc[:, [3]][:5].values.flatten())

from sklearn.metrics import r2_score
print('r2_score(결정계수):{}'.format(r2_score(test_set.iloc[:, [3]], pred)))  # 0.93833

plt.scatter(train_set.iloc[:, [2]], train_set.iloc[:, [3]],  color='red')
plt.plot(np.array(test_set.iloc[:, [2]]), model_linear.predict(test_set.iloc[:, [2]]))
plt.show()

print('\nRidge -----------')
# 오버핏팅일 가능성이 높은데? 그럼 릿지를 돌려보는거에요
# 회귀분석 방법 - Ridge: alpha값을 조정(가중치 제곱합을 최소화)하여 과대/과소적합을 피한다. 다중공선성 문제 처리에 효과적.
from sklearn.linear_model import Ridge
model_ridge = Ridge(alpha=10).fit(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])

#점수
print(model_ridge.score(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]]))  # 0.91880
print(model_ridge.score(X=test_set.iloc[:, [2]], y=test_set.iloc[:, [3]]))    # 0.94101
pred_ridge = model_ridge.predict(test_set.iloc[:, [2]])
print('ridge predict : ', pred_ridge[:5])
print('r2_score(결정계수):{}'.format(r2_score(test_set.iloc[:,[3]], pred_ridge)))

plt.scatter(train_set.iloc[:, [2]], train_set.iloc[:, [3]],  color='blue')
plt.plot(np.array(test_set.iloc[:, [2]]), model_linear.predict(test_set.iloc[:, [2]]))
plt.show()

print('\nLasso -----------')

# 회귀분석 방법 - Lasso: alpha값을 조정(가중치 절대값의 합을 최소화)하여 과대/과소적합을 피한다.
from sklearn.linear_model import Lasso
model_lasso = Lasso(alpha=0.1).fit(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])

#점수
print(model_lasso.score(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])) # 0.913863
print(model_lasso.score(X=test_set.iloc[:, [2]], y=test_set.iloc[:, [3]]))   # 0.940663
pred_lasso = model_lasso.predict(test_set.iloc[:, [2]])
print('lasso predict : ', pred_lasso[:5])
print('r2_score(결정계수):{}'.format(r2_score(test_set.iloc[:,[3]], pred_lasso)))

plt.scatter(train_set.iloc[:, [2]], train_set.iloc[:, [3]],  color='green')
plt.plot(np.array(test_set.iloc[:, [2]]), model_lasso.predict(test_set.iloc[:, [2]]))
plt.show()

# 회귀분석 방법 4 - Elastic Net 회귀모형 : Ridge + Lasso의 형태로 가중치 절대값의 합(L1)과 제곱합(L2)을 동시에 제약 조건으로 가지는 모형
print('\nLasso -----------')

# 회귀분석 방법 - ElasticNet: alpha값을 조정(가중치 절대값의 합을 최소화)하여 과대/과소적합을 피한다.
from sklearn.linear_model import ElasticNet
model_elastic = ElasticNet(alpha=0.1).fit(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])

#점수
print(model_elastic.score(X=train_set.iloc[:, [2]], y=train_set.iloc[:, [3]])) # 0.913863
print(model_elastic.score(X=test_set.iloc[:, [2]], y=test_set.iloc[:, [3]]))   # 0.940663
pred_elastic = model_elastic.predict(test_set.iloc[:, [2]])
print('ElasticNet predict : ', pred_elastic[:5])
print('r2_score(결정계수):{}'.format(r2_score(test_set.iloc[:,[3]], pred_elastic)))

plt.scatter(train_set.iloc[:, [2]], train_set.iloc[:, [3]],  color='cyan')
plt.plot(np.array(test_set.iloc[:, [2]]), model_elastic.predict(test_set.iloc[:, [2]]))
plt.show()
