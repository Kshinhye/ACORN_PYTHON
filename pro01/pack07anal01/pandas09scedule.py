# 일정시간마다 웹에 있는 데이터읽기 / time / schedule
#import schedule #pop insall schedule 스케쥴러 모듈 지원
import time
import datetime
import urllib.request as req
from bs4 import BeautifulSoup
import requests

def work():
    url="https://finance.naver.com/marketindex/"
    #url 읽는방법1 (제일 많이 쓰는 방법)
    #urllib: 데이터를 보낼 때 인코딩하여 바이너리 형태로 보낸다.
    data=req.urlopen(url)
    #url 읽는방법2
    #requests: 데이터를 보낼 때 딕셔너리 형태로 보낸다
    #data=requests.get(url).text
    
    soup=BeautifulSoup(data,'html.parser')
    #print(soup)
    #잡고 읽어오기
    price=soup.select_one("div.head_info > span.value").string
    price2=price.replace(',','') #replace() 공백제거
    print('미국 USD : ', price2)
    
    #파일로 저장할거야 (제목은 현재 시간으로 할거임)
    t=datetime.datetime.now()
    fname="./usd/"+t.strftime('%Y-%m-%d-%H-%M-%S')+'.txt'
    print(fname)
    
    #연습이니 5초에 한번씩 찍어볼게요
    #우선 저장할게요
    with open(fname,'w') as f:
        f.write(price)

while True:
    work()
    time.sleep(5)

