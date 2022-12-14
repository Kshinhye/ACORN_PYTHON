# 기상청 제공 날씨정보 (XML 자료 읽기)
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
data=urllib.request.urlopen(url).read()

soup=BeautifulSoup(data,'html.parser')
#print(soup)

#find method #find method #find method #find method #find method
title=soup.find('title').string
print(title)
wf=soup.find('wf').string
print(wf)

city=soup.find_all('city')
print(city)
#태그떼고 데이터 리스트로 만듬
cityData=[]
for c in city:
    cityData.append(c.string)
    
df=pd.DataFrame()
df['city']=cityData
print(df.head(3),len(df))

#select method #select method #select method #select method
tempMins=soup.select('location > province + city + data > tmn') 
#print(tempMins) #각지역의 최저기온이 나온다. data의tmd이 나온다. 
tempData=[]
for t in tempMins:
    tempData.append(t.string)
df['temp_min']=tempData
#컬럼명 바꾸고 싶을 때 (그냥 저거 써도됨)
df.columns=['지역','최저기온']
print(df.head(3))


#파일로 저장해보기
df.to_csv('날씨.csv',index=False)
#파일 읽어와보기
df2=pd.read_csv('날씨.csv')
print('[ 읽어온 데이터 정보 ]\n',df2.head(3))

print('------df 자료로 슬라이싱------')
#iloc (정수기반의 2차원 인덱싱)
print(df.iloc[0]) #1차원 배열취급당함 / vector (Series)

print(df.iloc[0:2,:]) #dataframe / matrix
print(df.iloc[0:2,0:1])
print(df.iloc[0:2,0:2])
print()
print(df['지역'][0:2]) #(Series)
print(df['지역'][:2])
print()
#loc (라벨값 기반의 2차원 인덱싱)
print(df.loc[1:3]) #인덱스가 숫자라서 요런모양을 주었어요
print(df[1:4])
print(df.loc[[1,3]]) #1행과 3행 고르고 싶을 때
print(df.loc[:,'지역'].head(2)) #(Series)
print(df.loc[1:3,['최저기온','지역']])
print(df.loc[:,'지역'][1:4]) #모든 지역에서 1행2행3행

print('-----------')
df=df.astype({'최저기온':int}) #int로 형변환
print(df.info()) #최저기온    41 non-null     int32  형변환 확인
print('최저기온 평균 ', df['최저기온'].mean())
print('최저기온 표준편차 ',df['최저기온'].std())
print(df['최저기온']>=6) #True/False반환
print(df.loc[df['최저기온']>=6]) #True/False에 대한 데이터값이 나온다
print(df.sort_values(['최저기온'],ascending=True))










