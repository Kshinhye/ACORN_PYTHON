#BeautifulSoup으로 XML 문서처리

import urllib.request as req
from bs4 import BeautifulSoup

url="https://raw.githubusercontent.com/pykwon/python/master/seoullibtime5.xml"
plainText=req.urlopen(url).read().decode() #decode() 디코딩
#print(plainText)
soup=BeautifulSoup(plainText, 'lxml')
libData=soup.select('row')
for data in libData:
    name = data.find('lbrry_name').text
    addr=data.find('adres').text
    print('도서관명: ',name)
    print('주  소: ',addr)