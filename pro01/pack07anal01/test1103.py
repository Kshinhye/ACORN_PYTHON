import numpy as np
#
# data = np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12],
#                 [13,14,15,16]])
# print(data)
# print(data[::-1,::-1])
'''
크기가 다른 두 배열(numpy)을 작성하시오.
x 변수에는 1차원 배열의 요소로 1 2 3 4 5를, 
y 변수에는 2차원 배열(3행 1열)의 요소로 1 2 3을 저장한다.
y 변수는 reshape 함수를 사용한다.
두 배열 간 더하기(+) 연산을 하면 아래와 같은 결과가 나오는데 그 이유도 간단히 적으시오.
'''
#
# x=np.array([1,2,3,4,5])
# y=np.array([1,2,3]).reshape(3,1)
# print(x+y)
#
#
import pandas as pd
# df=pd.read_csv("ex.csv",names=['a','b','c','d'])
# print(df)

#
# a=pd.DataFrame(np.arange(12).reshape((4,3)),columns=['강남','강북','서초'],index=['1월','2월','3월','4월'])
# print(a)

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
url = "http://www.kyochon.com/menu/chicken.asp"
source=urllib.request.urlopen(url)
soup=BeautifulSoup(source,'lxml', from_encoding='utf-8')
#print(soup)
datas_menu=[]
datas_price=[]
for menu in soup.select("#tabCont01 > ul"):
    #print(menu)
    irum=menu.find_all(['dt'])
    price=menu.find_all(['strong'])
    
    for irum2,price2 in zip(irum,price):
        
        irum2=irum2.text
        price2=price2.text.replace(',','')
        
        datas_menu.append(irum2)
        datas_price.append(int(price2))
        
df1=pd.DataFrame(datas_menu,columns=['상품명'])
df1['가격']=datas_price
#print(df1)
print('가격평균: ',df1['가격'].mean())
print('가격 표준편차: ',df1['가격'].std())



