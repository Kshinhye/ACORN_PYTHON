#이항검정(binom test) : 결과가 두가지 값을 가지는 확률변수의 분포(이항분포)를 판단하는데 효과적
#정규분포는 연속변량인데에 반해 이항분포는 이산변량

#binom test(이항검정)

import pandas as pd
import scipy.stats as stats

#귀무: 직원을 대상으로 고객대응 교육 후 고객안내 서비스 만족율은 80%이다.
#대립: 직원을 대상으로 고객대응 교육 후 고객안내 서비스 만족율은 80%가 아니다.

data=pd.read_csv("../testdata/one_sample.csv")
# print(data.head(3))

# print(data['survey'].unique()) #[1 0]  #data.survey.unique()

ctab=pd.crosstab(index=data['survey'], columns='count')
ctab.index=['불만족','만족']
print(ctab) #불만족 14, 만족 136

print('\n-----양측검정: 방향성이 없다-----')
#성공확률기준 (만족률기준)
x=stats.binom_test([136,14],p=0.8, alternative='two-sided') #[성공, 실패]
print(x) 
#해석: p-value: 0.0006734701362867024 < 0.05 귀무기각 / 교육 후 고객안내 서비스 만족율은 80%가 아니다. 차이가있다
print()
#실패확률기준 (불만족률기준)
x=stats.binom_test([14,136],p=0.2, alternative='two-sided') #[실패, 성공]
print(x) # 0.0006734701362867063 p-value는 비슷하다 가설검정에 큰 영향을 미치지는 않는다.

print('\n-----단측검정: 방향성이 있다 (크다, 작다)-----')
#만족값이 80%보다 클 것이라고 가정하고 alternative='greater'
x=stats.binom_test([136,14],p=0.8, alternative='greater') #[성공, 실패]
print(x) 
# 해석 : 0.00031794019219854805 < 0.05 귀무기각
print()
#불만족값이 80%보다 작을 것이라고 가정하고 alternative='less'
x=stats.binom_test([14,136],p=0.2, alternative='less') #[실패, 성공]
print(x) #0.00031794019219854924