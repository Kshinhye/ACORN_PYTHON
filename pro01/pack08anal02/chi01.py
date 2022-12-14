# 가설검정 중 카이제곱검정(교차분석)
# 범주형 하나 또는 둘

# 카이제곱분포는 데이터의 분산이 퍼져 있는 모습을 분포로 만든 것
# x² = sum((실제값 - 기대값)^2 / 기대값)
# 기대값 = 각 행의 주변합 * 각 열의 주변합 / 총합(전체 표본수)
#       (행의 합/전체표본수 × 열의합/전체 표본수) × 전체 표본수

#귀무가설: 벼락치기 공부는 합격여부와 관련이 없다.(관련이 없다 => 독립적이다.)
#대립가설: 벼락치기 공부는 합격여부와 관련이 있다.(관련이 있다. => 비독립적이다.)

import pandas as pd
data=pd.read_csv("../testdata/pass_cross.csv", encoding='euc-kr')
#print(data.head(3))
print(data.shape[0]) #행의개수
print(data.shape[1]) #열의개수
print()
print(data[(data['공부함'] == 1) & (data['합격'] == 1)].shape[0])
print(data[(data['공부함'] == 1) & (data['불합격'] == 1)].shape[0])
print()
ctab=pd.crosstab(index=data['공부안함'], columns=data['불합격'], margins=True) #margine으로 합계 구하기
ctab.columns=['합격','불합격','행의합']
ctab.index=['공부함','공부안함','열의합']
print(ctab)
# chi2 = sum((실제값 - 기대값)^2 / 기대값)
chi2=(18-15)**2/15 + (7-10)**2/10 + (12-15)**2/15 + (13-10)**2/10
print(chi2) #3.0

# 판정 방법1 : 카이제곱표를 이용
# 자유도 = (행의 개수 -1)*(열의 개수 -1) #1
# 카이제곱표를 이용해 임계값(critical value) 얻기: 3.84(카이제곱검정표)
# 판정: chi2값이 cv값 왼쪽에 있으므로 귀무가설 채택
# 즉, 벼락치기 공부는 합격여부와 관련이 없다.(관련이 없다 => 독립적이다.)

# 판정 방법2 : p-value를 이용
import scipy.stats as stats

#chi2,p,ddof,expected 인데 의미없어서 무시
chi2,p,_,_ = stats.chi2_contingency(ctab)
print('chi2: {}, ,p-value: {}'.format(chi2,p)) #chi2: 3.0, ,p-value: 0.5578254003710748
#판정: 유의확률 p-value가 0.5578254003710748(55프로) > α(유의수준 0.05) 임으로 오차 허용범위를 넘어간다. => 귀무가설 채택(대립가설 기각)
# 즉, 벼락치기 공부는 합격여부와 관련이 없다.(관련이 없다 => 독립적이다.)
# 검정에 사용된 샘플 데이터는 우연히 발생된 데이터이다. (유의하지않다)