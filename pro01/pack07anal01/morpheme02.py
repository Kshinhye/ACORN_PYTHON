#웹문서를 읽어 형태소 분석(konlpy) 후 단어 빈도 수 등을 출력

import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse #한글 인코딩 해주는 친구 한글로 입력해도 

okt=Okt()

#searchPara=input('검색단어: ')
searchPara="김신혜"
searchPara=parse.quote(searchPara)
#print(searchPara) #인코딩 된 문자가 나온다.
#%EA%B9%80%EC%8B%A0%ED%98%9C
#%ED%98%95%EC%9B%90

url="https://ko.wikipedia.org/wiki/" + searchPara
page=urllib.request.urlopen(url).read().decode()
#print(page)

soup = BeautifulSoup(page, 'lxml')
#print(soup)

wordlist=[] #명사만 추출해서 기억
for item in soup.select("#mw-content-text > div.mw-parser-output > p"):
    if item.string != None:
        #print(item.string)
        wordlist+=okt.nouns(item.string) #okt로 명사만 추출
        
print('단어수: ',len(wordlist))
print('wordlist: ',wordlist)

# 어떤 단어가 몇번 나오는지 확인하고싶어요
# 단어의 발생의 횟수를 dict로 저장해보기
word_dict={}

for i in wordlist:
    if i in word_dict:
        word_dict[i]+=1 #이미 있으면 횟수를 누적
    else: #없다면
        word_dict[i]=1 #없다면 1을 넣어
print('발생단어 수:', word_dict)
print('발생단어(중복제거):', set(wordlist))
print('발견된 단어 수 (중복제거):'+str(len(set(wordlist))))

print('----결과를 Series로 출력----')
import pandas as pd

woList=pd.Series(wordlist) #Series 생성자에 wordlist를 준다.
print(woList[:3])
print(woList.value_counts()[:5])
print()
print('----결과를 dataFrame 출력----')
df1=pd.DataFrame(wordlist, columns=['단어'])
print(df1.head(5))
print()
df2=pd.DataFrame([word_dict.keys(),word_dict.values()])
print(df2)
df2=df2.T
df2.columns=['단어','빈도수']
print(df2.head(5))
