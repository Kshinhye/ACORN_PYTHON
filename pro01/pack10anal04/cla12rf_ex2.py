'''
[Randomforest 문제2]
중환자 치료실에 입원 치료 받은 환자 200명의 생사 여부에 관련된 자료다.
종속변수 STA(환자 생사 여부)에 영향을 주는 주요 변수들을 이용해 검정 후에 해석하시오. 
모델 생성 후 입력자료 및 출력결과는 Django를 사용하시오.
예제 파일 : https://github.com/pykwon  ==>  patient.csv

<변수설명>
  STA : 환자 생사 여부 (0:생존, 1:사망)
  
  AGE : 나이
  SEX : 성별
  RACE : 인종
  SER : 중환자 치료실에서 받은 치료
  CAN : 암 존재 여부
  INF : 중환자 치료실에서의 감염 여부
  CPR : 중환자 치료실 도착 전 CPR여부
  HRA : 중환자 치료실에서의 심박수
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import matplotlib.pyplot as plt

df=pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/patient.csv")
print(df.shape) #(200, 11)
df_x=df.loc[:,['AGE','SEX','RACE','SER','CAN','INF','CPR','HRA']]
df_y=df.loc[:,'STA']
# print(df_x.info())
# print(df_y.info())

train_x, test_x, train_y, test_y = train_test_split(df_x, df_y, test_size=0.2, random_state=0)
# print(train_x.shape, test_x.shape, train_y.shape, test_y.shape) #(1197, 11) (399, 11) (1197,) (399,)
#(160, 8) (40, 8) (160,) (40,)

#model
model = RandomForestClassifier(n_estimators=500, criterion='entropy') # n_estimators: 생성할 트리 개수
model.fit(train_x, train_y)

pred=model.predict(test_x)
print('예측값: ', pred[:5]) #[0 1 0 1 1]
print('실제값: ', np.array(test_y[:5])) #[0 1 0 1 1]

#정확도
acc=accuracy_score(test_y, pred)
print(acc)

pickle.dump(model,open('patient_model.sav','wb'))

print('특성(변수) 중요도 :\n{0}'.format(model.feature_importances_))

def plot_feature_importances(model):   # 특성 중요도 시각화

    n_features = train_x.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), train_x.columns)
    plt.xlabel("attr importances")
    plt.ylabel("attr")
    plt.ylim(-1, n_features)
    plt.show()
    plt.close()

plot_feature_importances(model)