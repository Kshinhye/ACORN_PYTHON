# 로지스틱 회귀분석 (Logistic Regression)
# 종속변수와 독립변수 간의 관계로 예측모델을 생성한다는 점에서 선형회귀분석과 유사하다. 하지만
# 독립변수(x)에 의해 종속변수(y)의 범주로 분류한다는 측면에서 분류분석 방법이다. 분류 문제에서 선형
# 예측에 시그모이드 함수를 적용하여 가능한 각 불연속 라벨 값에 대한 확률을 생성하는
# 모델로 이진분류 문제에 흔히 사용되지만 다중클래스 분류(다중 클래스 로지스틱 회귀 또는 다항회귀 )에도 사용될 수 있다.

# 독립변수 : 연속형  |  종속변수 : 범주형
# 뉴럴네트워크(신경망)

import math
def sigFunc(x):
    return 1/(1+math.exp(-x)) #시그모이드 함수 처리결과 반환

print(sigFunc(3)) # 인자값은 로짓 전환된 값이라 가정
print(sigFunc(1))
print(sigFunc(37.6))
print(sigFunc(-3.4))

print('---ㅡmtcars dataset으로 분류 모델 작성---')
import statsmodels.api as sm

carData=sm.datasets.get_rdataset('mtcars')
print(carData) #<class 'statsmodels.datasets.utils.Dataset'>
print(carData.keys()) #dict_keys(['data', '__doc__', 'package', 'title', 'from_cache', 'raw_data'])

#필요한것만 빼보자
carDatas=sm.datasets.get_rdataset('mtcars').data
print(carDatas.head(3))

mtcar=carDatas.loc[:,['mpg','hp','am']]
print(mtcar.head(2))
print(mtcar['am'].unique()) #[1 0] 이항분류 

# 연비와 마력수에 따른 변속기 분류 (수동, 자동)
# 모델작성1 : logit()
import statsmodels.formula.api as smf
import numpy as np
from sklearn.metrics import accuracy_score

formula='am ~ hp+mpg'
result=smf.logit(formula=formula,data=mtcar).fit()
print(result) #Iterations 9 학습 9번 반복했어
print(result.summary())
#hp / mpg 의 P>|z|는 각각 0.041 / 0.026  < 0.05 보다 작다. 이것만 봐
# print('예측값: ', result.predict())

pred=result.predict(mtcar[:10])
print('예측값: ',pred.values)
print('예측값: ',np.around(pred.values)) #np.around: 0.5 를 기준으로 0과1로 출력
print('시렞값: ',mtcar['am'][:10].values)

#빈도표를 구할게요
print()
conf_tab=result.pred_table() #confusion matrix
print(conf_tab)
print('--------분류정확도--------')
print('분류정확도: ', (16+10)/len(mtcar))
print('분류정확도: ', (conf_tab[0][0]+conf_tab[1][1])/len(mtcar))
pred2=result.predict(mtcar)
print('분류정확도: ', accuracy_score(mtcar['am'],np.around(pred2)))

print('-------------------------------')
# 모델 작성2 : glm() - 일반화된 선형모델
result2=smf.glm(formula=formula, data=mtcar, family=sm.families.Binomial()).fit()
# print(result2) #statsmodels.genmod.generalized_linear_model
# print(result2.summary())
print()
glm_pred=result2.predict(mtcar[:10])
print('glm 예측값: ', np.around(glm_pred.values))
print('glm 예측값: ', mtcar['am'][:10].values)
glm_pred2=result2.predict(mtcar)
print('glm 분류정확도: ', accuracy_score(mtcar['am'],np.around(glm_pred2)))
print('\n 새로운 값으로 분류 예측')
newdf=mtcar.iloc[:5].copy()
print(newdf)
newdf['mpg']=[50,21,30,40,50]
newdf['hp']=[100,110,130,140,150]
print(newdf)

new_pred=result2.predict(newdf)
print('분류 예측 결과: ', np.around(new_pred.values))