'''
회귀분석 문제 2) 
testdata에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.
수학점수를 종속변수로 하자.
  - 국어 점수를 입력하면 수학 점수 예측 (단순선형회귀)
  - 국어, 영어 점수를 입력하면 수학 점수 예측 (다중선형회귀)
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

data=pd.read_csv("../testdata/student.csv")
print(data.describe())

#상관계수
print(data.corr())
#           국어        영어        수학
# 국어  1.000000  0.915188  0.766263
# 영어  0.915188  1.000000  0.809668
# 수학  0.766263  0.809668  1.000000
print(data)

print('----국어 점수를 입력하면 수학 점수 예측 (단순선형회귀)----')
#종속변수(label): 수학점수 독립변수(feature): 국어점수
#모델만들기
result1=smf.ols('수학 ~ 국어', data=data).fit()
print(result1.summary())
# Prob (F-statistic): 8.16e-05 < 0.05 이므로 유의
# R-squared:0.587 이므로 국어점수가 수학점수를 58프로 정도 설명한다.
# std err: 0.113  / 신뢰구간 0.334~0.807 사이가 아닌데ㅠㅠㅠㅠ뭐고
# 회귀식 | 0.5705*x + 32.1069

#시각화
#실제값
plt.scatter(data.국어,data.수학 )
#예측값
plt.plot(data.국어, result1.predict(),color='y')
plt.show()

print(0.5705*90+ 32.1069)
#키보드로 새로운 값(국어점수)을 입력받아 예측(수학점수)하기
new_kor=float(input('국어점수 입력: '))
new_data=pd.DataFrame({'국어':[new_kor]})
new_pred=result1.predict(new_data)
print('예상 수학점수:',new_pred.values)


print('----국어, 영어 점수를 입력하면 수학 점수 예측 (다중선형회귀)----')
#종속변수(label): 수학점수 독립변수(feature): 국어점수, 영어점수
#모델만들기
result2=smf.ols('수학 ~ 국어+영어', data=data).fit()
print(result2.summary())
# Prob (F-statistic): 0.000105 < 0.05 이므로 모델은 유의
# 국어 pvalue:0.663 | 영어 pvalue:0.074 > 0.05 데이터를 가공할 필요가 있다.
# R-squared:  0.619 이므로 61프로 정도를 설명하고 있다.
# 국어기울기:0.1158  영어: 0.5942 절편: 22.6238

#키보드로 새로운 값(국어점수,영어점수)을 입력받아 예측(수학점수)하기
new_kor=float(input('국어점수 입력: '))
new_eng=float(input('영어점수 입력: '))
new_data=pd.DataFrame({'국어':[new_kor], '영어':[new_eng]})
new_pred=result2.predict(new_data)
print('예상 수학점수:',new_pred.values)
