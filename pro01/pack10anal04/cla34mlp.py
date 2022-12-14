# MLP(다층신경망) 요즘 mlp라고 부르지 않는다 딥러닝이라고 부른다

#논리회로 실습
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

feature=np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)
label=np.array([0,0,0,1]) #and
# label=np.array([0,1,1,1]) #or
# label=np.array([0,1,1,0]) #xor 

# solver: default=’adam’
# 레이어를 늘리는게 좋을까 레이어안에 노드 개수를 늘리는게 좋을까? 요리조리 바꿔봐야해요
# model=MLPClassifier(hidden_layer_sizes=10, solver='adam', learning_rate_init=0.01) #hidden_layer_sizes: 노드
# model=MLPClassifier(hidden_layer_sizes=30, solver='lbfgs', learning_rate_init=0.0001,
#                     max_iter=100, verbose=2) #learning_rate_init 와 max_iter 의 관계를 잘 봐라
model=MLPClassifier(hidden_layer_sizes=(10,10,10), solver='lbfgs', learning_rate_init=0.0001,max_iter=100, verbose=0) 

model.fit(feature,label)

pred=model.predict(feature)

print('pred',pred)
print('acc', accuracy_score(label, pred))