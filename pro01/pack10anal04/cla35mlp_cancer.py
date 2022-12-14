# MLP : breast_cancer dataset
# 표준화 보여줄게요

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

cancer=load_breast_cancer()
# print(cancer.keys()) #['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module']

x=cancer['data']
y=cancer['target'] 
# print(cancer.target_names) #['malignant' 'benign']

#stratify 데이터 나눌 때 쏠림 방지, 값을 target으로 지정하면, 각각의 class 비율을 train / test(validation)에 유지하여, 한 쪽에 쏠려서 분배되는 것을 방지 
x_train, x_test, y_train, y_test=train_test_split(x,y,random_state=1)
# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(426, 30) (143, 30) (426,) (143,)
print(x_train[0])

scaler=StandardScaler().fit(x_train, x_test)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)
print(x_train[0]) #표준화된 값이라 음수도 나오는거야

model=MLPClassifier(hidden_layer_sizes=(30,30,30), solver='adam', learning_rate_init=0.01,max_iter=100, verbose=2, random_state=1) 
model.fit(x_train,y_train)
pred=model.predict(x_test)
print('예측값: ',pred[:5])
print('실제값: ', y_test[:5])
print('train acc: ', model.score(x_train, y_train))
print('test acc: ', model.score(x_test, y_test))

print(confusion_matrix(y_test, pred))
print(classification_report(y_test,pred))