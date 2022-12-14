from scipy import stats
import pandas as pd
from numpy import average

'''
서로 독립인 두 집단의 평균 차이 검정(independent samples t-test)
독립변수는 집단이야 범주, 평균은 연속형이야 

문제1-1) 남녀 두 집단 간 파이썬 시험의 평균 차이 검정 
남녀의 성적(서로 독립인 두 집단에서 얻은 표본을 독립표본(two sample))
Male = [75, 85, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]
'''
#귀무: 남녀 두 집단 간 파이썬 시험의 평균에 차이가 없다.
#대립: 남녀 두 집단 간 파이썬 시험의 평균에 차이가 있다.

male = [75, 85, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]

print(average(male),average(female)) #83.8 #72.24
print(83.9 - 72.24) #11.66 정도의 차이가 있는데,차이가 있는가 없는가? 우연히 발생한것인가 아닌가?

two_sample=stats.ttest_ind(male,female) #등분산성 #두개의 표본에 대한 t-test실시
print(two_sample)
#statistic(검정통계량, 표본통계량)=1.233193127514512, pvalue=0.2525076844853278
#해석 : pvalue=0.2525076844853278 > 0.05 귀무가설 채택 남녀 두 집단 간 파이썬 시험의 평균에 차이가 없다.

print()
'''
서로 독립인 두 집단의 평균 차이 검정(independent samples t-test)
문제1-2) 두 가지 교육방법에 따른 평균시험 점수에 대한 검정 수행 two_sample.csv'
'''
#귀무: 두 가지 교육방법에 따른 평균시험 점수 차이는 없다.
#대립: 두 가지 교육방법에 따른 평균시험 점수 차이가 있다.

data=pd.read_csv("../testdata/two_sample.csv")
print(data)
ms=data[['method','score']] #필요한 칼럼만 꺼내자
print(ms)
#교육방법별로 집단 나누기(데이터분리)
m1=ms[ms['method']==1] #방법1번 꺼내기
m2=ms[ms['method']==2]
score1=m1['score']
score2=m2['score']
print(score1)
print(score2)
print(score1.isnull().sum()) #0
print(score2.isnull().sum()) #2 NaN 처리: 제거, 0으로 대체, 평균으로 대체

# NaN 처리: 제거:dropna(), 0으로 대체:fillna(0), 평균으로 대체:fillna(score1.mean())
sco1=score1.fillna(score1.mean())
sco2=score2.fillna(score2.mean())
print(sco1)
print(sco2)

#정규성검정
import matplotlib.pyplot as plt
import seaborn as sns

# sns.histplot(sco1,kde=True, color='r')
# sns.histplot(sco2,kde=True, color='b')
# plt.show()

print(stats.shapiro(sco1).pvalue) # 0.3679903745651245 > 0.05 정규성만족
print(stats.shapiro(sco2).pvalue) # 0.6714189648628235 > 0.05 정규성만족

#등분산성 확인 법
print(stats.levene(sco1,sco2).pvalue) #0.4568427112977609 #얘를 많이 쓰고있긴해 #데이터가 30개 이상일 때 > 0.05 등분산성만족
print(stats.fligner(sco1,sco2).pvalue) #0.44323735267062647 #데이터가 30개 이상일 때
print(stats.bartlett(sco1,sco2).pvalue) #0.26789717886602216 #비모수검정일 때 사용
#비모수: 데이터가 정규분포가 아니며 데이터의 표본 수가 적거나 부족하고 데이터가 서로 독립적인 경우

result1=stats.ttest_ind(sco1,sco2) #정규성만족 등분산성만족
print('t-value(statistic검정통계량): %.5f, p-value: %.5f'%result1)
#t-value(statistic검정통계량): -0.19649, p-value: 0.84505
#해석: p-value: 0.84505 > 0.05 귀무채택
print()
#참고
print('----------------------참고----------------------')
result1=stats.ttest_ind(sco1,sco2, equal_var=True) #정규성만족 등분산성만족
print('t-value(statistic검정통계량): %.5f, p-value: %.5f'%result1)
result1=stats.ttest_ind(sco1,sco2, equal_var=False) #정규성 만족, 등분산성 불만족
print('t-value(statistic검정통계량): %.5f, p-value: %.5f'%result1)
print()
#result2=stats.wilcoxon(sco1,sco2) #정규성을 만족하지 않을 경우
#err: ValueError: The samples x and y must have the same length.
result2=stats.mannwhitneyu(sco1,sco2) #정규성을 만족하지 않을 경우
print('t-value(statistic검정통계량): %.5f, p-value: %.5f'%result2)

