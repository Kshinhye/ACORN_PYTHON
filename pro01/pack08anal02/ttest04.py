'''
* 서로 대응인 두 집단의 평균 차이 검정(paired samples t-test)
처리 이전과 처리 이후를 각각의 모집단으로 판단하여,
동일한 관찰 대상(한개의 집단)으로부터 처리 이전과 처리 이후를
1:1로 대응시킨 두 집단으로 부터의 표본을 대응표본(paired sample, 동일표본)이라고 한다.

대응인 두 집단의 평균 비교는 동일한 관찰 대상으로부터 처리 이전의 관찰과 이후의 관찰을 비교하여 영향을 미친 정도를 밝히는데 주로 사용
하고 있다. 집단 간 비교가 아니므로 등분산 검정을 할 필요가 없다.

즉, 하나의 집단에 대해 독립변수를 적용하기 전과 후의 종속변수의 수준을 측정하고, 이들의 평균 차이를 통계적으로 확인

★ 집단간의 비교가 아니므로 등분산 검정은 필요하지 않다.
  예) 광고 전후의 상품 선호도, 매출액 평균의 차이 등등
'''
import numpy as np
import scipy.stats as stats

#특정학생들을 대상으로 특강 전후의 시험점수의 쳥균에 차이가 있는지 검증
#귀무: 학생들을 대상으로 특강 전후의 시험점수 평균에 차이가 없다.
#대립: 학생들을 대상으로 특강 전후의 시험점수 평균에 차이가 있다.

np.random.seed(123)
x1=np.random.normal(75,10,100) #평균 75 표준편차 10 갯수는100
x2=np.random.normal(80,10,100) #평균 75 표준편차 10 갯수는100
print(x1)
print(x2)

print(stats.shapiro(x1)) # pvalue=0.2748860716819763 > 0.05 당연히 정규성 만족
print(stats.shapiro(x2)) # pvalue=0.1021389588713646

print(stats.ttest_rel(x1,x2))
#statistic=-3.003102708378836, pvalue=0.0033837913974620205
#해석: pvalue=0.0033837913974620205 < 0.05  귀무가설 기각. 학생들을 대상으로 특강 전후의 시험점수 평균에 차이가 있다.
#그러므로 특강 개설이 효과가 있음을 알 수 있다. 
print()
# 실습) 9명의 환자를 대상으로 한 복부 수술 전 후 몸무게 변화유무 검증
baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]
#귀무: 복부 수술 전 몸무게와 복부 수술 후 몸무게 변화는 없다.
#대립: 복부 수술 전 몸무게와 복부 수술 후 몸무게 변화는 있다.

print(np.mean(baseline),' ', np.mean(follow_up)) #78.41111111111111  vs 71.5 ??
# stats.ttest_rel(): 쌍체 검정 : 측정값 쌍 간 평균 차이가 0인지 여부를 검정하는 데 사용되는 방법
print(stats.ttest_rel(baseline, follow_up)) 
#statistic=3.6681166519351103, pvalue=0.006326650855933662
#해석: pvalue=0.0063266 < 0.05 귀무가설 기각 / 복부 수술 전 몸무게와 복부 수술 후 몸무게 변화는 있다.


