# Perceptron(퍼셉트론, 단중신경마)이 학습할 때 주어진 데이터를 학습하고 에러가 발생한 데이터에 기반하여
# Weight(가중치)값을 기존에서 새로운 W값으로 업데이트 시켜주면서 학습
# input의 가중치합에 대해 임계값을 기준으로 두가지 output중 한 가지를 출력하는 구조

#논리회로 실습
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

feature=np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)
# label=np.array([0,0,0,1]) #and
# label=np.array([0,1,1,1]) #or
label=np.array([0,1,1,0]) #xor #아무리 max_iter, eta0을 바꿔도 못맞춘다. 이게 바로 노드가 하나일때의 문제점

ml=Perceptron(max_iter=20, eta0=0.1, verbose=2).fit(feature, label)
# verbose 학습과정을 보여주는것 0:출력X, 1:자세히, 2:함축적 정보만
# eta0 학습률, learning_rate
print(ml)

pred=ml.predict(feature)
#의미는 없지만 그냥 보는거야...
print('pred',pred)
print('acc',accuracy_score(label, pred))