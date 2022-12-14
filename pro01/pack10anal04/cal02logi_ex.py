# [로지스틱 분류분석 문제1]
# 문1] 소득 수준에 따른 외식 성향을 나타내고 있다.
# 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 
# 다음 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.
# 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라.

import pandas as pd
import statsmodels.formula.api as smf
import numpy as np
from sklearn.metrics import accuracy_score

edata=pd.read_csv("../testdata/eat_out.txt")
print(edata.shape) #(28, 3)
data=edata[((edata['요일']=='토')|(edata['요일']=='일'))]

formula='외식유무 ~ 소득수준'
# result=smf.logit(formula=formula, data=data).fit()
result=smf.glm(formula=formula, data=data).fit()
# print(result.summary()) #소득수준 0.018 < 0.05
# print(result.predict())

pred=result.predict(data)
print('예측값: ',pred.values)
print('예측값: ',np.around(pred.values))
print('실제값: ',data['외식유무'].values)

# print('-----빈도표/logic-----')
# conf_tab=result.pred_table()
# print(conf_tab)
# print('분류정확도: ', (conf_tab[0][0]+conf_tab[1][1])/len(data)) #0.9047619047619048
# pred2=result.predict(data)
# print('분류정확도: ', accuracy_score(data['외식유무'],np.around(pred2))) #0.9047619047619048
# print('-----빈도표/glm-----')
glm_pred=result.predict(data)
print('glm 분류정확도: ', accuracy_score(data['외식유무'],np.around(glm_pred))) #0.8571428571428571

print('-----새로운 예측값-----')
new_sd=int(input("새로운 소득 수준을 입력하이소: "))
if new_sd >= 0:
    new_data=pd.DataFrame({'소득수준':[new_sd]})
    new_pred=result.predict(new_data)
    new_pred=np.around(new_pred.values)
    if new_pred == 1:
        print("외식가자!!!!!!!!!!")
    elif new_pred == 0:
        print("집밥이 최고지")
else:
    print("양의 정수값만 입력해주세요")