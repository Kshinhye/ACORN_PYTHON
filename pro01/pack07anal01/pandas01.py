# Pandas
# 고수준의 자료구조(Series, DataFrame)와 빠르고 쉬운 데이터 분석용 자료구조 및 함수를 제공한다.
# - NumPy의 고성능 배열 계산 기능과 스프레드시트
# - SQL과 같은 RDMBS의 유연한 데이터 조작 기능을 갖고 있다.
# - 세련된 인덱싱 기능으로 쉽게 데이터를 재배치하여 집계 등의 처리를 편리하게 한다.

import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from astropy.table import index
print('-----------------Series-----------------')
# Series는 일련의 객체를 담을 수 있는 1차원 배열과 같은 자료구조로 색인을 갖는다.

#'pandas.core.series.Series' class 타입

# list #tuple
#set type은 순서가 없기때문에 err: type is unordered
#obj = Series([3, 7, -5, 4])
#obj = Series((3, 7, -5, 4))
#obj = Series({3, 7, -5, 4}) 

#index=[] 색인을 붙일 수 있다.
obj = Series([3, 7, -5, 4], index=['a','b','c','d'])
print(obj, type(obj))
#pandas함수, numpy함수, python함수 (속도차이)
print(obj.sum(),'',np.sum(obj),' ',sum(obj))
print(obj.mean(), obj.std())

print('---value:배열반환, index" 인덱스 반환---')
print(obj.values) #[ 3  7 -5  4] ,가 없으니 array (list는 ,가있음)
print(obj.index)

print('---인덱싱과 슬라이싱---')
#스칼라
print(obj[0],obj['a'])
#Series type
#인덱스명으로 a행이된다.
print( obj[['a']])
#Series type
print(obj[['a','b']]) #인덱싱
print(obj[[2,1]]) #인덱싱
print(obj['a':'b']) #슬라이싱
print(obj[1:4]) #슬라이싱
print(obj>0)  #조건
print('a' in obj) #조건

print('---dict로 Seies 객체 생성---')
names={'mouse':5000,'keyboard':25000, 'monitor':350000}
#print(names)
objs=Series(names)
print(objs) #key=인덱스명 / value=Series의 values
#key(인데스명) 바꾸기
objs.index=['마우스','키보드','모니터']
print(objs)
#name주기
objs.name='상품가격'
print(objs) #Name: 상품가격, dtype: int64


print()
print('-----------------DataFrame-----------------')
# DataFrame
# 여러개의 Series가 모여서 DataFrame을 구성한다.
# 표 모양(2차원 형태 자료)의 자료구조로 여러 개의 칼럼을 갖는다. (Series가 모인 형태)
# 각 칼럼(열, 변수)은 서로 다른 종류의 값을 기억할 수 있다.
# 같은 길이의 리스트에 담긴 dict type의 데이터를 이용해 DataFrame 객체 생성

df=DataFrame(objs) #Series로 Dataframe객체 생성
print(objs)

data = {
    'irum':['홍길동', '한국인', '신기해', '공기밥', '한가해'],
    'juso':('역삼동', '신당동', '역삼동', '역삼동', '신사동'),
    'nai':[23, 25, 33, 30, 35],
}
print(data) #python의 dict type
#dict로 dataframe객체 생성
frame= pd.DataFrame(data)
print(frame, type(frame))

#보고싶은 열 뽑아서보기
#dataframe에서 하나 뽑았으니 Series 타입이다.
print(frame['irum'],type(frame['irum']))
print(frame.irum,type(frame.irum))

#그냥 해보는 칼럼 바꾸기
print(DataFrame(data, columns=['juso','irum','nai']))
print(DataFrame(data, columns=['juso','irum','nai','tel']))
frame2= DataFrame(data, columns=['juso','irum','nai','tel'],index=['a','b','c','d','e'])
print(frame2)
frame2['tel']='111-1111'
print(frame2)
print()
val=Series(['222-2222','333-3333','444-4444'],index=['b','c','d'])
frame2['tel']=val
print(frame2) #덮어쓰기 때문에 나머지 a,e는 다시 NaN이된다.

#행과 열 바꿔보기
#Transpose
print(frame2.T) #numpy랑 똑같음
#★☆★☆★☆★☆이거 잘 봐둬야해요★☆★☆★☆★☆.
print(frame.values) #2차원 배열로 반환된다.
print(frame.values[0,1]) #스칼라로 반환
print(frame.values[0:2])

print('----drop:날리기----')
frame3=frame2.drop('d')
print(frame3)
frame4=frame2.drop('tel',axis=1)
print(frame4)
print('----index명/열 이름으로 정렬----')
print(frame2)
print(frame2.sort_index(axis=0, ascending=False))
print(frame2.sort_index(axis=1, ascending=False))
print(frame2.rank(axis=0)) #열마다 순위매기기 (사전순)
print(frame2['juso'].value_counts()) #개수세기 #어디선가 가끔은 등장 시킬거에요
#문자열 자르기
data={
    'juso':['강남구 역삼동','강남구 신당동', '샤이니 링딩동'],
    'inwon':[23,25,65]
}
fr=DataFrame(data)
print(fr)
result1=Series([x.split()[0] for x in fr.juso])
result2=Series([x.split()[1] for x in fr.juso])
print(result1)
print(result2)
print(result1.value_counts())


























