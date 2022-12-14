# LinearRegression으로 선형회귀 모델을 작성 / mtcars dataset 사용

import statsmodels.api
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error

mtcars=statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars.head(3))
#데이터가 적으니 train/test split은 안할게요
print(mtcars.corr(method="pearson")) #method="pearson" 기본값 안써도됨

#hp가 mpg에 영향을 준다.라는 가정하에 모델을 생성 #r:-0.776168
x=mtcars[['hp']].values #(dataframe에서 배열로 꺼냈따.) 반환값이 matrix type
print(x[:5])
y=mtcars['mpg'].values # 반환값이 vector type
print(y[:5])

# plt.scatter(x,y)
# plt.show()

lmodel=LinearRegression().fit(x,y)
print('회귀계수(slope): ', lmodel.coef_)
print('회귀계수(intercept): ', lmodel.intercept_)

pred=lmodel.predict(x)
print('예측값: ',np.round(pred[:5],1))
print('실제값: ',y[:5])
# 모델 성능 확인 (절대적이 아니라 참조할 뿐)
print('MSE: ',mean_squared_error(y, pred)) #13.989822298268805
print('R2(설명력): ',r2_score(y,pred)) #0.602437341423934 60프로의 설명력을 가지고 있다

#새로운 hp 데이터로 mpg 예측 (연속형연속형)
new_hp=[[110]]
new_pred=lmodel.predict(new_hp)
print('%s 마력인경우 연비는 %s입니다.'%(new_hp[0][0],new_pred[0]))