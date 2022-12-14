#둘 중 편한걸로 긁어오면 된다
from urllib.request import urlopen 
import requests
from bs4 import BeautifulSoup

print('----------웹문서읽기1: 벅스차트 읽어오기------------')
url=urlopen("https://music.bugs.co.kr/chart")
soup=BeautifulSoup(url.read(),'html.parser')
#print(soup)
musics = soup.find_all('td',class_='check')
#print(musics)
# 리스트의 원소에 순서값을 부여해주는 함수
#for i, music in enumerate(musics):
#    print("{}위:{}".format(i+1, music.input['title']))


print('----------웹문서읽기2: 위키백과 읽어오기------------')
import urllib.request as req
url="https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
wiki=req.urlopen(url)
#print(wiki)
soup2=BeautifulSoup(wiki,'html.parser')
#mw-content-text > div.mw-parser-output > p:nth-child(6)
#마우스오른쪽 클릭
#print(soup2.select("div.mw-parser-output > p > b"))
result=soup2.select("div.mw-parser-output > p > b")

for a in result:
    #print(a.string)
    if a.string != None:
        print(a.string)
        
print('----------웹문서읽기3: 다음 뉴스읽어오기------------')
url="https://news.daum.net/society#1"
daum=req.urlopen(url)
soup3=BeautifulSoup(daum, 'lxml')

data=soup3.select_one("div > strong >a")
print(data)
for i in data:
    print('i:',i)
print()

datas=soup3.select("div > strong >a")
for i in datas[:5]:
    print('i:',i)
print()

datas2=soup3.findAll("a")
for i in datas2[:5]:
    h=i.attrs['href']
    t=i.string
    print(type(i))
    #print('href: %s, text: %s'%(h,t))






















        
        