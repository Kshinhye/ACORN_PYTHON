# 날씨정보 데이터로 이항분류를 한 번 해볼게요 : 비가올까?

import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split #과적합방지 목적

data=pd.read_csv("../testdata/weather.csv")
print(data.head(3), data.shape) #(366, 12)
#필요없는 데이터는 빼기
data2=pd.DataFrame()
data2=data.drop(['Date','RainToday'],axis=1)
print(data2.head(3), data2.shape) #(366, 10)

#YES는 1 NO는 2로 바꾼다.
#Binomial에서는 꼭 바꿔줘야해요
data2['RainTomorrow']=data2['RainTomorrow'].map({'Yes':1,'No':0}) #Dummy
print(data2['RainTomorrow'].unique()) #[1 0]

# RainTomorrow : 종속변수, 그 외는 독립변수(feature)

# train/test split == 7:3
train, test=train_test_split(data2, test_size=0.3, random_state=42) #random_state 난수고정
print(train.shape, test.shape) #(256, 10) (110, 10)

#모델은 만들어봅시다
col_select="+".join(train.columns.difference(['RainTomorrow']))
my_formula='RainTomorrow ~' + col_select
print(my_formula)

# model=smf.glm(formula=my_formula,data=train, family=sm.families.Binomial()).fit()  #내부적으로 최소제곱법 사용
# glm은 pred_table()이 안됨
model=smf.logit(formula=my_formula,data=train, family=sm.families.Binomial()).fit()  #내부적으로 최소제곱법 사용

print(model.summary())
# print(model.params) #계수값들만 쫘악 뽑아볼 수 있다.

print('예측값: ',np.around(model.predict(test)[:10].values))
print('예측값: ',np.rint(model.predict(test)[:20].values))

print('실제값: ',test['RainTomorrow'][:20].values)
#어우 정확해보이는데??? 정확도를 확인해볼까?
conf_mat=model.pred_table()
#err: AttributeError: 'GLMResults' object has no attribute 'pred_table'
#.pred_table()은 logit만 가능 glm은 사용불가
print('conf_mat: \n',conf_mat)
print('분류 정확도: ',(conf_mat[0][0] + conf_mat[1][1])/len(train))
pred=model.predict(test)
print('분류 정확도: ', accuracy_score(test['RainTomorrow'],np.around(pred)))


# 여기서 여러분들이 기억할 것은 
# 머신러닝의 포용성(inclusion, tolerance)
# 통계 및 추론 모델을 가지고 새로운 값을 예측(정량적일수도 있고, 정성적일 수도 있다)
# ex) y=w*2 + 0 수학에서는 100%의 답을 원함
# 통계에서는 4의 주변값이 나오도록 학습을 한다.(4가 나오지 않도록한다, 4가 나오면 오버피팅이다.)

# 예를 들어 개 이미지는 분류를 하는 경우 꼬리가 없는 개도 정확하게 분류되도록 하는것이 머신러닝의 목적
# 포용성이 있는 모델이라 함은 데이터 분류 인식률이 80%, 90% 등이 되는것이 100%인 경우보다 더 효과적인다.