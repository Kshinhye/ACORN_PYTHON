'''
* 서로 독립인 세 집단의 평균 차이 검정
세 개 이상의 모집단에 대한 가설검정 – 분산분석

‘분산분석’이라는 용어는 분산이 발생한 과정을 분석하여
요인에 의한 분산과 요인을 통해 나누어진 각 집단 내의 분산으로 나누고
요인에 의한 분산이 의미 있는 크기를 크기를 가지는지를 검정하는 것을 의미한다.

세 집단 이상의 평균비교에서는 독립인 두 집단의 평균 비교를 반복하여 실시할 경우에 제1종 오류가 증가하게 되어 문제가 발생한다.
이를 해결하기 위해 Fisher가 개발한 분산분석(ANOVA, ANalysis Of Variance,F분포)을 이용하게 된다.
'''

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import ylabel
#여기서는 회귀분석을 슬쩍 꺼내볼게요
#R에서도 회귀분석할 때 ANOVA를 슬쩍 꺼냈었어요

#실습) 세 가지 교육방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로 실기시험을 실시. three_sample.csv'

#교육방법이 한개의 요인이다. 요인내의 3가지 방법(레벨)으로 나눠진다(즉, 세개의 집단이 된다)
#귀무: 세가지 교육방법에 따른 시험점수에 차이가 없다.
#대립: 세가지 교육방법에 따른 시험점수에 차이가 있다.
#===============================================================================
# 가설검정
#===============================================================================

data=pd.read_csv("../testdata/three_sample.csv")
print(data.head(3))
print(data.shape) #(80, 4)
print(data.describe()) #결측치 없다, 메소드는 1,2,3 있고 score보니까 500 아웃라이어가 보이네요

# #이상치(아웃라이어) 확인
# plt.boxplot(data.score) #방법1
# # plt.hist(data.score) #방법2
# plt.show() #위에 동그라미 두개 / 오른쪽 두개가 떨어져있는 두개가 이상치인걸 알 수 있다.

#이상치(아웃라이어)제거
data=data.query('score <= 100') #query(조건) : score값이 100이하
print(data.shape) #(78, 4) 이상치 2개 제거완료

#정규성확인 전에 두개 떼내야겠네
result=data[['method','score']]
m1=result[result['method']==1]
m2=result[result['method']==2]
m3=result[result['method']==3]

score1=m1['score']
score2=m2['score']
score3=m3['score']

print('평균',np.mean(score1),' ',np.mean(score2),' ',np.mean(score3))
#평균 67.384   68.357   68.875

#===============================================================================
#정규성확인 (만족한다면 ANOVA 검증 킵고잉)
#만약에 정규성을 만족하지 않으면 kruskal_wallis test를 사용한다.
#=============================================================================== 

#방법1 : 한개의 표본이 같은 분포를 따르는지 확인
print(stats.shapiro(score1).pvalue) #0.1746741086244583 > 0.05 만족
print(stats.shapiro(score2).pvalue) #0.33189886808395386 > 0.05 만족
print(stats.shapiro(score3).pvalue) #0.1155870258808136 > 0.05 만족
#방법2 : 두개의 표본이 같은 분포를 따르는지 확인
print(stats.ks_2samp(score1, score2).pvalue) #0.3096879629846001
print(stats.ks_2samp(score2, score3).pvalue) #0.7724081666033108
print(stats.ks_2samp(score1, score3).pvalue) #0.7162094473752455
print()

#===============================================================================
#등분산성확인
#===============================================================================
#참고, 등분산성을 만족하지 않는 경우의 대안: 데이터를 정규화, 표준화, 자연 log를 붙이기.
#만약에 등분산성을 만족하지 않으면 welchi_anova test 사용
#모수검정할 때 주로 쓴다.
print(stats.levene(score1,score2,score3).pvalue) #0.11322850654055751 > 0.05 등분산성 만족
#print(stats.fligner(score1,score2,score3).pvalue) #0.10847180733221087
#비모수검정(참고)
#print(stats.bartlett(score1,score2,score3).pvalue)

#바로 ANOVA들어가지말고 하나 보고 갈게요
print('교육방법별 건수 : 교차표')
data2=pd.crosstab(index=data['method'],columns='count')
data2.index=['방법1','방법2','방법3']
print(data2)

print('교육방법별 만족여부 : 교차표')
data3=pd.crosstab(data.method,data.survey)
data3.index=['방법1','방법2','방법3']
data3.columns=['만족','불만족']
print(data3)

#===============================================================================
#이제 ANOVA를 진행할게요
#===============================================================================
#선형회귀 임포트
import statsmodels.api as sm
print('-----------')
# 독립변수 한개, 종속변수 한개

#학습시켜볼게요. 학습후에는 lm(리니어모델)(reg)이 만들어집니다.
#score 종속 method 독립
reg = ols('score ~ method', data=data).fit()
table=sm.stats.anova_lm(reg,type=1) #type 1,2,3 뱉어주는 형태만 조금 다르다. 
print(table) #분산분석표 출력
#분산분석표를 읽을 수 있어야해요
#Residual 잔차 df 자유도 /  sum_sq 제곱합 / mean_sq 평균 / PR(>F) F값을 이용해 P값을 구한것
#F값은 : 집단간분산(Between/전체평균으로부터 각 그룹의 평균사이) / 집단내분산(Within/그룹내의분산 )
#27.980888(분자) / 228.922822(분모) =print(27.980888/228.922822) #0.12222847750845917

#해석: P-value가 0.727597 > 0.05 이므로 귀무 채택
print('----참고----')
# (참고 정말 참고) 독립변수 두개, 종속변수 하나 / 이런식으로도 할 수 있다.
reg2 = ols('score ~ C(method + survey)', data=data).fit()
table2=sm.stats.anova_lm(reg2,type=2)
print(table2) #분산분석표 출력
print()
print('''---사후검정: post hoc test
그룹전체 평균의 차이여부를 알려주나
각 그룹 사이 평균의 차이는 알려주지 않는다.
그래서 사후검정이 필요하다.---''')
from statsmodels.stats.multicomp import pairwise_tukeyhsd
turkeyResult = pairwise_tukeyhsd(endog=data.score, groups=data.method) #알파값은 0.05 기본
print(turkeyResult)
# 차이가 크지 않아서  reject에서 False가 나온다. (True는 유의미)
# meandiff (평균차이)  p-adj(수정된값)

#차트로 그려보자(시각화)
turkeyResult.plot_simultaneous(xlabel='mean',ylabel='group')
plt.show() #평균의 차이가 없으면 그래프가 겹친다 (reject이 Ture면 겹치지 않는다)
