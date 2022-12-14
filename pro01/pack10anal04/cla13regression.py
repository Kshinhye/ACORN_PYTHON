# DecisionTreeRegressor, RandomForestRegressor로 정량적인 예측 모델 생성

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score

boston = load_boston()
# print(boston.keys())
# RM 방개수

dfx=pd.DataFrame(boston.data, columns=boston.feature_names)
dfy=pd.DataFrame(boston.target, columns=['MEDV'])
df=pd.concat([dfx, dfy],axis=1)
print(df.head(3))
print(df.corr())

# # 시각화
# cols=['MEDV', 'RM','LSTAT']
# sns.pairplot(df[cols])
# plt.show()

# 단순선형회귀
x=df[['LSTAT']].values
y=df['MEDV'].values
print(x[:3])
print(y[:3])

print('--DecisionTreeRegressor--')
model=DecisionTreeRegressor(criterion='mse', random_state=123).fit(x,y) #MSE(mean squared error) 평균제곱오차
# DecisionTreeRegressor 파라미터
# criterion(분할 성능 측정하는 기능 | mse, friedmen_mse, mae
# splitter(각 노드에서 분할을 선택하는 방법) | best, random
# max_depth(트리의 최대깊이)
print('예측값: ', model.predict(x)[:5])
print('실제값: ', y[:5])
print('결정계수: ', r2_score(y, model.predict(x))) #0.95900

print('--RandomForestRegressor--')
model2=RandomForestRegressor(criterion='mse', n_estimators=100, random_state=123).fit(x,y)
print('예측값: ', model2.predict(x)[:5])
print('실제값: ', y[:5])
print('결정계수: ', r2_score(y, model2.predict(x))) #0.908