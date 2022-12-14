"""
회귀분석 문제 3) 
kaggle.com에서 carseats.csv 파일을 다운 받아 (https://github.com/pykwon 에도 있음)
Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.
변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
회귀분석모형의 적절성을 위한 조건도 체크하시오.
완성된 모델로 Sales를 예측."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api
plt.rc('font',family='malgun gothic')
import seaborn as sns
import statsmodels.formula.api as smf

df=pd.read_csv("../testdata/carseats.csv")
print(df.head(3))
print(df.info()) #6,9,10 번째는 object라 떠나보낼게요
df=df.drop([df.columns[6],df.columns[9],df.columns[10]], axis=1)
print(df.info())

print(df.corr()) #상관관계 확인 후 높은녀석들을 최대한 선택
lm=smf.ols(formula='Sales ~ Income + Advertising + Price + Age',data=df ).fit() #타당한 변수만 임의적으로 선택
print('요약결과: \n',lm.summary()) #ols가 지원하는 summary() 그래서 꼭 기억해둬요~
# 넣어보고 P>|t| 가 0.05 보다 크면 빼~
# CompPrice 독립변수로써 의미는 있지만 상관계수가 너무 작다. 그렇기때문에 뺴는게 낫지않을까 해요(정답은아님)
# Prob (F-statistic):1.33e-38 < 0.05 모델은 유의하다
# 종속변수가 Salses를 Adj. R-squared:36.4프로정도 설명하고 있다.

df_lm=df.iloc[:,[0,2,3,5,6]] #모든행의  [0,2,3,5,6]열
print(df_lm.head(3))

#여기서 이런 생각을 함 해보자고~
#모델저장
#정다정은 모르고 윤현성은 꽉잡고 있어 잘 알아, 그래서 만들어서 다정이한테 줄거야. 그 때 소스까지 주는게 아니라 그 모델만 주믄된다
#(파이썬에서 객체를 별도의 파일로 저장할 때 피클 썼던 것 처럼)
#딥러닝 텐서플로우가면 또 방법 달라져요 그때 다시 배울거에요~
import joblib
joblib.dump(lm,'yhs.model') #파일이름 yhs.model 윤현성은 모델이다.
del lm #지우고 보려면 없음 
# print(lm.summary()) #err: NameError: name 'lm' is not defined

print('---지금부터는 저장된 모델을 읽어서 사용---')
lm=joblib.load('yhs.model')
# print(lm.summary())

print('---회귀분석모형의 적절성 확인 작업을 해봅시다---')
#이작업은 윤현성이 다 하는거야 작업까지 다 끝나고 직원들한테 나눠줘요 그럼 직원들은 predict만 하믄됩니다.
#잔차 먼저 얻어줄게요
fitted=lm.predict(df_lm) #이얏 예측값을 얻겠지
residual=df_lm['Sales']-fitted #잔차
print(residual.head(3))
print('잔차의 평균:', np.mean(residual)) #잔차의 평균: -1.1102230246251565e-14

print('---선형성---')
sns.regplot(fitted,residual,lowess=True, line_kws={'color':'red'})
plt.plot([fitted.min(),fitted.max()],[0,0],'--',color='blue')
plt.show()
#잔차가 일정하게 분포되어있으므로 선형성 만족
print('---정규성---')
import scipy.stats as stats
sr=stats.zscore(residual)
(x,y),_=stats.probplot(sr)
sns.scatterplot(x,y)
plt.plot([-3,3],[-3,3],'--',color='yellow')
plt.show()
#찰-싹! 붙어있죠. 잔차항이 정규분포를 따름
#shapiro도 볼 수 있다. 0.05보다 커야해요
print('shapito test: ',stats.shapiro(residual))
#shapito test:  ShapiroResult(statistic=0.994922399520874, pvalue=0.2127407342195511)
#pvalue=0.2127407342195511 얘만 관심있다. > 0.05 정규성만족

print('---독립성---')
#Durbin-Watson:   1.931

print('---등분산성---')
#오차들의 분산은 일정해야해
sr=stats.zscore(residual)
sns.regplot(fitted,np.sqrt(abs(sr)),lowess=True, line_kws={'color':'red'})
plt.show()
#평펴엉~합니다 등분산성 만족이에요
#평균선을 기준으로 일정한 패턴을 보이지 않아 등분산성 만족이야

print('---다중공선성---')
from statsmodels.stats.outliers_influence import variance_inflation_factor
df2=df[['Income','Advertising','Price','Age']]
print(df2.head(2))
print(df2.shape) #(400, 4)
#분산팽창계수를 사용하도록 할게요
vifdf=pd.DataFrame()
vifdf['vif_value']=[variance_inflation_factor(df2.values,i) for i in range(df2.shape[1])]
print(vifdf)
#모든 변수가 10을 넘기지 않음, 다중공선성이 발생하지 않음(다중공선성 우려 없음)

#완성된 모델로 새로운 독립변수의 값을 주고 Sales를 예측
new_df=pd.DataFrame({'Income':[33,55,66],'Advertising':[10,13,16],
                     'Price':[100,120,140],'Age':[30,35,40]})
pred=lm.predict(new_df)
print('Sales에 대한 예측결과: \n',pred)