# 한글 데이터로 워드 카운트
from sklearn.feature_extraction.text import CountVectorizer

text_data=['나는 배 고프다 아니 배가 고프다','오늘 점심 뭐 먹지?','내일 공부 해야겠다','점심 먹고 공부 해야지!']

# 형태소분석을 안하고 한다면?
count_vec=CountVectorizer() 
# count_vec=CountVectorizer(min_df=1, max_df=5) # 최소한번 최대 다섯번까지 허용하겠다.
# count_vec=CountVectorizer(ngram_range=(1,1)) # ngram_range=:단어를 몇개 묶을것이냐
# count_vec=CountVectorizer(stop_words=['나는','해야지']) #stop_words: 불용어(제외할단어/자주등장하는데 분석에는 도움 안되는애(한글의 경우 조사 접미사 등))


count_vec.fit(raw_documents=text_data)
print(count_vec.get_feature_names_out())
print(count_vec.vocabulary_) # 단어사전

# transform()으로 벡터화
print([text_data[0]])
sentence=[text_data[0]] # 문장을 하나 꺼내서
print(count_vec.transform(sentence)) # 벡터화를한다.
print(count_vec.transform(sentence).toarray()) # 벡터화를한다.

# 형태소 분석 후 워드 카운트
from konlpy.tag import Okt

okt=Okt()
my_words=[]
for i, doc in enumerate(text_data):
    for word in okt.pos(doc, stem=True): #stem=True어간추출
        # print(word)
        if word[1] in ['Noun','Verb','Adjective']:
            my_words.append(word[0])
print(my_words)

count_vec=CountVectorizer(analyzer='word',ngram_range=(1,1))
count_vec.fit(my_words)
print(count_vec.get_feature_names_out())
print(count_vec.vocabulary_) # 단어사전
print(count_vec.transform(my_words)) # 벡터화를한다.
print(count_vec.transform(my_words).toarray()) # 벡터화를한다.

print('------------------------------------------')
from sklearn.feature_extraction.text import TfidfVectorizer
# my_word로 할게요
tfidf_vec=TfidfVectorizer(analyzer='word',ngram_range=(1,1))
tfidf_vec.fit(my_words)
print(tfidf_vec.get_feature_names_out())
print(tfidf_vec.vocabulary_) # 단어사전
print(tfidf_vec.transform(my_words)) # 벡터화를한다.
print(tfidf_vec.fit_transform(my_words).toarray()) # 벡터화를한다.
