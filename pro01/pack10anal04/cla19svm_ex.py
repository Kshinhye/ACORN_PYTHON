'''
[SVM 분류 문제] 심장병 환자 데이터를 사용하여 분류 정확도 분석 연습
https://www.kaggle.com/zhaoyingzhu/heartcsv
https://github.com/pykwon/python/tree/master/testdata_utf8         Heartcsv

Heart 데이터는 흉부외과 환자 303명을 관찰한 데이터다. 
각 환자의 나이, 성별, 검진 정보 컬럼 13개와 마지막 AHD 칼럼에 각 환자들이 심장병이 있는지 여부가 기록되어 있다. 
dataset에 대해 학습을 위한 train과 test로 구분하고 분류 모델을 만들어, 모델 객체를 호출할 경우 정확한 확률을 확인하시오. 
임의의 값을 넣어 분류 결과를 확인하시오.
 
정확도가 예상보다 적게 나올 수 있음에 실망하지 말자. ㅎㅎ
feature 칼럼 : 문자 데이터 칼럼은 제외
label 칼럼 : AHD(중증 심장질환)

데이터 예)
"","Age","Sex","ChestPain","RestBP","Chol","Fbs","RestECG","MaxHR","ExAng","Oldpeak","Slope","Ca","Thal","AHD"
"1",63,1,"typical",145,233,1,2,150,0,2.3,3,0,"fixed","No"
"2",67,1,"asymptomatic",160,286,0,2,108,1,1.5,2,3,"normal","Yes"

'''

import pandas as pd
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing._data import StandardScaler

df=pd.read_csv("../testdata/Heart.csv")
df['Ca']=df['Ca'].fillna(df['Ca'].mean())
# print(df.head(3), df.shape) #(303, 15)
print(df.info()) #ChestPain #Thal
print(df['AHD'].unique()) #['No' 'Yes']

x=df.drop(columns=['ChestPain','Thal','AHD'],axis=1)
y=df.loc[:,'AHD']

print(x.isnull().sum())

# train/test split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.3, random_state=12)
# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(207, 12) (90, 12) (207,) (90,)

#model만들기
model=svm.SVC(C=0.1).fit(x_train,y_train)

pred=model.predict(x_test)
acc=metrics.accuracy_score(y_test, pred)
print('예측값: ',pred[:10])
print('실제값: ', y_test[:10].values)
print('정확도: ',acc) #정확도:0.56043

#새값으로 예측
new_x=[[1,63,1,145,233,1,2,150,0,2.3,3,0],[2,67,1,160,286,0,2,108,1,1.5,2,3]]
new_pred=model.predict(new_x)
print(new_pred)