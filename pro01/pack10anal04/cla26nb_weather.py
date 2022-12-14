# 날씨정보로 나이브베이즈 분류기 작성 - 비 예보
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics

df=pd.read_csv("../testdata/weather.csv")
# print(df.head(3))
# print(df.info())

features=df[['MinTemp','MaxTemp','Rainfall']]
# label=df['RainTomorrow'].apply(lambda x:1 if x== 'Yes' else 0)
label=df['RainTomorrow'].map({'Yes':1,'No':0})
# print(features.head(3))
# print(label.head(3))
# print(set(label)) #{0, 1}

# 7:3 split
train_x, test_x, train_y, test_y=train_test_split(features, label, test_size=0.3, random_state=1) 
# print(train_x.shape,test_x.shape, train_y.shape,test_y.shape) #(256, 3) (110, 3) (256,) (110,)

# model
gmodel=GaussianNB()
gmodel.fit(train_x,train_y)

pred=gmodel.predict(test_x)
print('예측값: ', pred[:10])
print('실제값: ',test_y[:10].values)

acc=sum(test_y==pred)/len(pred)
print('acc: ',acc)
print('acc: ',accuracy_score(test_y, pred))

#kfold 교차검증
from sklearn import model_selection
cross_val= model_selection.cross_val_score(gmodel, features,label,cv=5)
print('교차검증: ',cross_val)
print('교차검증 평균: ',cross_val.mean())

print('--새로운 자료로 분류 예측--')
import numpy as np
new_weather=np.array([[8.0,24.3,0.0],[10.0,25.0,10.0],[20.0,30.3,5.0]])
new_pred=gmodel.predict(new_weather)
print(new_pred) #[0 1 0]
