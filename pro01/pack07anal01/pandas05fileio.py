#pandas로 file 읽기
import pandas as pd

#웹에서 읽어오기
df=pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/ex1.csv")
print(df)

#csv로 읽어오기
df=pd.read_csv("../testdata/ex1.csv")
print(df,type(df))

#table로 읽어오기 #skipinitialspace=True : 칼럼 맨앞에 공백 있을 때
df=pd.read_table("../testdata/ex1.csv",sep=',',skipinitialspace=True)
print(df)
print()

#칼럼명이 없는 데이터 읽어오기 / header=None
df=pd.read_csv("../testdata/ex2.csv")
df_hn=pd.read_csv("../testdata/ex2.csv",header=None, names=list('abcde'))
print(df)
print(df_hn)

#txt 파일 읽어오기
#\s+ (공백,tab)
#skiprows=[1,3] : 1행 3행 빠지기
df=pd.read_table("../testdata/ex3.txt",sep='\s+',skiprows=[1,3]) 
print(df)
print(df.describe()) #describe(): 데이터 요약

df=pd.read_fwf("../testdata/data_fwt.txt")
#widths(10자리,3자리,5자리로 끊기)
df_hn=pd.read_fwf("../testdata/data_fwt.txt",header=None,
                  widths=(10,3,5), names=('date','name','price')) 
print(df)
print(df_hn)
print(df_hn['date'].head(3)) #date만 3개 끊어서보기

#★☆★☆★☆ 이거 중요하다 ★☆★☆★☆
print('----chunck: tensor를 쪼개는 함수-----')
#파일의 크기가 큰 경우 일정 행 단위로 끊어 읽기 (메모리 절감 차원)
test=pd.read_csv("../testdata/data_csv2.csv",header=None,names=('no','name','price'),
                 chunksize=3) #chunksize=3 : 3개씩 끊어읽을게요
print(test)
#<pandas.io.parsers.readers.TextFileReader object at 0x00000209067E3A30>
#객체야, 어쩌라고?? 돌려
print('----chunksize=3 반복문으로 꺼내기----')
for piece in test:
    #print(piece)
    #by='price': price를 ascending=True: 내림차순 정렬(청크단위로)
    print(piece.sort_values(by='price', ascending=True))
print()
print('--Series / DataFrame을 파일로 저장--')
items={'apple':{'count':10,'price':1500},'orange':{'count':5,'price':1000}}
df=pd.DataFrame(items)
print(df)

df.to_clipboard()
print(df.to_html()) #dataframe을 웹으로 출력
print(df.to_csv())
print(df.to_json())

print('---csv file로 저장하기---')
df.to_csv("result1.csv")
df.to_csv("result2.csv",index=False,header=False,sep=',') #index=False: 색인제외

data=df.T
print(data)
data.to_csv("result4.csv",index=False,sep=',')

print('---excel file 로 저장하기')
print(df)
print()
writer=pd.ExcelWriter('result5.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='testSheet')
writer.save()
myexcel=pd.read_excel('result5.xlsx', sheet_name='testSheet')
print(myexcel)

