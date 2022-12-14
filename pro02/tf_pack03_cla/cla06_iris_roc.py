# iris dataset으로 분류 모델 여러개 생성 후 성능비교(다항분류) 
# 최종 모델 ROC curve 표현

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from keras.layers import Dense
from keras.models import Sequential

iris=load_iris()
# print(iris.keys())

x=iris.data
print(x[:2])
y=iris.target
print(set(y)) #3가지

names=iris.target_names #꽃의 종류명
print(names) #['setosa' 'versicolor' 'virginica']
feature_names=iris.feature_names
print(feature_names) #['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

# label에 대한 원핫인코딩
print(y[:1], y.shape) #[0] (150,)
onehot=OneHotEncoder(categories='auto') # keras:to_categorical / numpy:eye(), pandas:get_dummies()
y=onehot.fit_transform(y[:, np.newaxis]).toarray() #newaxis 차원확대
print(y[:1], y.shape) #[[1. 0. 0.]] (150, 3)

# feature에 대해 표준화(지금은 단위에 큰 차이는 없지만 보여주기위해 하는거야)
scaler=StandardScaler()
x_scale=scaler.fit_transform(x)
print(x_scale[:2]) # 평균0 표준편차 1을 쓰고있다

# train/test split
x_train, x_test, y_train, y_test=train_test_split(x_scale, y, test_size=0.3, random_state=1)

n_features=x_train.shape[1]
n_classes=y_train.shape[1]
print('feature수: {}, label 수: {}'.format(n_features,n_classes)) #feature수: 4, label 수: 3

print('model--------------------------------')

# 패턴만 보여줄게요~ 간결하게 짜볼게요
def create_model_func(input_dim, output_dim, out_nodes, n, model_name='model'):
    # print(input_dim, output_dim, out_nodes, n, model_names)
    def create_model():
        model=Sequential(name=model_name)
        # 입력층
        for _ in range(n):
            model.add(Dense(units=out_nodes, input_dim=input_dim, activation='relu'))
        # 출력층
        model.add(Dense(units=output_dim, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
        
        return model
    return create_model
   
models=[create_model_func(n_features, n_classes, 10, n, 'model_{}'.format(n)) for n in range(1,4)]
    
print(models)

for cre_model in models:
    print()
    cre_model().summary()

history_dict = {}
for cre_model in models:
    model = cre_model()
    print('모델명 : ', model.name)
    histories = model.fit(x_train, y_train, batch_size=5, epochs=50, validation_split=0.3,verbose=0)
    score = model.evaluate(x_test, y_test, verbose=0)
    
    print('test_loss : ',score[0])
    print('test_acc : ',score[1])
    history_dict[model.name] = [histories,model]
    
print(history_dict)


# 모델 성능 확인을 위한 시각화
import matplotlib.pyplot as plt
fig, (ax1, ax2)=plt.subplots(2,1, figsize=(8,6))

for model_name in history_dict:
    print('h_d: ', history_dict[model_name][0].history['acc'])

    val_acc=history_dict[model_name][0].history['val_acc']
    val_loss=history_dict[model_name][0].history['val_loss']
    
    ax1.plot(val_acc, label=model_name)
    ax2.plot(val_loss, label=model_name)
    ax1.set_ylabel('val_acc')
    ax2.set_ylabel('val_loss')
    ax2.set_xlabel('epochs')
    ax2.set_ylabel('val_loss')
    ax1.legend()
    ax2.legend()
plt.show()

# ROC curve 로 모델 성능 확인
from sklearn.metrics import roc_curve, auc
# 왼쪽에 가까울수록 좋은모델

plt.figure() # 위에 2행1열 짜리를 다시 원래대로 돌림
plt.plot([0,1],[0,1], 'k--') #검은색 파선 그어보기

for model_name in history_dict:
    model=history_dict[model_name][1]
    y_pred= model.predict(x_test)
    
    #fpr, tpr 구하기
    fpr, tpr, _=roc_curve(y_test.ravel(), y_pred.ravel()) #ravel 차원 떨어뜨리기
    plt.plot(fpr, tpr, label='{}, AUC value: {:.3f}'.format(model_name, auc(fpr, tpr)))

plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC curve')
plt.legend()
plt.show()

print()
print('\nk-fold 교차검증 수행하여 모델 성능 비교')
from keras.wrappers.scikit_learn import KerasClassifier #분류 인터페이스를 실행
from sklearn.model_selection import cross_val_score
create_model = create_model_func(n_features, n_classes, 10, 1)
estimator = KerasClassifier(build_fn=create_model, epochs=50, batch_size=10, verbose=2)
scores = cross_val_score(estimator, x_scale, y, cv=10) #cv는 10겹으로 접기
print('acc : {:0.2f} (+/-{:0.2f}'.format(scores.mean(), scores.std()))

create_model = create_model_func(n_features, n_classes, 10, 1)
estimator = KerasClassifier(build_fn=create_model, epochs=50, batch_size=10, verbose=2)
scores = cross_val_score(estimator, x_scale, y, cv=10) #cv는 10겹으로 접기
print('acc : {:0.2f} (+/-{:0.2f}'.format(scores.mean(), scores.std()))

create_model = create_model_func(n_features, n_classes, 10, 1)
estimator = KerasClassifier(build_fn=create_model, epochs=50, batch_size=10, verbose=2)
scores = cross_val_score(estimator, x_scale, y, cv=10) #cv는 10겹으로 접기
print('acc : {:0.2f} (+/-{:0.2f}'.format(scores.mean(), scores.std()))

