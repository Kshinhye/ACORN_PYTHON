'''
[로지스틱 분류분석 문제3]
Kaggle.com의 https://www.kaggle.com/truesight/advertisingcsv  file을 사용
  참여 칼럼 : 
  Daily Time Spent on Site : 사이트 이용 시간 (분)
  Age : 나이,
  Area Income : 지역 소독,
  Daily Internet Usage:일별 인터넷 사용량(분),
  Clicked on Ad : 광고 클릭 여부 ( 0 : 클릭x , 1 : 클릭o )
광고를 클릭('Clicked on Ad')할 가능성이 높은 사용자 분류.
ROC 커브와 AUC 출력
'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler 
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn import metrics

adata=pd.read_csv("../testdata/advertisement.csv")
data=adata.loc[:,['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage','Clicked on Ad']]

array=data.values
x=array[:,0:4]
y=array[:,4]
print(x.shape, y.shape) #(1000, 4) (1000,)
print(y,type(y)) #<class 'numpy.ndarray'>
x_train, x_test, y_train, y_test=model_selection.train_test_split(x,y,test_size=0.3,random_state=123)
print(x_train.shape, x_test.shape) #(700, 4) (300, 4)

# 표준화
sc=StandardScaler()
sc.fit(x_train); sc.fit(x_test)
x_train=sc.transform(x_train)
x_test=sc.transform(x_test)

model=LogisticRegression().fit(x_train,y_train)
print(x_test.shape, x.shape) #(300, 4)
y_hat=model.predict(x_test)
print('예측 결과값: ',y_hat[:3]) # [0. 1. 1.]

#판별 경계선 값
# f_value=model.decision_function(x)
# print(f_value)

print(confusion_matrix(y_test,y_hat))
# [[143   3]
#  [  5 149]]
acc=(143+149)/300  #(TP+TN)/전체수 #정확도:모델이 정확하게 분류한 비율
recall=143/(143+3) #TP/(TP+FN) # 재현도 : 실제값이 참이 값 중에서 모델이 참이라고 분류한 비율
precision=143/(143+5) #TP/(TP+FP) #정밀도 : 모델이 참이라고 분류한 값에서 실제값이 참인 비율
specificity=149/(5+149) #TN(FP+TN) #특이도: 실제값이 거짓인 값 중에서 모델이 거짓이라고 분류한 비율
fallout=5/(5+149)   #FP/(FP+TN) #위양성률: 실제값이 거짓인 값 중에서 모델이 참이라고 분류한 비율
print('acc(정확도): ',acc)
print('recall(재현율): ',recall) #TPR 실제값이 참이 값 중에서 모델이 참이라고 분류한 비율
print('precision(정밀도): ',precision)
print('specificity(특이도)', specificity)
print('fallout(위양성률): ', fallout) #FPR 실제값이 거짓인 값 중에서 모델이 참이라고 분류한 비율
print('fallout(위양성률): ',1-specificity)

fpr, tpr, threshold=metrics.roc_curve(y_test,model.decision_function(x_test))
# print('fpr: ',fpr)
# print('tpr: ',tpr)
# print('threshold(분류결정 인계값): \n',threshold) #positive 예측값을 결정하는 확률 기준값


# ROC curve 그리기
plt.plot(fpr,tpr,'yo-',label='Logistic Regression') #x축: fpr, y축:tpr
plt.plot([0,1],[0,1],'g--', label='random classifier line(AUC:0.5)') 
plt.plot([fallout],[recall],'ro',ms=8)
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC curve')
plt.legend()
plt.show()

# AUC (ROC curve의 면적) 1에 근사할수록 좋은 모델이다
print('AUC: ',metrics.auc(fpr,tpr))
# random_state=7 / AUC: 0.9965308663938801
# random_state=0 / AUC: AUC:  0.9918848637015782
# random_state=123 /AUC:  0.9874616513271975