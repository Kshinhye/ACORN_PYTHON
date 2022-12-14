# Kaggle.com의 https://www.kaggle.com/truesight/advertisingcsv  file을 사용
# 얘를 사용해도 됨   'testdata/advertisement.csv' 
# 참여 칼럼 : 
#   Daily Time Spent on Site : 사이트 이용 시간 (분)
#   Age : 나이,
#   Area Income : 지역 소독,
#   Daily Internet Usage:일별 인터넷 사용량(분),
#   Clicked Ad : 광고 클릭 여부 ( 0 : 클릭x , 1 : 클릭o )
# 광고를 클릭('Clicked on Ad')할 가능성이 높은 사용자 분류.
# 데이터 간의 단위가 큰 경우 표준화 작업을 시도한다.
# ROC 커브와 AUC 출력

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, roc_curve

data = pd.read_csv('../testdata/advertisement.csv')
# print(data.head(3))
# print(data.info())
x = np.array(data[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage']])
y = np.array(data['Clicked on Ad'])
print(type(x)); print(type(y)) #<class 'numpy.ndarray'>
print(type(data[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage']])) #<class 'pandas.core.frame.DataFrame'>
print(type(data['Clicked on Ad'])) #<class 'pandas.core.series.Series'>
print(type(x[0][0])) #<class 'numpy.float64'>
print(type(y[0])) #<class 'numpy.int64'>
print(y)

# import sklearn.utils
# print(sklearn.utils.multiclass.type_of_target(y)) 

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=123) 
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
print(x_train[:3])

sc = StandardScaler()
sc.fit(x_train)
sc.fit(x_test)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)
print(x_train[:3])

model = LogisticRegression(C=100.0, random_state=12).fit(x_train, y_train)
y_pred = model.predict(x_test)

print('총 갯수 : %d, 오류수: %d'%(len(y_test), (y_test != y_pred).sum()))
print('정확도 : %.3f'%accuracy_score(y_test, y_pred))

from sklearn.metrics import confusion_matrix
con_mat = confusion_matrix(y_test, y_pred, labels=[1, 0])

print(con_mat)
acc = (con_mat[0][0] + con_mat[1][1]) / len(y_test)
print('acc : ', acc)

recall = con_mat[0][0] / (con_mat[0][0] + con_mat[0][1])
fallout = con_mat[1][0] / (con_mat[1][0] + con_mat[1][1])    
print('recall : ', recall)
print('fallout : ', fallout)

fpr, tpr, _ = roc_curve(y_test, model.decision_function(x_test))

import matplotlib.pyplot as plt

plt.plot(fpr, tpr, 'o-', label='Logistic Regression')
plt.plot([0,1],[0,1], 'k--', label='classifier line')
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.legend()
plt.show()

# AUC : ROC 커브 면적
from sklearn.metrics import auc
print('auc : ', auc(fpr, tpr))
