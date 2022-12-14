# 선형회귀 분석 모델

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api
plt.rc('font',family='malgun gothic')
import seaborn as sns
import statsmodels.formula.api as smf

# 여러 매체의 광고비에 따른 판매량(판매액) 데이터 사용
advdf=pd.read_csv("../testdata/Advertising.csv", usecols=[1,2,3,4])
print(advdf.head(3),advdf.shape) #(200,4)
print(advdf.info())

#단순선형회귀 : tv(feature), sales(label)
print('상관계수(r): ', advdf.loc[:,['tv','sales']].corr()) #모든행의 tv,와 sales를 쓸게
# 0.782224 양의 상관관계가 다소 강하다
# 인과관계인가? 확인해보자
# tv가 sales에 영향을 준다라고 가정

# 모델 생성
lm=smf.ols(formula='sales ~ tv', data=advdf).fit()
#cost가 최소가되는 모델이 만들어졌다.
print(lm.summary())

# #시각화를 한다면
# plt.scatter(advdf.tv , advdf.sales) #실제값
# plt.xlabel('TV')
# plt.ylabel('SALES')
# y_pred=lm.predict(advdf.tv) #예측값
# # print('real y:', advdf.sales.values) #실제값
# # print('y_pred: ',y_pred.values) #모델의 예측값 (회귀선 그릴 때 사용)
# plt.scatter(advdf.tv, y_pred, c='r')
# plt.show()
# plt.plot(advdf.tv, y_pred, c='r')
# plt.show()

#예측1: 새로운 tv값으로 sales를 추정
x_new=pd.DataFrame({'tv':[230.1, 44.5, 100]})
pred=lm.predict(x_new)
print('예측결과: ', pred.values)
#예측결과: [17.97077451  9.14797405  11.78625759]


print('-----'*20)
print(advdf.corr()) #tv > radio > newspaper > sales 순으로 상관관계가 강하다.
lm_mul=smf.ols(formula='sales ~ tv+radio+newspaper', data=advdf).fit()
print(lm_mul.summary())
#Prob (F-statistic): 1.58e-96어우 신뢰도가 높겠네요.
#Adj. R-squared: 0.896 89프로 설명하고있네요.
#P>|t| 0.860 > 0.05: newspaper를 제거할지 생각해봐야한다. (독립변수로서 의미가 없는게 아닐까?하는 고민을 해봐야한다.)

#예측2: 새로운 tv,radio 값으로 sales를 추정
print(advdf.corr()) #tv > radio > newspaper > sales 순으로 상관관계가 강하다.
lm_mul=smf.ols(formula='sales ~ tv+radio', data=advdf).fit()
print(lm_mul.summary())

x_new2=pd.DataFrame({'tv':[230.1, 44.5, 100],'radio':[30.0, 40.0,50.0]})
pred2=lm_mul.predict(x_new2)
print('예측결과2: ', pred2.values)
#예측결과2:  [19.08910967 12.47695825 16.89629275]

print('******'*30)
#===============================================================================
# 회귀분석모형의 적절성을 위한 조건 : 아래의 조건 위배 시에는 변수 제거나 조정을 신중히 고려해야 함.
# 1) 정규성 : 독립변수들의 잔차항이 정규분포를 따라야 한다.
# 2) 독립성 : 독립변수들 간의 값이 서로 관련성이 없어야 한다.
# 3) 선형성 : 독립변수의 변화에 따라 종속변수도 변화하나 일정한 패턴을 가지면 좋지 않다.
# 4) 등분산성 : 독립변수들의 오차(잔차)의 분산은 일정해야 한다. 특정한 패턴 없이 고르게 분포되어야 한다.
# 5) 다중공선성 : 독립변수들 간에 강한 상관관계로 인한 문제가 발생하지 않아야 한다.
#===============================================================================

#잔차항 구하기
fitted=lm_mul.predict(advdf.iloc[:,0:2])
print('fitted \n',fitted)
residual=advdf['sales'] - fitted #잔차: 표본데이터의 실제값 - 예측값
# 차이가 거의 0에 가까워야겠죠 / residual의 평균이 0에 가까워야한다.
print('residual: ', residual[:3])
print(np.mean(residual)) #3.481659405224491e-15
print(np.sum(residual)) #6.856737400084967e-13


#===============================================================================
print('3) 선형성 : 독립변수의 변화에 따라 종속변수도 변화하나 일정한 패턴을 가지면 좋지 않다.')
#===============================================================================
#예측값과 잔차가 비슷하게 유지되어야 함
sns.regplot(fitted, residual,lowess=True, line_kws={'color':'red'}) #lowless 최저모델값을 볼 수 있다.
plt.plot([fitted.min(), fitted.max()],[0,0], '--')
#x축에 예측값의 최소, 최대값, y축은 0,0 선의 모양은 파선 
plt.show()
#실선: 잔차의 추세를 나타낸다. 실선이 파선에서 크게 벗어나있다면 예측값에 따라서 잔차가 크게 달라지게된다는 뜻이다.
#그림으로 확인하니 선형성을 만족하지 못하고있다.(비선형이다) 선형성을 만족하지 못할 땐 다항회귀 추천


#===============================================================================
print('1) 정규성 : 독립변수들의 잔차항이 정규분포를 따라야 한다.') #zscore -> scatterplot
#===============================================================================
#잔차가 정규분포를 따라야한다. Q-Q plot으로 확인 가능
import scipy.stats
sr=scipy.stats.zscore(residual) #표본에 있는 각 값의 z값(확률분포값)을 계산
(x,y),_=scipy.stats.probplot(sr) #probplot 정규분포 분위수
sns.scatterplot(x,y)
plt.plot([-3,3],[-3,3],'--') #x축에 [-3,3] 사시에, y축에 [-3,3] 사이에 선을 그어보자
plt.show()
#커브를 그리고 있다는 점이 좋지는 않죠 , 표본에 있는 z값(확률분포값)을 구해가지고 probplot을 통해 x,y를 구하고 scatterplot통해 그리고 있어요
#잔차가 정규분포를 따르는지 QQ를 통해 확인해봤지만 정규성을 만족하지 못하고있다.
#이럴 때 데이터값에 log를 취하는 작업을 통해 정규 분포를 따르도록 데이터 가공 작업이 필요하다
#log를 씌우면 데이터값의 크기가 전체적으로 작아지면서 커브의 강도도 약해진다. (반드시 만족하는건 아님!)

#잔차의 정규성은 shapiro test를 통해서도 확인가능
print('shapiro: ',scipy.stats.shapiro(residual))
#pvalue=4.190036317908152e-09 < 0.05 이므로 정규성을 만족하지 못한다.

#===============================================================================
print('2) 독립성 : 독립변수들 간의 값이 서로 관련성이 없어야 한다.(잔차가 독립적이어야한다.=자기상관이 없어야한다.)')
#===============================================================================
# Durbin-Watson: 잔차의 독립성 만족여부 확인 가능 2에 근사하면 자기상관이 없다. 0<-양의 상관관계계 크다 , 2 에있는건 독립성, ->4에 가까우면 음의 상관관계가 크다
# (summary 확인한 결과) 2.081 독립성은 만족

#===============================================================================
print('4) 등분산성 : 독립변수들의 오차(잔차)의 분산은 일정해야 한다. 특정한 패턴 없이 고르게 분포되어야 한다.')
#===============================================================================
sns.regplot(fitted,np.sqrt(np.abs(sr)),lowess=True, line_kws={'color':'red'})
plt.show()
#수평에 가까워야 좋은거에요. 지금은 뚜렷하게 커브를 그리고 있어요. 그렇기때문에 등 분산성을 만족하지 못한다.
#일정한 패턴의 곡선을 그리고 있으므로 등분산성을 만족하지 못한다. 
#이런경우에 아웃라이어(이상값)을 확인해보고, 비선형인지 확인, 정규성을 확인해봐야한다.
#만약에 정규성을 만족하나 등분산성을 만족하지 못하는 경우에는 가중회귀분석을 추천

print()
#===============================================================================
print('5) 다중공선성 : 독립변수들 간에 강한 상관관계로 인한 문제가 발생하지 않아야 한다.')
#독립변수로 사용할 애들끼리는 서로 관계가 약한게 좋아요 #독립성과 관련이 있다
#===============================================================================
# VIF(분산팽창계수)를 사용해서 
# VIF가 10이 넘으면 다중공선성 있다고 판단하며 5가 넘으면 주의할 필요가 있는 것으로 봅니다
from statsmodels.stats.outliers_influence import variance_inflation_factor
# print(advdf.head(3)) #tv  radio 얘네 둘 사이에 관계는 적어야한다.
#summary()결과에서 coef순서는 intercept:0, tv:1, radio:2
print(variance_inflation_factor(advdf.values,1)) #1: index tv 12.57
print(variance_inflation_factor(advdf.values,2)) #2: index radio 3.153

#dataframe으로 한 번 꺼내서 볼까욤(그냥 이렇게도 볼 수 있음)
vifdf=pd.DataFrame()
vifdf['vif_value']=[variance_inflation_factor(advdf.values,i) for i in range(1,3)]
print(vifdf)

#참고참고~ R에서 cook's distance - 극단값(이상치)를 나타내는 지표
print("---참고: cook's distance---")
from statsmodels.stats.outliers_influence import OLSInfluence
cd,_=OLSInfluence(lm_mul).cooks_distance
print(cd.sort_values(ascending=False).head(3))
#130번째 값이 제일 크다, 그다음은 다섯번째
#이걸 시각화 해볼까요
import statsmodels.api as sm
sm.graphics.influence_plot(lm_mul, criterion='cooks')
plt.show()

print(advdf.iloc[[130,5,35,178,126]]) #이상치 데이터로 의심됨 제거 권장