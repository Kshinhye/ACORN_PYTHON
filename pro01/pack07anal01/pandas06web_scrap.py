# 웹문서읽기
# crawling : scrap, selenium(브라우저마저 통제)
# Beautisoup을 이용 : xml, html 문서처리

import requests
from bs4 import BeautifulSoup

#스크랩핑(웹문서읽기)
def spider():
    baseUrl="https://www.naver.com/index.html"
    sourceData = requests.get(baseUrl)
    print(sourceData)
    
    #페이지 소스가 받아오기(텍스트로 넘어옴)
    plainText = sourceData.text
    print(type(plainText)) #<class 'str'> 얘을 객체로 만들어야함
    
    #객체만들기(구조적인문서로 만들기)
    convertData = BeautifulSoup(plainText, 'lxml')
    print(type(convertData)) #<class 'bs4.BeautifulSoup'> 짠, 객체로 만들어짐
    
    #앵커 한번 읽어볼게용(a태그 몽땅 잡아볼게요)
    for atag in convertData.find_all('a'):
        href=atag.get('href') #a태그 링크와
        title=atag.string #a태그 타이틀
        print(href,' ',title)
        
    
if __name__ == '__main__':
    spider()  #<Response [200]> 서버 양호!