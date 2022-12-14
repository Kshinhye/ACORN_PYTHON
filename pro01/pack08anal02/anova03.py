#어느 음식점 매출자료와 날씨 자료를 활용하여 온도(추움, 보통, 더움)에 따른 매출액 평균의 차이를 검정해보자

#귀무: 음식점 매출액의 평균은 온도에 영향이 없다.
#대립: 음식점 매출액의 평균은 온도에 영향이 있다.

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
#온도, 매출액 칼럼 구하기
print(frame.columns) #['YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn', 'maxWs', 'avgWs', 'ddMes']
data=frame.iloc[:,[0,1,7,8]] #'YMD'(날짜), 'AMT'(매출액), 'maxTa'(온도), 'sumRn'(강수량)
print(data.isnull().sum()) #결측치 없음
# print(data.head(3))

#일별 최고온도 (maxTa)를 구간설정 한 후 범주형 변수 추가 (연속형 -> 범주형)
print(data.maxTa.describe()) 

data['Ta_gubun']=pd.cut(data.maxTa,bins=[-5,8,24,37], labels=[0,1,2]) #bins[최저, , ,최고]
print(data.isnull().sum()) #결측치없음
print(data['Ta_gubun'].unique()) #[2, 1, 0] 카테고리세개

#세 그룹의 매출액으로 정규성, 등분산성확인
x1=np.array(data[data.Ta_gubun==0].AMT)
x2=np.array(data[data.Ta_gubun==1].AMT)
x3=np.array(data[data.Ta_gubun==2].AMT)
print(x1[:3])

#정규성확인 : 만족못함!!
print(stats.ks_2samp(x1,x2).pvalue) #9.28938415079017e-09 < 0.05 만족못함
print(stats.ks_2samp(x1,x3).pvalue) #1.198570472122961e-28
print(stats.ks_2samp(x3,x2).pvalue) #1.4133139103478243e-13

#등분산성확인 : 얘도 만족못함!!
print(stats.levene(x1,x2,x3).pvalue) #0.039002396565063324 < 0.05 만족못함

print('------------온도별 매출액 평균------------')
#pd.options.display.float_format = '{:.5f}'.format

spp=data.loc[:,['AMT','Ta_gubun']] #모든행의 AMT열과Ta_gubun열을 꺼낸다.
print(spp.head(2))
print(spp.groupby('Ta_gubun').mean())

print(pd.pivot_table(spp, index=['Ta_gubun'], aggfunc='mean'))
#1032362.31884  vs  818106.87023  vs  553710.93750

#===============================================================================
#anova진행
#===============================================================================
sp=np.array(spp) #spp는 df라서 np로 바꿔볼게요
print(sp[:3])
group1=sp[sp[:,1]==0,0] #sp의 모든행의 1열값이 0이면 0열을 가져온다.
group2=sp[sp[:,1]==1,0]
group3=sp[sp[:,1]==2,0]

#데이터분포 시각화
# plt.boxplot([group1,group2,group3], showmeans=True)
# plt.show()
print()
#정규성만족했을 때
print(stats.f_oneway(group1,group2,group3))
#F_onewayResult(statistic=99.1908012029983, pvalue=2.360737101089604e-34)
#해석: pvalue=2.360737101089604e-34 < 0.05 이므로 귀무기각
#음식점 매출액의 평균은 온도에 영향이 있다.

#정규성을 만족하지 않으므로 
print(stats.kruskal(group1,group2,group3))
#statistic=132.7022591443371, pvalue=1.5278142583114522e-29
#귀무기각

#등분산성을 만족하지 않으므로
#pip install pingouin
from pingouin import welch_anova
print(welch_anova(data=data, dv='AMT', between='Ta_gubun'))
# #Source ,ddof1/ddof2:자유도.  p-unc: p값
#      Source  ddof1     ddof2           F         p-unc       np2
# 0  Ta_gubun      2  189.6514  122.221242  7.907874e-35  0.379038

#===============================================================================
# 사후검정 post hoc test
#===============================================================================
#차이난다고 이대로가 끝이 아니다. 각 지역(그룹)의 평균의 차이를 알기위해 사후검정을 한다.
from statsmodels.stats.multicomp import pairwise_tukeyhsd
turkeyResult = pairwise_tukeyhsd(endog=spp.AMT, groups=spp.Ta_gubun, alpha=0.05) #알파값은 0.05 기본
print(turkeyResult)

turkeyResult.plot_simultaneous(xlabel='mean' , ylabel='group')
plt.show()