# [로지스틱 분류분석 문제3] 
#
# Kaggle.com의 https://www.kaggle.com/truesight/advertisingcsv  file을 사용

#   참여 칼럼 :
#   Daily Time Spent on Site : 사이트 이용 시간 (분)
#   Age : 나이,
#   Area Income : 지역 소독,
#   Daily Internet Usage:일별 인터넷 사용량(분),
#   Clicked Ad : 광고 클릭 여부 ( 0 : 클릭x , 1 : 클릭o )

# 광고를 클릭('Clicked on Ad')할 가능성이 높은 사용자 분류.
# ROC 커브와 AUC 출력

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
"""
df=pd.read_csv('../testdata/advertisement.csv',usecols=[0,1,2,3,9])
array=df.values
print(array)
x=array[:,0:4]
y=array[:,4]

print(array.dtype) #float64
print(type(x[0][0])) #<class 'numpy.float64'>
print(type(y[0])) #<class 'numpy.float64'>
"""

data = pd.read_csv('../testdata/advertisement.csv')
datas = data.values # <class 'numpy.ndarray'>
print(datas)
x = datas[:,0:4]
y = datas[:,9]

print(y.dtype) #object
print(type(datas))
print(type(x),type(y))
print(type(x[0][0])) #<class 'float'> #파이썬 클래스
print(type(y[0])) #<class 'int'>


print()
print(y.shape,y[0:10], type(y))
model = LogisticRegression().fit(x,y)
# y_hat = model.predict(x)
# print('예측값 :',y_hat[:3])