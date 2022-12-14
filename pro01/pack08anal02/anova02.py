#===============================================================================
# 일원분산분석으로 평균차이검정하기
# 일원분산분석: 한개의 요인에 따른 여러개의 집단으로 데이터가 구성
#===============================================================================
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib.pyplot import ylabel
from statsmodels.stats.anova import anova_lm
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import urllib.request

#===============================================================================
# 가설검정
#===============================================================================
#강남구에있는 GS편의점 3개지역 알바생의 급여에 대한 평균차이 검정을 실시
#귀무: 강남구에있는 GS편의점 알바생의 급여에 대한 평균은 차이가 없다.
#대립: 강남구에있는 GS편의점 알바생의 급여에 대한 평균은 차이가 있다.

url="https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3.txt"
#방법1 : pandas #dataFrame으로 떨어진다.
# data1=pd.read_csv(url,header=None) #txt 파일이지만 , 로 구분되어있어서 csv로 읽어왔다.
# print(type(data1))
# print(data1.describe()) #이상치, 결측치 확인
# data1=data1.values
# print(data1[:3,],type(data1))

#방법2 : numpy #metrix로 떨어진다.
data=np.genfromtxt(urllib.request.urlopen(url), delimiter=',')
#print(data)
#print(type(data)) #<class 'numpy.ndarray'>

#세 지역의 급여 평균 확인
gr1=data[data[:,1]==1, 0]
gr2=data[data[:,1]==2, 0]
gr3=data[data[:,1]==3, 0]
#이 세 집단의 평균이 차이가 있는가??
print('gr1: ',np.mean(gr1)) # 316.6
print('gr2: ',np.mean(gr2)) # 256.4
print('gr3: ',np.mean(gr3)) # 278.0

#===============================================================================
#정규성확인
#===============================================================================
print(stats.shapiro(gr1).pvalue) #0.3336853086948395 > 0.05 정규성만족
print(stats.shapiro(gr2).pvalue) #0.6561065912246704
print(stats.shapiro(gr3).pvalue) #0.832481324672699

#===============================================================================
#등분산성확인
#===============================================================================
print(stats.levene(gr1,gr2,gr3).pvalue)
#0.045846812634186246 < 0.05 등분산성 불만족 / 하지만 이정도면 그냥 만족했다고 보고 진행해도 됩니다.(웰치_아노바도 사용가능)
#print(stats.bartlett(gr1,gr2,gr3).pvalue) #표본수가 적은경우  #비모수검정 #0.3508032640105389

# 데이터의 퍼짐 정도 시각화
# plt.boxplot([gr1,gr2,gr3],showmeans=True)
# plt.show()

#===============================================================================
# 일원분산분석 방법1 : anova_lm()
#===============================================================================

df=pd.DataFrame(data,columns=['pay','group']) #위에 np로 뺐기때문에 다시 df로 바꿨다.
# print(df.head(3))
#ols(최소자승법): 선형회귀 모델을 만듬
#파이썬에서 그룹이 범주형일 때 C() 둘러줘야한다.
lmodel=ols('pay ~ C(group)', data=df).fit() #학습해라= 최적의 모델을 만들어라.
print(anova_lm(lmodel,type=1))
# 해석: p-value  0.043589 < 0.05 이므로 귀무 기각 대립채택
print()
#===============================================================================
# 일원분산분석 방법2 : f_oneway()
#===============================================================================
f_sta, pvalue=stats.f_oneway(gr1,gr2,gr3)
print('f통계량: ', f_sta)  #3.7113
print('유의확률값: ', pvalue) #0.043589
#통계표 찾아서 cv 보고 찾으면 됨

#===============================================================================
# 사후검정 post hoc test
#===============================================================================
#차이난다고 이대로가 끝이 아니다. 각 지역(그룹)의 평균의 차이를 알기위해 사후검정을 한다.
turkeyResult = pairwise_tukeyhsd(endog=df.pay, groups=df.group) #알파값은 0.05 기본
print(turkeyResult)
# 차이가 크지 않아서  reject에서 False가 나온다. (True는 유의미)
# meandiff (평균차이)  p-adj(수정된값)

#차트로 그려보자(시각화)
turkeyResult.plot_simultaneous(xlabel='mean',ylabel='group')
plt.show()
#그룹1과 2는 차이가 매우 크다 (True)