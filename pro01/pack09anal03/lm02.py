#===============================================================================
# 방법4 : linregress를 사용 | 모델이 만들어진다.
#===============================================================================

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# iq에 따른 시험점수 예측
score_iq=pd.read_csv("../testdata/score_iq.csv")
print(score_iq.head(3))
print(score_iq.info())

print(score_iq.corr()) # 0.882220 양의 상관관계가 강하다
# 그리고 둘 다 int64로 연속형이다 문제 없네요~

x=score_iq.iq
y=score_iq.score

#피어쓴 상관계수 확인
print(np.corrcoef(x,y)[0,1]) #0.8822203446134701

# plt.scatter(x,y)
# plt.show()

#모델생성
model=stats.linregress(x, y)
print(model)
print('slope(기울기): ',model.slope)
print('intercept(절편): ',model.intercept)
print('rvalue: ', model.rvalue) #r값을 제곱하면 r-square값이 나온다.
print('pvalue: ', model.pvalue) #모델의 성능이 유의한지 아닌지 확인 유의수준 0.05보다 작으므로 유의하다.(두 변수간에 인과관계가 있다)
print('stderr(표준오차):', model.stderr)

#y_hat=0.6514309527270075 * x + -2.8564471221974657 | 모델 회귀식

plt.scatter(x,y)
plt.plot(x,model.slope*x + model.intercept, c='red')
#plt.show()

# 점수 예측 해볼게요 1
# x값 140, 125로 줘볼게요 90,75에 가깝게 나오는지 볼게요
print('점수예측: ',model.slope*140 + model.intercept) #88
print('점수예측: ',model.slope*125 + model.intercept) #78
print()
# 점수 예측 해볼게요 2
# linregress는 predict을 지원하지 않는다.
new_df=pd.DataFrame({'iq':[140,125]})  #[140,125,123,100] 미지의 x값 넣어주면됨 
print('점수예측: ', np.polyval([model.slope, model.intercept], new_df))
# 점수예측:  [[88.34388626]  [78.57242197]]
