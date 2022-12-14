# 회귀분석 문제 5) 
# Kaggle 지원 dataset으로 회귀분석 모델(LinearRegression)을 작성하시오.
# testdata 폴더 : Consumo_cerveja.csv
# Beer Consumption - Sao Paulo : 브라질 상파울루 지역 대학생 그룹파티에서 맥주 소모량 dataset
# feature : Temperatura Media (C) : 평균 기온(C)
#             Precipitacao (mm) : 강수(mm)
# label : Consumo de cerveja (litros) - 맥주 소비량(리터) 를 예측하시오
# 조건 : NaN이 있는 경우 삭제!

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics._regression import explained_variance_score
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection._split import train_test_split
""" 이란답
df = pd.read_csv("../testdata/Consumo_cerveja.csv")
print(df.head(), df.shape) #(941, 7)
print(df.info())
df_lm = df.iloc[:,[1,4,6]]
df_lm = df_lm.dropna()
df_lm.columns = ['temp', 'rain', 'beer']
print(df_lm.head(),df_lm.shape) #(365, 3)
#print(df_lm.iloc[:,0].str.replace(',','.').astype(float).values)
df_lm['temp']=df_lm.iloc[:,0].str.replace(',','.').astype(float)
df_lm['rain']=df_lm.iloc[:,1].str.replace(',','.').astype(float)

print(df_lm.head())
x= df_lm[['temp','rain']].values.reshape(-1,2)
y=df_lm['beer'].values

print('상관계수 : \n', np.corrcoef(df_lm['temp'], y)) #0.5746147
print('상관계수 : \n', np.corrcoef(df_lm['rain'], y)) #-0.1937843

print('\n-----------데이터 세트 분리')
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(292, 2) (73, 2) (292,) (73,)

print('\n모델 만들기----------------')
lmodel = LinearRegression().fit(x_train,y_train) #train data로 학습
# print('회귀계수(slope) : ', lmodel.coef_)
# print('회귀계수(intercept) : ', lmodel.intercept_) #8.76264285047758

y_pred= lmodel.predict(x_test) #test data로 예측 검정
print('예측값 : ', np.round(y_pred[:5], 3)) #[23.795 22.545 27.659 26.    18.301]
print('실제값 : ', y_test[:5]) #[20.227 19.052 32.536 28.034 21.814]

print('\n----모델 성능 확인-----')
print('MSE : ', mean_squared_error(y_test, y_pred)) #평균제곱오차 12.388
print('R2 : ', r2_score(y_test, y_pred)) #0.44970846025013145 44.97% 설명력
print('explained_variance_score(설명분산점수) : ', explained_variance_score(y_test, y_pred))
#0.46536376263674917

# 시각화
# 평균기온, 맥주 소모량 상관관계
sns.scatterplot(x[:,0], df_lm['beer'],color='blue', alpha=0.4)

plt.show()
# 강수량, 맥주 소모량 상관관계
sns.scatterplot(df_lm['rain'], df_lm['beer'],color='green', alpha=0.4)

# plt.plot(x, y=y_pred, color='red')
plt.show()

sns.scatterplot(y_test, y_pred)

plt.xlabel('실제값')
plt.ylabel('예측값')
plt.show()
""" 
#정연이 답
df = pd.read_csv('../testdata/Consumo_cerveja.csv', usecols = [1,4,6])
df['Temperatura Media (C)'] = df['Temperatura Media (C)'].str.replace(',', '.').apply(float)
df['Precipitacao (mm)'] = df['Precipitacao (mm)'].str.replace(',', '.').apply(float)
df = df.dropna(axis=0)
print(df.info())
print(df.head(3))

x = df[['Temperatura Media (C)', 'Precipitacao (mm)']]
y = df[['Consumo de cerveja (litros)']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearRegression().fit(x_train, y_train)
print(model.intercept_, model.coef_)
y_pred = model.predict(x_test)
# print('예측값 :', y_pred)
# print('실제값 :', y_test.values)

print('결정계수로 모델 성능을 확인')
print('결정계수 :', r2_score(y_test, y_pred)) # test data를 사용
print('mean_squared_error(RMSE, 평균제곱오차):{}'.format(mean_squared_error(y_test, y_pred)))
print('explained_variance_score(설명분산점수):{}'.format(explained_variance_score(y_test, y_pred)))

# 독립변수 값이기 때문에 metrix로 넣어주어야 된다.
new_pred = model.predict([[24.82, 0.0]])
print('예측 맥주 소비량은 %s입니다.'%new_pred[0][0])
