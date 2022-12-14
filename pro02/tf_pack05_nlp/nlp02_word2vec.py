# daum 사이트의 뉴수 자료를 읽어 (원래는 웹에서 크롤링해야하는데 귀찮으니) 형태소 분석 후 word2vec을 이용하여 단어 간 유사도 확인
import pandas as pd
from konlpy.tag import Okt

okt=Okt() #객체만들기

with open('다음뉴스.txt', mode='r', encoding='utf-8') as f:
    lines=f.read().split('\n')
# print(lines)
# print(len(lines))

# 명사만 담아보자
wordDic={} # 명사만 추출하여 단어 수 확인
#lines는 list라서 반복문으로 뺴내야한다.
for line in lines:
    datas=okt.pos(line)
    # print(datas)
    for word in datas:
        if word[1] == 'Noun':
            if not(word[0] in wordDic):
                wordDic[word[0]]=1
            wordDic[word[0]] +=1
            
# print(wordDic)

# 단어 건수별 내림차순
keys=sorted(wordDic.items(), key=lambda x:x[1], reverse=True)
# print(keys)

# 결과를 Dataframe에 담기
wordList=[]
countList=[]

for word, count in keys[:20]: #등장횟수가 빈번한 20개만 담아보자
    wordList.append(word)
    countList.append(count)
    
df=pd.DataFrame()
df['word']=wordList
df['count']=countList

print(df)

# 이후 pandas의 다양한 기능들을 활용함
# 우리는 유사도를 봐야해
print('*******'*20)

result=[]

with open('다음뉴스.txt', mode='r', encoding='utf-8') as f:
    lines=f.read().split('\n')
    
    #lines는 list라서 반복문으로 뺴내야한다.
for line in lines:
    datas=okt.pos(line, stem=True) #stem: 원형어근으로 출력, 한가한 -> 한가하다
    print(datas)
    
    imsi=[]
    for word in datas:
        if not word[1] in ['Punctuation','Noun','Josa','Alpha','Suffix','Number']:
            if len(word[0]) >=2:
                imsi.append(word[0])
            
    imsi2=(" ".join(imsi)).strip()
    result.append(imsi2)
    
print(result)
fn='daum_clean.txt'
with open(fn, mode='w', encoding='utf-8') as fobj:
    fobj.write('\n'.join(result))
print('저장성공')

print('\n 밀집벡터 생성 방법 중 wored2vec 사용------')
# 단어간 유사도 확인
from gensim.models import word2vec
lineObj=word2vec.LineSentence(fn)
# 객체로 올라오기때문에 그냥 찍으면 안된다
model=word2vec.Word2Vec(lineObj, min_count=1, vector_size=100, window=10,sg=1)
# vector_size: 100차원 
# sg : (0:CBOW 주변단어로 중심단어를 예측),(1:SkipGram 중심단어로 주변 단어를 예측)
# window : 중심단어를 기반으로 주변단어를 10개 참조할거야
# print(model)

print(model.wv.most_similar(positive=['깨우다']))
print(model.wv.most_similar(positive=['깨우다','찌르다'],topn=3))
print(model.wv.most_similar(positive=['찌르다'],topn=3))
print(model.wv.most_similar(negative=['찌르다']))

# topn 가장유사한 애들 n개까지만

# print('word_vectors: ',word_vectors)
#
# print('word_vectors index: ',word_vectors.key_to_index)
# print('word_vectors keys: ',word_vectors.key_to_index.keys())
# print('word_vectors values: ',word_vectors.key_to_index.values())
