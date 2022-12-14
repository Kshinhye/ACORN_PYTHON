'''
참고 : 70년대 미국 보스턴 시의 주택가격을 설명한 dataset

회귀분석의 한 예로 scikit-learn 패키지에서 제공하는 주택가격을 예측하는 Dataset을 사용할 수 있다. 
이는 범죄율, 공기 오염도 등의 주거 환경 정보 등을 사용하여 70년대 미국 보스턴 시의 주택가격을 표시하고 있다.

* 데이터 세트 특성 :
    : 인스턴스 수 : 506
    : 속성의 수 : 13 개의 숫자 / 범주 적 예측
    : 중간 값 (속성 14)은 대개 대상입니다
    : 속성 정보 (순서대로) :

CRIM   자치시(town) 별 1인당 범죄율
ZN 25,000   평방피트를 초과하는 거주지역의 비율
INDUS   비소매상업지역이 점유하고 있는 토지의 비율
CHAS   찰스강에 대한 더미변수(강의 경계에 위치한 경우는 1, 아니면 0)
NOX   10ppm 당 농축 일산화질소
RM   주택 1가구당 평균 방의 개수
AGE   1940년 이전에 건축된 소유주택의 비율
DIS   5개의 보스턴 직업센터까지의 접근성 지수
RAD   방사형 도로까지의 접근성 지수
TAX   10,000 달러 당 재산세율
PTRATIO   자치시(town)별 학생/교사 비율
B   1000(Bk-0.63)^2, 여기서 Bk는 자치시별 흑인의 비율을 말함.
LSTAT   모집단의 하위계층의 비율(%)
MEDV   본인 소유의 주택가격(중앙값) (단위: $1,000)

'''

#회귀분석: 선형회귀, 다항회귀
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic')

df=pd.read_csv("../testdata/housing.data", header=None, sep="\s+")
# print(df)
df.columns=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
print(df.head(3),df.shape) #(506, 14)

print(df.corr()) #집값 MEDV
#LSTAT 와 상관관계가 높으니까 얘를 제물로 삼을게요

#꺼내볼게요
x=df[['LSTAT']].values
print(x[:3])
y=df['MEDV'].values
print(y[:3])

model=LinearRegression()
#===============================================================================
# 단순회귀
#===============================================================================
model.fit(x,y)

x_fit=np.arange(x.min(), x.max(), 1)[:,np.newaxis] #차원은1 모든행의, np.newaxis
y_lin_fit=model.predict(x_fit)#이걸만든이유는 그래프에 써먹어보려고 하는 것 뿐이야
# print(y_lin_fit)

model_r2=r2_score(y,model.predict(x))
print(model_r2) #0.5441462975864799

#===============================================================================
# 다항회귀
#===============================================================================
quad=PolynomialFeatures(degree=2)
cubic=PolynomialFeatures(degree=3)
x_quad=quad.fit_transform(x)
x_cubic=cubic.fit_transform(x)

#degree=2
model.fit(x_quad,y)
y_quad_fit=model.predict(quad.fit_transform(x_fit))

q_r2=r2_score(y,model.predict(x_quad))
print(q_r2) 

#degree=2
model.fit(x_cubic,y)
y_cubic_fit=model.predict(cubic.fit_transform(x_fit))

c_r2=r2_score(y,model.predict(x_cubic))
print(c_r2) 

#시각화
plt.scatter(x,y,c='lightgray', label='학습 데이터')
#단순회귀
plt.plot(x_fit, y_lin_fit, linestyle=':',label='linear fit(d=1), $R^2=%.2f$'%model_r2, c='blue',lw=2)
#다중회귀
plt.plot(x_fit, y_quad_fit, linestyle='-',label='quad fit(d=2), $R^2=%.2f$'%q_r2, c='r',lw=2)
plt.plot(x_fit, y_cubic_fit, linestyle='-',label='cubic fit(d=3), $R^2=%.2f$'%c_r2, c='k',lw=2)
plt.xlabel('하위계층비율')
plt.ylabel('주택값')
plt.legend()
plt.show()
