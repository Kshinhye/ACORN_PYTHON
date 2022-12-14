# SVM으로 이미지 분류
# 세계 정치인 중 일부 사진 사용

from sklearn.svm import SVC
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_lfw_people
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


faces=fetch_lfw_people(min_faces_per_person=60, color=False) #인물사진 60개
# print(faces) # 설명을 보고싶으면 faces.DESCR
print(faces.data[:1], '', faces.data.shape)
print(faces.target,'',set(faces.target)) #(1348, 2914)
print(faces.target_names)
print(faces.images.shape) #(1348, 62, 47) 62행 47열 짜리가 1348개 있따
"""
#극단적으로 첫번쨰 이미지만 보실게요
print(faces.images[1])
print(faces.target_names[faces.target[1]])
plt.imshow(faces.images[1], cmap='bone')
plt.show()

fig, ax=plt.subplots(3,5) #3행5열 #Figure(640x480)(기본크기)
# print(fig)
# print(ax.flat)
for i, axi in enumerate(ax.flat):
    axi.imshow(faces.images[i], cmap='bone')
    axi.set(xticks=[], yticks=[], xlabel=faces.target_names[faces.target[i]]) #x축 , y축에 쓰여져있는 글자 ㅇ나보이게

plt.show()
"""
# 주성분 분석으로 이미지 차원 축소
# 이미지의 가장 영향을 주는애들로 차원축소
m_pca=PCA(n_components=150, whiten=True, random_state=0) #whiten: 주성분의 스케일이 작아지도로 조정
x_low=m_pca.fit_transform(faces.data)
print(x_low[:1],x_low.shape) #(1348, 150)
print('변동성비율(중요, 꼭 봐야함): \n', m_pca.explained_variance_ratio_) #앞순서대로 중요
# 다 더하면 0.94573823135579

# model 생성
# 주성분 분석 했으니 그걸로 해볼게요.(원래 faces.data로가지고 SVM을 적용할 수 있어요)
m_svc=SVC(C=1)
#선처리(주성분분석)기와 분류기를 하나의 pipeline으로 묶어 순차적으로 진행
model=make_pipeline(m_pca, m_svc) 
print(model)
#Pipeline(steps=[('pca', PCA(n_components=150, random_state=0, whiten=True)),('svc', SVC(C=1))])

#train/test split
x_train,x_test, y_train,y_test=train_test_split(faces.data, faces.target, random_state=1)
# print(x_train.shape,x_test.shape, y_train.shape,y_test.shape)
#(1011, 2914) (337, 2914) (1011,) (337,)

model.fit(x_train, y_train) #make_pipeline에 의해 먼저 PCA한다.
pred=model.predict(x_test)
print('예측값: ',pred[:10])
print('실제값: ',y_test[:10])
print(classification_report(y_test, pred, target_names=faces.target_names)) #관찰값
print(confusion_matrix(y_test, pred))
print(accuracy_score(y_test, pred)) #분류정확도: 0.7952

fig, ax=plt.subplots(4,6) #4행6열 #Figure(640x480)(기본크기)
for i, axi in enumerate(ax.flat):
    axi.imshow(x_test[i].reshape(62,47), cmap='bone') #bone: 흑백
    axi.set(xticks=[], yticks=[])
    axi.set_ylabel(faces.target_names[pred[i]].split()[-1], color='black' if pred[i] ==  y_test[i] else 'red') #.split([-1])last네임만 보이도록

    fig.suptitle('pred result', size=14)
plt.show()