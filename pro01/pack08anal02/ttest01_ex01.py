import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#문제 의도를 잘 봐야해 놓치면 안된다.
'''
[one-sample t 검정 : 문제1]  
영사기에 사용되는 구형 백열전구의 수명은 250시간이라고 알려졌다. 
한국연구소에서 수명이 50시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명시간 관련 자료를 얻었다. 
한국연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
'''
# 귀무: 한국연구소에서 개발한 수명은 300시간이다.
# 대립: 한국연구소에서 개발한 수명은 300시간이 아니다.
one_sample1=[305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]

print(np.array(one_sample1).mean()) #289
print(stats.shapiro(one_sample1)) #pvalue=0.8208622932434082 > 0.05 정규성 만족

result1=stats.ttest_1samp(one_sample1, popmean=300)
print('result1: statistic(t-value) :{}, p-value: {}'.format(result1[0],result1[1]))
# statistic(t-value) :-1.556435658177089, p-value: 0.143606254517609
# p-value: 0.143606254517609 > 0.05 이므로 대립기각 / 한국연구소에서 개발한 수명은 300시간이다.

'''
[one-sample t 검정 : 문제2] 
국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다.
A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서 A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.
실습 파일 : one_sample.csv
참고 : time에 공백을 제거할 땐 ***.time.replace("     ", "")
'''
# 귀무: 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간이다.
# 대립: 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간이 아니다.

one_sample2=pd.read_csv("../testdata/one_sample.csv")
one_sample2=one_sample2.replace("     ", "")
# err: Could not convert {x} to numeric  (해결: object -> numeric)
data1=pd.to_numeric(one_sample2.time).dropna()
print(np.mean(data1)) #5.5568807339449515 vs 5.2

result2= stats.ttest_1samp(data1, popmean=5.2)
print(result2)
# statistic=3.9460595666462432, pvalue=0.00014166691390197087
# pvalue=0.00014166691390197087 < 0.05 이므로 귀무가설 기각
# 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간이 아니다.

'''
[one-sample t 검정 : 문제3]
https://www.price.go.kr/tprice/portal/main/main.do 에서 
메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료(엑셀)를 파일로 받아 미용 요금을 얻도록 하자. 
정부에서는 전국 평균 미용 요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오.
'''
# 귀무: 전국 평균 미용 요금이 15000원이다.
# 대립: 전국 평균 미용 요금이 15000원이 아니다.
print()
one_sample3=pd.read_excel("../testdata/미용.xls").T.dropna(axis=0).iloc[2:,] #2행 이후것들만 가져오낟.
one_sample3.columns=['미용요금']
print(one_sample3.mean()) #17367
print(np.mean(one_sample3.미용요금))

#err: 'float' object has no attribute 'sqrt' #이유: one_sample3.미용요금이 아닌 one_sample3로만 입력
result3=stats.ttest_1samp(one_sample3.미용요금, popmean=15000)
print(result3)
#statistic=4.8147100568703705, pvalue=0.0002272390122086427
print('t-value: %.6f, p-value: %.6f'%result3)
# 해석: p-value: 0.000227 < 0.05 이므로 귀무가설 기각. 전국 평균 미용 요금이 15000원이 아니다.
