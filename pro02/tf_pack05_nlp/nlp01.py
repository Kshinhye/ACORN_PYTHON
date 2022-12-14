# 자연어 처리란 자연어의 의미를 분석하여 컴퓨터를 통해 사람들이 원하는 어떤 결과를 처리할 수 있도록 하는 일을 말한다. 
# 이를 통해 음성 인식, 문서 요약, 문서 번역, 감성 분석, 텍스트 분류(스팸 메일 분류, 뉴스 기사 카테고리 분류), 
# 질의 응답 시스템, 챗봇 등의 다양한 분야에서 사용될 수 있다.

# 딥 러닝을 이용한 자연어 처리가 주목을 받으면서, 획기적인 알고리즘으로 무장한 새로운 연구 논문들이 활발하게 발표되고 있다. 
# 이러한 기술들을 이해하려면 먼저 자연어 처리에 필요한 전처리 방법(preprocessing), 전통적인 방식의 통계 기반 언어모델, 
# 그리고 무엇보다 중요한 것은 자연어 처리를 위한 관심이 필요하다고 생각한다.

# 워드 임베딩: 단어를 수치화해서 vector를 만듦, 단어를 밀집 벡터(dense vector)의 형태로 표현하는 방법
# 1)카테고리컬 인코딩: 원핫인코딩, 희소백터
# 2)밀집표현: 다차원 벡터 생성

# 데이터 인코딩
print('레이블 인코딩-----')
datas=['python','program','computer','lan','say']
values=[]
for x in range(len(datas)):
    values.append(x)

print(values,'',type(values)) #[0, 1, 2, 3, 4]  <class 'list'>

print('원핫 인코딩------')
import numpy as np
# onehot=np.eye(len(datas)) # 숫자든 문자든
onehot=np.eye(len(values)) # 숫자든 문자든
print(onehot) # 단어의 관계 표현이 불가, 자원 소모가 많음

print('\n 인코딩 클래스를 사용------')
from sklearn.preprocessing import LabelEncoder
datas=['python','program','computer','lan','say']
encoder=LabelEncoder().fit(datas)
values=encoder.transform(datas)
print(values,'', type(values))
print(encoder.classes_)

print('밀집표현 : 단어의 의미를 다차원 공간에 실수로 벡터화하는 분산표현 방법. 단어 간 유사성을 표현할 수 있다')
from gensim.models import word2vec

sentence=[['python','program','computer','lan','say']]
# Word2Vec()을 이용: 유사한 단어들을 비슷한 방향과 힘의 벡터를 갖도록 변환하여 사용
model=word2vec.Word2Vec(sentences=sentence, min_count=1, vector_size=50) #vector_size: 50차원
print(model)
#Word2Vec(vocab=5, vector_size=50, alpha=0.025)
# vocab 5개
word_vectors=model.wv  # wv 단어벡터 생성
print('word_vectors: ',word_vectors)

print('word_vectors index: ',word_vectors.key_to_index)
# {'say': 0, 'lan': 1, 'computer': 2, 'program': 3, 'python': 4}
print('word_vectors keys: ',word_vectors.key_to_index.keys())
# dict_keys(['say', 'lan', 'computer', 'program', 'python'])
print('word_vectors values: ',word_vectors.key_to_index.values())
# dict_values([0, 1, 2, 3, 4])

vocabs=word_vectors.key_to_index.keys()
word_vectors_list=[word_vectors[v] for v in vocabs]
print(word_vectors_list[0]) # 이걸 이용해 단어간 유사도를 구할 수 있다

# 벡터를 사용해 단어간 유사도 구하기
# 1에 가까이갈수록 좋은겨
print(word_vectors.similarity(w1='python',w2='computer')) # python 과 computer 양의관계 0.165
print(word_vectors.similarity(w1='python',w2='say'))
# 코사인 유사도 알고리즘을 사용: 결과값은 -1 ~ 1사이로 나온다. 절대값 1에 근사할수록 유사도가 높다.
print(word_vectors.most_similar(positive='computer')) # computer와의 관계를 보여줌 python이 가장 가까움

# 단어간 유사도결과를 이차원평면으로 시각화 해볼게요
import matplotlib.pyplot as plt

def plot_2d(vocabs,x,y):
    plt.figure(figsize=(8,6))
    plt.scatter(x,y)
    for i, v in enumerate(vocabs):
        plt.annotate(v, xy=(x[i],y[i]))

from sklearn.decomposition import PCA  #PCA 주성분분석(차원축소)
pca=PCA(n_components=2)
xys=pca.fit_transform(word_vectors_list)
xs=xys[:,0]
ys=xys[:,1]

plot_2d(vocabs,xs,ys)
plt.show()