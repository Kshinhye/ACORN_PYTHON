# 웹에서 json문서 읽기
# BeatifulSoup XXXXXXXXXX

import json
import urllib.request as req

url="https://raw.githubusercontent.com/pykwon/python/master/seoullibtime5.json"
plainText=req.urlopen(url).read().decode()
#print(plainText) #str

jsonData=json.loads(plainText) #str -> dict : json 디코딩
#print(jsonData) #dict
print()
print(jsonData['SeoulLibraryTime']['row'][0]['LBRRY_NAME'])
print()
#get() : dict가 갖고있느거
libDatas=jsonData.get('SeoulLibraryTime').get('row')
datas=[]
for ele in libDatas:
    name=ele.get('LBRRY_NAME')
    tel=ele.get('TEL_NO')
    addr=ele.get('ADRES')
    #print(name+'\t'+tel+'\t'+addr)
    
    imsi=[name,tel,addr] #list로 만들어서
    datas.append(imsi)
    
import pandas as pd
df=pd.DataFrame(datas,columns=['도서관명','전화번호','주  소'])
print(df)
print(df.to_html()) #장고에 뿌리고 싶다면?