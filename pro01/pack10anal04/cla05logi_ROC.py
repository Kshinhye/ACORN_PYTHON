# ROC(Receiver Operating Characteristic) curve
# ROC 커브는 모든 가능한 threshold에 대해 분류모델의 성능을 평가하는 데 사용됩니다.
# ROC 커브 아래의 영역을 AUC (Area Under thet Curve)라 합니다.

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

x,y= make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=123)
#n_samples:표본개수 #n_features=독립변수개수 #n_redundant: 독립변수간 선형 조합으로 나타나는 성분의 수
print(x[:3])
print(y[:3])

# import matplotlib.pyplot as plt
# plt.scatter(x[:,0], x[:,1])
# plt.show()

model=LogisticRegression().fit(x,y)
y_hat=model.predict(x)
print('예측 결과값: ',y_hat[:3])
print()
#판별 경계선 값
f_value=model.decision_function(x) #판별함수(결정함수): 판별 경계선을 위해 샘플을 얻어냄
# print('f_value: ', f_value) #클래스가 나눠짐. 0이하는 0으로 취급 0초과일때는 1로취급 #그냥 참고

df=pd.DataFrame(np.vstack([f_value,y_hat,y]).T, columns=['f','y_hat','y'])
print(df.head(3))

print()
#acc,recall,precision 은 필수로 알고 있어야해
print(confusion_matrix(y,y_hat))
acc=(44+44)/100  #(TP+TN)/전체수 #정확도:모델이 정확하게 분류한 비율
recall=44/(44+4) #TP/(TP+FN) # 재현도 : 실제값이 참이 값 중에서 모델이 참이라고 분류한 비율
precision=44/(44+8) #TP/(TP+FP) #정밀도 : 모델이 참이라고 분류한 값에서 실제값이 참인 비율
specificity=44/(8+44) #TN(FP+TN) #특이도: 실제값이 거짓인 값 중에서 모델이 거짓이라고 분류한 비율
fallout=8/(8+44)   #FP/(FP+TN) #위양성률: 실제값이 거짓인 값 중에서 모델이 참이라고 분류한 비율
print('acc(정확도): ',acc)
print('recall(재현율): ',recall) #TPR 실제값이 참이 값 중에서 모델이 참이라고 분류한 비율
print('precision(정밀도): ',precision)
print('specificity(특이도)', specificity)
print('fallout(위양성률): ', fallout) #FPR 실제값이 거짓인 값 중에서 모델이 참이라고 분류한 비율
print('fallout(위양성률): ',1-specificity)

print()
from sklearn import metrics
ac_sco=metrics.accuracy_score(y, y_hat) #(TP+TN)/전체수 #정확도:모델이 정확하게 분류한 비율
print('ac_sco: ', ac_sco)

cl_rep=metrics.classification_report(y, y_hat)
print('cl_rep: \n',cl_rep)

print()
fpr, tpr, threshold=metrics.roc_curve(y,model.decision_function(x))
print('fpr: ',fpr)
print('tpr: ',tpr)
print('threshold(분류결정 인계값): \n',threshold) #positive 예측값을 결정하는 확률 기준값

# ROC curve 그리기
plt.plot(fpr,tpr,'o-',label='Logistic Regression') #x축: fpr, y축:tpr
plt.plot([0,1],[0,1],'k--', label='random classifier line(AUC:0.5)') #중간에 선을 한 번 그어볼까요 #k--: 검은색(k) 파선(--)
plt.plot([fallout],[recall],'ro',ms=10) #위양성률,재현율 한 번 찍어볼까요 #ms:크기
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC curve')
plt.legend()
plt.show()

# AUC (ROC curve의 면적) 1에 근사할수록 좋은 모델이다
print('AUC: ',metrics.auc(fpr,tpr)) #0.9547275641025641