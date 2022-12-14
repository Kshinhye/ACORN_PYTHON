#선형회귀분석: iris dataset으로 모델 생성
#약한 상관관계 변수, 강한 상관관계 변수로 모델을 작성해보도록 할게요

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

iris=sns.load_dataset('iris')
print(iris.head(3))
print(type(iris))
print(iris.corr()) #method는 피어쓴이야 생략해~

#약한 상관관계 먼저 해볼게요
#===============================================================================
print('-------연습1: 약한 상관관계 변수 / sepal_length ,sepal_width-------')
#===============================================================================

result1=smf.ols(formula='sepal_length ~ sepal_width', data=iris).fit()
print('요약결과1',result1.summary())
#Prob (F-statistic): 0.152 > 0.05 배렸네 배렸어
#R-squared: 0.014 이걸 어따써!!
#P>|t|  0.152 -> p값으 로써 자격이 없다

print('R-squared',result1.rsquared) #0.013822654141080748 이므로 설명력이 매우 낮다(쓸만한 녀석이 아니다)
print('p-value',result1.pvalues[1]) #0.15189826071144708 > 0.05이므로 독립변수로 유의하지 않다.
#의미없는 모델로 예측 결과 확인
print('실제값: ',iris.sepal_length[:5].values)
print('예측값: ',result1.predict()[:5])

#model1 시각화
# #실제값
# plt.scatter(iris.sepal_width,iris.sepal_length ) #sepal_width로 sepal_length 예측
# #예측값
# plt.plot(iris.sepal_width, result1.predict(),color='r')
# plt.show()

#===============================================================================
print('-------연습2: 강한 상관관계 변수 / sepal_length,petal_width-------')
#===============================================================================
result2=smf.ols(formula='sepal_length ~ petal_width', data=iris).fit()
print('요약결과2',result2.summary())

#Prob (F-statistic):  2.33e-37 < 0.05 유의해 / 독립변수로써 의미있다.
#R-squared: 0.669 66프로를 설명한다.


print('R-squared',result2.rsquared)
#R-squared 0.6690276860464136
print('p-value',result2.pvalues[1])
#p-value 2.325498079793343e-37

#의미있는 모델로 예측결과 확인
print('실제값: ',iris.sepal_length[:5].values) #[5.1 4.9 4.7 4.6 5. ]
print('예측값: ',result2.predict()[:5]) #[4.95534547 4.95534547 4.95534547 4.95534547 4.95534547]

#model2 시각화
#실제값
plt.scatter(iris.petal_width,iris.sepal_length ) #petal_width sepal_length 예측
#예측값
plt.plot(iris.petal_width, result2.predict(),color='y')
plt.show()

print('새로운 값(petal_width)로 결과 결과예측(sepal_length)')
new_data=pd.DataFrame({'petal_width':[1.1,3.3,5.5,7.7]})
y_pred=result2.predict(new_data)
print('예측결과:', y_pred.values) #[ 5.75506769  7.70994425  9.66482081 11.61969737]