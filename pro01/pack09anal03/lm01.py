#회귀분석 (선형회귀분석)
#각각의 데이터에 대한 잔차(표준오차:예측값 - 실제값)제곱합이 최소가되는 추세선(표준회귀선)을 만들고,
#이를 통해 독립변수(x, feature) 가 종속변수(y, label, class)에 얼마나 영향을 주는지 인과관계를 분석
#독립변수: 연속형 , 종속변수: 연속형  | 두 변수는 상관관계가 있어야하고 나아가서는 인과관계가 있어야한다.
#정량적인 모델을 생성

import statsmodels
from sklearn.datasets import make_regression
import numpy as np
#sklearn 은 feature는 무조건 matrix(2차원),  label은 vector나 matrix


#방법은 그냥 내 맘대로 정한거야~ 어느 책에도 안써져있어~~ 
np.random.seed(12)

#모델 생성 맛보기
#===============================================================================
#방법1 : make_regression사용 | 모델이 만들어지지는 않아요. 실험용이에요 (선생님이 좋아하는거)
#===============================================================================

#make_regression 아주 최적화된 모델을 만들어준다. (sklearn 제공)
x,y,coef=make_regression(n_samples=50, n_features=1, bias=100, coef=True) #bias:절편, 내맘대로 쓸겡 coef:기울기 리턴할거면 T
# print(x)
# print(y)
# print(coef)

#회귀식 y=a+bx  |  y=b+wx  |  y=wx+b
y_pred=89.47430739278907*0.75314283+100
print(y_pred)

#새로운 x값(미지의값)에 대한 y값 예측 결과를 출력해볼게요
y_pred_new=89.47430739278907*33+100
print(y_pred_new)
print()


#===============================================================================
#방법2 : LinearRegression 사용 | 모델이 만들어진다.
#      지가 학습을 한다 (fit())
#===============================================================================
from sklearn.linear_model import LinearRegression

#변수값을 담아볼까요 (또만들기 귀찮으니까...)
xx=x
yy=y
model=LinearRegression() #LinearRegression 클래스객체 하나 만들었다아~
#이미 수집된 학습 데이터로 모형(선형회귀모델)을 추정: 절편과 기울기를 얻는다(내부적으로 최소 제곱법이 사용된다)
fit_model=model.fit(xx,yy) #학습해라 FIT!! 독립변수xx, 종속변수yy를 준다(얘네는 수집된 과거의 학습 데이터다)

#print(fit_model) #이러면 안나온다. 업데이트 된 이후로 이래
#API를 읽어야해!!
#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
print('기울기(slope, w):', fit_model.coef_) #회귀계수를 얻을 수 있다(w)
print('편향(bias, b):', fit_model.intercept_) #절편이라는 말 잘 안써(우리끼리 쓰는거얌), 편향이야 편향

#예측값 확인 함수로 미지의 feature에 대한 label을 예측
#print(xx[0]) #[-1.70073563]
# y_new=fit_model.predict(xx[0]) # err : 
# ValueError: Expected 2D array, got 1D array instead:
# array=[-1.70073563].
# Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.

#학습할떄 타입유지시키기 (sklearn에서는 matrix로 학습했기떄문에 matrix로 넣어준다.)
y_new=fit_model.predict(xx[[0]])
print('y_new(예측값):', y_new) #[-52.17214291]
print('실제값:', yy[0])  #-52.17214291

#새로운 x값(미지의값)에 대한 y값 예측 결과를 출력해볼게요
y_new2=fit_model.predict([[33]]) #이때도 타입 신경쓰기
print('y_new(예측값): ', y_new2)


#===============================================================================
#방법3 : ols(아노바에서도 봤음) 사용. model - 잔차제곱합(rss)를 최소화하는 가중치 벡터를 행렬미분으로 구하는 방법
#===============================================================================
import statsmodels.formula.api as smf
import pandas as pd

print(xx.shape) #(50, 1) 이차원이야~
x1=xx.flatten() # .flatten() 차원 축소
print(x1.shape) #(50,)
y1=yy #yy는 이미 일차원이기 때문에 그냥 간다

data=np.array([x1,y1]) # dataframe에 넣기위한 과정
df=pd.DataFrame(data.T)
df.columns=['x1','y1']
print(df.head(3))

model2=smf.ols(formula='y1 ~ x1', data=df).fit()
print(model2.summary())

#예측값 확인 함수를 쓸게요
print(x1[:2]) #요걸로 할게요
new_df=pd.DataFrame({'x1':[-1.70073563, -0.67794537]}) #기존 자료 사용
new_pred=model2.predict(new_df)
print('new_pred: \n', new_pred)
#가만있어보자, 실제값을 볼까요?
print('실제값: \n', df.y1[:2])
# 와우~ 똑같아요(make_regression 사용했기때문에 최적화된 모델이 나옴) 사실 좋은 데이터는 아니죠
# new_pred: 
#  0   -52.172143
# 1    39.341308
# dtype: float64
# 실제값: 
#  0   -52.172143
# 1    39.341308
# Name: y1, dtype: float64

#전혀 새로운 x값(미지의값)에 대한 예측
new_df2=pd.DataFrame({'x1':[33.0, -1.234]})
new_pred2=model2.predict(new_df2)
print('new_pred2: \n', new_pred2) #33일때는  3052 / 1.234일때는 -10을 뱉어준다.


# 지금까지는 느낌만 본거야, 다음주부터는 본격적으로 어~Uh~ 머신러닝으로 들어갈게요




