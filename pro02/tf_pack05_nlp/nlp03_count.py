# sklearn이 제공하는 자연어 특징 추출: 문자열을 수치벡터화 함
# CountVectorizer: 각 텍스트에서 단어 출현횟수를 카운팅하는 방법 (수치벡터화:BOW) 얘는 건수만 셀 수 있다 중요한게 뭔지는 모른다. 그래서 Tf를 쓴다.

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
content=['How to format my hard disk', 'Hard disk format format problems'] # 리스트에 두개의 멤버가 들어있다.

# CountVectorizer 먼저 출발해보자
# 한글이라면 선행으로 형태소분석을 먼저 해야한다. 그래서 명사만 가지고하든 동사와같이하든 선행학습이 필요하다.
count_vec=CountVectorizer(analyzer='word', min_df=1)  #analyzer='word'(단어단위), char(글자단위) #min_df 최소등장횟수
print(count_vec)

tran=count_vec.fit_transform(raw_documents=content) # token 처리 후 벡터화됨 (기준은 공백)
print(tran)
print(count_vec.get_feature_names_out()) #대문자는 소문자가 되었다.
# ['disk' 'format' 'hard' 'how' 'my' 'problems' 'to'] BOW벡터  
#    0        1       2     3    4       5        6    <== 사전순으로 인덱싱되고있다.
print(tran.toarray()) #단점: 의미있는 단어를 알기에 문제가 있다.
print('---------------------------------------')
# TfidfVectorizer
# TF  : 특정 단어가 하나의 문장 안에서 등장하는 횟수
# DF  : 특정 단어가 여러 문장에 등장하는 횟수
# IDF : DF에 역수를 취함
# TF-IDF : 하나의 문장 안에서 자주 나오는 단어에 대해 가중치를 줌. 여러 문장에서 자주 등장하는 단어의 경우에는 패널티를 주는 방법

tfidf_vec=TfidfVectorizer(analyzer='word', min_df=1)
tran_idf=tfidf_vec.fit_transform(raw_documents=content)
print(tran_idf) # 출연빈도에서 확률값으로 나온다.
print(tfidf_vec.get_feature_names_out())
print(tran_idf.toarray())