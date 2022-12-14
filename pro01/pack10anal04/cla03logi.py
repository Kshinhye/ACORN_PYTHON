# kaggle에 등제되어있는 pima-indians-diabetes dataset으로 당뇨병 유무 분류 모델

import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Pregnancies : 임신 횟수
# Glucose : 포도당 부하 검사 수치
# BloodPressure : 혈압(nm Hg)
# SkinThickness : 팔 삼두근 뒤쪽의 피하지방 측정값(nm)
# Insulin : 혈청 인슐린(mu U/ml)
# BMI : 체질량지수(체중(kg)/(키(m))^2)
# DiabetesPedigreeFunction : 당뇨 내력 가중치 값
# Age : 나이
# Outcome : Class 결정 값(0 or 1)

url="https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/prima-indians-diabetes.csv"
names=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']

df=pandas.read_csv(url,names=names, header=None)
print(df.head(3),df.shape) #(768, 9)

array=df.values #matrix로 홀랑 바꿔버렸다.
print(array)
x=array[:,0:8] #인덱싱 2차원 유지
y=array[:,8] #슬라이싱 1차원
print(x.shape, y.shape)  #(768, 8) (768,)

x_train, x_test, y_train, y_test=model_selection.train_test_split(x,y,test_size=0.3,random_state=7) #test_size안주면 2.5 기본
print(x_train.shape, x_test.shape) #(537, 8) (231, 8) 요렇게 쪼개졌다

#모델을 만들어보자
model=LogisticRegression()
model.fit(x_train,y_train)
print('예측값: ', model.predict(x_test[:10]))
print('실제값: ', y_test[:10])
print((model.predict(x_test)!= y_test).sum()) #58개를 틀림

#아래 둘의 차이가 크면 좋지않ㄷㅏ.
print('test로 검정한 분류 정확도: ', model.score(x_test, y_test)) #score() 모델의 정확도  #0.74891
print('train으로 검정한 분류 정확도: ', model.score(x_train, y_train)) #score() 모델의 정확도  #0.78212
pred=model.predict(x_test)
print('분류 정확도: ', accuracy_score(y_test, pred)) #0.74891


print('----------------------------------------------')
# 지금은 전통적인 방법이기떄문에 요런방법으로 알려주는거야
# 텐서플로가면 별도로 있다.
import joblib
import pickle

# 학습이 끝난 모델은 저장 후 읽어 사용하도록 함
# joblib.dump(model,'pima_model.sav')
pickle.dump(model,open('pima_model.sav','wb'))

mymodel=joblib.load('pima_model.sav')
mymodel=pickle.load(open('pima_model.sav','rb'))
print('test로 검정한 분류 정확도: ', mymodel.score(x_test, y_test))

# 새로운 값으로 예측
print(x_test[:1]) #[[ 1.   90.   62.   12.   43.   27.2   0.58 24.  ]]
print(mymodel.predict([[1.,90.,62.,12.,43.,27.2,0.58,24.]]))  #[0.]