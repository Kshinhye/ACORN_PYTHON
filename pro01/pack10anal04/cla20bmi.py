# 체질량지수는 자신의 몸무게(kg)를 키의 제곱(m)으로 나눈 값
# 예시) 몸무게 71, 키 178
print(71/((178/100)*(178/100))) #22.4087
"""
import random
random.seed(12)

def calc_bmi(h,w):
    bmi=w/(h/100)**2
    if bmi <= 18.5: return 'thin'
    if bmi <= 25.0: return 'normal'
    else: return 'fat'

# print(calc_bmi(178,71))

fp=open('bmi.csv','w')
fp.write('height,weight,label\n')

#무작위로 데이터 생성
cnt={'thin':0, 'normal':0, 'fat':0}
for i in range(500000): #반복횟수
    h=random.randint(150, 200) #키는 150~200
    w=random.randint(35, 100) #몸무게는 35~100
    label=calc_bmi(h,w)
    cnt[label] +=1 #누적
    fp.write('{0},{1},{2}\n'.format(h,w,label))
    
fp.close()
"""

import pandas as pd
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

tbl=pd.read_csv("bmi.csv")
# print(tbl.head(3),tbl.shape)
# print(tbl.describe())

label=tbl['label']
print(label[:3])

#정규화 0~1사이로 바뀐다.
w=tbl['weight']/100 
h=tbl['height']/200
print(w[:3])
print(h[:3])

wh=pd.concat([w,h],axis=1)
print(wh[:3],wh.shape)

#label을 dummy화 (문자열을 숫자화)
label=label.map({'thin':0, 'normal':1, 'fat':2})
print(label[:3])

# train/test split
x_train, x_test, y_train, y_test=train_test_split(wh, label, test_size=0.3, random_state=1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)  #(350000, 2) (150000, 2) (350000,) (150000,)

print('---준비 끝, 출발합시다---')
#model만들기
model=svm.SVC(C=0.1).fit(x_train,y_train) #숫자가 작을수록 패널티를 많이주는것 (과적합 방지)

pred=model.predict(x_test)
# print('예측값: ',pred[:10])
# print('실제값: ', y_test[:10].values)
acc=metrics.accuracy_score(y_test, pred)
# print('acc: ',acc)
print()

#교차검증
from sklearn import model_selection
cross_vali=model_selection.cross_val_score(model, wh, label, cv=3) # cv: kfold, 몇개로 접을거니
print('각각의 검증 정확도: ', cross_vali)
print('평균 검증 정확도: ',cross_vali.mean())

#시각화
tbl2=pd.read_csv('bmi.csv', index_col=2)

def scatter_func(lbl, color):
    b=tbl2.loc[lbl]
    plt.scatter(b['weight'],b['height'],c=color, label=lbl)

scatter_func('fat', 'red')
scatter_func('normal', 'blue')
scatter_func('thin', 'yellow')
plt.legend()
plt.show()

#새값으로 예측
new_data=pd.DataFrame({'weight':[66,55],'height':[170,180]})
#정규화
new_data['weight']=new_data['weight'] / 100
new_data['height']=new_data['height'] / 200
new_pred=model.predict(new_data)
print('새로운 예측값: ', new_pred)