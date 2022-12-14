# Random forest는 ensemble(앙상블) machine learning 모델입니다.
# 여러개의 decision tree를 형성하고 새로운 데이터 포인트를 각 트리에 동시에 통과시키며, 
# 각 트리가 분류한 결과에서 투표를 실시하여 가장 많이 득표한 결과를 최종 분류 결과로 선택합니다.
# DecisionTree의 불완정성을 제거한 방법

# Bagging 방식을 사용
# Titanic dataset사용

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.preprocessing.tests.test_data import n_features

df=pd.read_csv("../testdata/titanic_data.csv")
df=df.dropna(subset=['Pclass','Age','Sex'])
# print(df.shape) #(714, 12)
# print(df.head(3))
# print(df.columns)
# print(df.info())
# print(df.isnull().sum())
df_x=df[['Pclass','Age','Sex']] #feature 

# scaling 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
###| Sex를 더미(값이 오직 0과ㅣ1로 이루어진변수)변수로 바꿔줄게요.
#방법1
df_x.loc[:,'Sex'] = LabelEncoder().fit_transform(df_x['Sex']) 
#방법2 함수
# df_x['Sex']=df_x['Sex'].apply(lambda x:1 if x == 'male' else 0)
print(df_x.head(5))

# print(df_y.head(2))

###| Pclass에 대한 원핫인코딩: 
### 해당 열, 범주의 종류만큼 벡터의 크기를 설정하고, 범주에 해당하는 index에 1을 주고, 나머지 요소 모두에는 0으로 준다.
# print(set(df_x['Pclass'])) #{1, 2, 3}

df_x2=pd.DataFrame(OneHotEncoder().fit_transform(df_x['Pclass'].values[:,np.newaxis]).toarray(),
                   columns=['f_class','s_class','t_class'],index=df_x.index)
df_x = pd.concat([df_x,df_x2],axis=1) #두 dataframe 연결

df_y=df['Survived']

# train/test split
train_x, test_x, train_y, test_y = train_test_split(df_x, df_y, test_size=0.25, random_state=12)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)

#model
model = RandomForestClassifier(n_estimators=500, criterion='entropy') # n_estimators: 생성할 트리 개수
model.fit(train_x, train_y)

pred=model.predict(test_x)
print('예측값: ', pred[:5])
print('실제값: ', np.array(test_y[:5]))

#정확도
print('acc: ', sum(test_y == pred)/len(test_y))
from sklearn.metrics import accuracy_score
print('acc: ',accuracy_score(test_y, pred))

#교차검증
from sklearn.model_selection import cross_val_score
cross_vali=cross_val_score(model, df_x,df_y, cv=5)
print(cross_vali)
print(np.mean(cross_vali))

#중요변수
print('특성(변수) 중요도: ', model.feature_importances_) #칼럼에 대한 수치를 제공함
#시각화
import matplotlib.pyplot as plt
def plot_importance(model):
    n_features=df_x.shape[1] #이러면 6이 들어오겠지
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), df_x.columns)
    plt.xlabel('feature_importances')
    plt.ylabel('feature')
    plt.show()

plot_importance(model)