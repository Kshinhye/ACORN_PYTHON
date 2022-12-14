#네이버 제공 코스피 정보를 읽어 csv 파일로 저장

import csv
import requests
from bs4 import BeautifulSoup
import urllib.request as req

url="https://finance.naver.com/sise/sise_market_sum.naver?&page={}"
fname="네이버_코스피.csv"
#newline='' 공백행 제외
fobj=open(fname,mode='w',encoding='utf-8-sig', newline='') #엑셀에서 읽을 때 한글깨짐 방지

writer=csv.writer(fobj)
title="N    종목명    현재가    전일비    등락률    액면가    시가총액    상장주식수    외국인비율    거래량    PER    ROE".split()
print(title)
#타이틀이름으로 제목저장하기
writer.writerow(title)

for page in range(1,3):
    res=requests.get(url.format(str(page)))
    #print(res) #<Response [200]> 확인!
    res.raise_for_status() #읽기를 실패했을시 작업중단
    soup=BeautifulSoup(res.text, 'html.parser')
    #print(soup) #잘 읽어오나 확인
    datas=soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
    #print(datas)
    
    for row in datas:
        cols=row.findAll("td")
        if len(cols) <=1:continue #[''] 해결
        data=[col.get_text().strip() for col in cols]
        #print(data)
        writer.writerow(data)
        
fobj.close()

#csv읽기
import pandas as pd
import numpy as np

df=pd.read_csv(fname)
print(df.head(5))


print('-------------웹툰 순위 읽어오기-------------')
url="https://comic.naver.com/index"
data=req.urlopen(url)

soup=BeautifulSoup(data,'html.parser')
#print(soup)

datas=soup.find("ol",attrs={"class":"asideBoxRank"}).findAll("li")
#print(datas)
for row in datas:
    print(row.find("a").text)
    
print('-------------웹툰 순위 읽어와서 저장하기-------------')
url="https://comic.naver.com/index"
data=req.urlopen(url)

fname2="네이버_웹툰순위.csv" #파일이름
fobj2=open(fname2,mode='w',encoding='utf-8-sig', newline='') 
writer2=csv.writer(fobj2)
title2="웹툰순위".split()
writer2.writerow(title2)

soup=BeautifulSoup(data,'html.parser')
datas=soup.find("ol",attrs={"class":"asideBoxRank"}).findAll("li")

for row in datas:
    col=row.find("a")
    
    writer2.writerow(col)

fobj2.close()
