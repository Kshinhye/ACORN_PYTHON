#집단이 독립적이다. 두집단의 평균을 구해보자
#어느 음식점 매출자료와 날씨 자료를 활용하여 강수 여부에따른 매출액 평균의 차이를 검정해보자
#"평균의차이를검정" => ttest
#집단1: 비가 올 때 매출 집단2: 비가 오지않을 때 매출

#귀무: 강수 여부에 따라 음식점 매출액의 평균에 차이가 없다.
#대립: 강수 여부에 따라 음식점 매출액의 평균에 차이가 있다.

import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

#data.go.kr을 참조
#날짜가 int로 되어있어서 object로 형변환 필요
sales_data=pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tsales.csv", dtype={'YMD':'object'})
print(sales_data.head(3))
print(sales_data.info()) # 328 by 3

wt_data=pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tweather.csv")
print(wt_data.head(3))
print(wt_data.info()) #702 by3

#두 데이터 병합 : 날짜 사용하여 merge
#그런데 날짜의 모양이 다르다.  20190514 / 2019-05-14 (편한걸로 통일)
wt_data.tm=wt_data.tm.map(lambda x:x.replace('-','')) #wt_data.tm은 시리즈다.

#이제 합쳐보자. 날짜 맞춰서 합치기 (sales를 기준으로 할거니 left join)
print('-----------merge-----------')
frame=sales_data.merge(wt_data,how='left',left_on='YMD', right_on='tm') #left_on, right_on 같은 칼럼 없을 때 기준정해주기
print(frame.head(3))
print(frame.tail(3)) 
print(len(frame)) #328
print()
print('----가설검정: 두 집단간의 매출액의 평균 검정----')
#분석에 사용할 열만 추출
#강수량 매출액 칼럼 구하기
print(frame.columns) #['YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn', 'maxWs', 'avgWs', 'ddMes']
data=frame.iloc[:,[0,1,7,8]] #'YMD'(날짜), 'AMT'(매출액), 'maxTa'(온도), 'sumRn'(강수량)
print(data.isnull().sum()) #결측치 없음

#두 집단간의 매출의 평균을 확인해봅시다.
# print(data['sumRn']>0) #T/F반환
#칼럼을 추가해볼게욤
data['rain_yn']=(data['sumRn']>0).astype(int) #비옴1, 비안옴0
print(data.head(3))

#boxplot으로 강수 여부에 따른 매출액 시각화
sp=np.array(data.iloc[:,[1,4]]) #matrix
print(sp)
tgroup1=sp[sp[:,1]==0,0] #조건을 만족하는 0열을 가져온다. #집단1 : 비 안오는 그룹의 매출액
tgroup2=sp[sp[:,1]==1,0] #조건을 만족하는 0열을 가져온다. #집단2 : 비오는 그룹의 매출액
# plt.plot(tgroup1)
# plt.show()
# plt.plot(tgroup2)
# plt.show()
plt.boxplot([tgroup1,tgroup2], meanline=True, showmeans=True, notch=True)
plt.show()

print('평균은', np.mean(tgroup1),' ', np.mean(tgroup2)) #761040.2542372881 vs  757331.5217391305 차이는??

#정규성확인
print(stats.shapiro(tgroup1).pvalue)  #0.056049469858407974 #만족
print(stats.shapiro(tgroup2).pvalue)  #0.882739782333374

#등분산성확인
print(stats.levene(tgroup1,tgroup2).pvalue)  #0.7123452333011173 #만족
print(stats.ttest_ind(tgroup1,tgroup2,equal_var=True))
#statistic=0.10109828602924716, pvalue=0.919534587722196
#pvalue=0.919534587722196 > 0.05 이므로 귀무가설 채택 / 강수 여부에 따라 음식점 매출액의 평균에 차이가 없다.