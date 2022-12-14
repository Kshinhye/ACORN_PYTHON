# BeautigulSoup 클래스가 제공하는 searching 관련 method

from bs4 import BeautifulSoup

#연습을 위해서 HTML 문서를 여기에 맹글어놓고 해볼게요
#request로 읽었다 치자
html_page= '''
<html><body>
<h1>제목 태그</h1>
<p>웹 문서 스크래핑</p>
<p>특정 페이지 문서읽기</p>
</body></html>
'''
print(type(html_page)) #<class 'str'>
#str을 객체로 만들기
#해석기 종류 / html.parser / lxml / xml
soup=BeautifulSoup(html_page,'html.parser')
print(type(soup)) #<class 'bs4.BeautifulSoup'>
print(soup) #트리로 만들어짐
print()

h1=soup.html.body.h1 #soup의 html아래 body 아래 h1
print(h1,h1.string,h1.text) #태그의 글자만 일어오기 h1.string  /  h1.text
print()

p1=soup.html.body.p
print(p1.string)

#DOM 사용 / 형제한테 가는 법
p2=p1.next_sibling.next_sibling
print(p2.string)

print('\n------검색용메소드: find()-------')
#뷰티풀수프의 검색을 위한 메소드
#검색용메소드 첫번 째

#find() 는 하나만 리턴한다.
html_page2= '''
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹 문서 스크래핑</p>
<p id="my" class="our" >특정 페이지 문서읽기</p>
</body></html>
'''
soup2=BeautifulSoup(html_page2,'html.parser')
print(soup2.p,' ',soup.p.string) #최초 p태그만 만남
print(soup2.find('p').string) #최초 p태그만 만남
print(soup2.find(['p','h1']).string) #제목 태그 하나만 받아옴
print(soup2.find(id='title').string)
print(soup2.find(id='my').string)
print(soup2.find(class_='our').string)
print(soup2.find(attrs={'class':'our'}).string)
print(soup2.find(attrs={'id':'my'}).string)

print('\n------검색용메소드: find_all()/findAll()-------')
#뷰티풀수프의 검색을 위한 메소드
#검색용메소드 두번째

#find_all()은 복수를 리턴한다.
html_page3= '''
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹 문서 스크래핑</p>
<p id="my" class="our" >특정 페이지 문서읽기</p>
<div>
    <a href="https://www.naver.com" class="aa">naver</a></br>
    <a href="https://www.daum.con">daum</a></br>
</div>
</body></html>
'''
soup3=BeautifulSoup(html_page3,'html.parser')
print(soup3.find_all('p'))
print(soup3.findAll('p'))
print(soup3.find_all('a'))
print(soup3.find_all(['a','p']))
print(soup3.find_all(class_='aa'))
links=soup3.find_all('a')
for i in links:
    print(i.attrs['href'],'-',i.string)
print()
print('--------정규표현식 써볼게용--------')
import re
links2=soup3.find_all(href=re.compile(r'^https')) #첫번째 글자 https글자로 시작하는거
for i in links2:
    print(i.attrs['href'],'-',i.string)
print()

print('--------css의 selector 사용--------')
#select_one :단수반환 / select :복수반환

html_page4= '''
<html><body>
<div id="hello">
    first div
    <a href="https://www.naver.com" class="aa">naver</a></br>
    <span>
        <a href="https://www.daum.con">daum</a></br>
    </span>
    <ul class="world">
     <li>안녕</li>
     <li>반가워</li>
    </ul>
</div>
<div id="hi" class="good">
    second div
</div>
</body></html>
'''
soup4=BeautifulSoup(html_page4,'html.parser')
print(soup4.select_one("div"))
print()
print(soup4.select_one("div#hi"))
print()
print(soup4.select_one("div.good"))
print()
print(soup4.select("div#hello > a")) #자식(직계자손)
print(soup4.select("div#hello a")) #자손
print(soup4.select("div#hello > span >a"))

lis=soup4.select("div#hello ul.world > li")
print(lis)
print()

#lis를 dataframe에 넣어볼게요
msg=list()  #msg=[]
for i in lis:
    msg.append(i.string)

import pandas as pd
df=pd.DataFrame(msg, columns=['자료'])
print(df)