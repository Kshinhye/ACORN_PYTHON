#mtcars dataset으로 단순/다중회귀 모델 작성 : ols() 사용
#ols는 꼭 기억하세요ㅣ summary랑

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api
plt.rc('font',family='malgun gothic')
import seaborn as sns
import statsmodels.formula.api as smf

mtcars=statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars)

# mp :연비: 기름 1리터를 넣었을 때 얼마큼 달릴 수 있는지
# hp :마력수
# wt : 차무게

# print(mtcars.corr())
print(np.corrcoef(mtcars.hp, mtcars.mpg)[0,1]) #0행1열 #-0.7761683718265864
print(np.corrcoef(mtcars.wt, mtcars.mpg)[0,1]) #0행1열 #-0.8676593765172281
#음의 상관관계가 매우 높다

#===============================================================================
# 단순선형회귀 : mtcars.hp(feature), mtcars.mpg(label) | 마력수가 연비에 영향을 준다.
#===============================================================================
#시각화
'''
#실제값
plt.scatter(mtcars.hp,mtcars.mpg)
#참고: ols를 안쓰고 numpy의 polyfit()을 이용하면 slope, intercept를 얻을 수 있다.
slope, intercept=np.polyfit(mtcars.hp,mtcars.mpg,1)
print('slope: {}, intercept: {}'.format(slope, intercept))
#slope: -0.0682282780715636, intercept: 30.098860539622496

#모델이 예측한 값
plt.plot(mtcars.hp, slope*mtcars.hp + intercept,c='r')
plt.xlabel('마력수')
plt.ylabel('연비')
plt.show()
'''

#모델을 만들게요
result1=smf.ols('mpg ~ hp', data=mtcars).fit()
print(result1.summary())

# Prob (F-statistic):1.79e-07 < 0.05 모델은 유의하다
# R-squared:0.602 60프로 정도의 설명력을 가지고있다. 유의한 단순선형회귀 모델이 맹글어진거에요
# Skew(왜도) 0.747 데이터가 편행되어있다

print(result1.conf_int(alpha=0.05))##95%신뢰구간(confidence interval) 내 결과만 보여줌
print()
print(result1.summary().tables[1]) #위쪽만 보인다.
print('마력수 110에 대한 연비는 얼마일까요')
print('slope*x + intercept:', -0.0682 *110+30.0989)#22.5969

#===============================================================================
# 다중선형회귀 : mtcars.hp(feature),mtcars.wt(feature), mtcars.mpg(label) 
#===============================================================================
result2=smf.ols(formula='mpg ~ hp+wt',data=mtcars).fit()
print(result2.summary())
print(result2.summary().tables[1])
#독립변수 둘 다 의미가 있다.

print('마력수 110, 차체 무게 5톤에 대한 연비는',-0.0318*110 + -3.8778*5 + 37.2273) 

print('predict 함수 사용')
new_data=pd.DataFrame({'hp':[110,120,150],'wt':[5,2,7]})
new_pred=result2.predict(new_data)
print('예상연비:', new_pred.values) #[14.34309224 25.65885499  5.31651287]

#키보드로 값 받기
new_hp=float(input('새로운 마력수를 입력하이소:'))
new_wt=float(input('새로운 차체를 입력하이소:'))
new_data2=pd.DataFrame({'hp':[new_hp],'wt':[new_wt]})
new_pred2=result2.predict(new_data2)
print('새로운 예상연비:', new_pred2.values)