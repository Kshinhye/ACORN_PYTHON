#색인 (슬라이싱관련메소드)

import pandas as pd
import numpy as np

#Series의 재색인
data=pd.Series([1,3,2],index=(1,4,2))
#series는 set type불가능이지만 index는 가능 단, {}을하면 원하는 순서대로 넣을 수 없다.
print(data)

#순서 재배치
data2=data.reindex((1,2,4))
print(data2)

print()
data3=data2.reindex([0,1,2,3,4,5])
print(data3) #대응값이 없는 인덱스는 Nan(결측값)이 들어간다.
#NaN(결측값)체워보기
#method='ffill/pad' : 앞에값으로 채우기
data3=data2.reindex([0,1,2,3,4,5],method='ffill')
data3=data2.reindex([0,1,2,3,4,5],method='pad')
print(data3)
#method='bfill/backfill' : 뒤에값으로 채우기
data4=data2.reindex([0,1,2,3,4,5],method='bfill')
data4=data2.reindex([0,1,2,3,4,5],method='backfill')
print(data4)

print('---조건---')
df=pd.DataFrame(np.arange(12).reshape(4,3),index=['1월','2월','3월','4월'],columns=['강남','강북','서초'])
print(df)
print(df['강남']) #강남 열만 나와
print(df['강남']>3) #강남 열만보여주고, 3 초과하는 애들만 True
print(df[df['강남']>3]) #df[] 조건에서 참인 행들만 반환
print('---슬라이싱 관련 method: 복수인덱싱: loc(lavel 지원 메소드), iloc(숫자 지원 메소드)---')
print('---loc---')
print(df.loc['3월',:])
print(df.loc[:'2월'])
print(df.loc[:'2월',['서초']]) #2월 이하행, 서초열 출력
print('---iloc---')
#0부터 시작하는거 헷갈리지말기
print(df)
print(df.iloc[2]) #2행, 모든열 나와라
print(df.iloc[2,:]) #2행만, 모든열 나와라
print(df.iloc[:3]) #2번 행까지, 모든 열
print(df.iloc[:3,2])#2번 행까지, 2열만
print(df.iloc[1:3,1:3]) #1번부터2번행까지, 1번부터2번열까지

print('---산술연산---')
s1=pd.Series([1,2,3],index=['a','b','c'])
s2=pd.Series([4,5,6,7],index=['a','b','d','c'])
print(s1)
print(s2)
print(s1+s2) # -, + ,* , /
print(s1.add(s2)) #numpy #sub,mul,div
print()
#columns=list('kbs') list를 써주면 kbs가 하나씩 잘려서 칼럼명으로 들어간다.
df1=pd.DataFrame(np.arange(9).reshape(3,3),columns=list('kbs'),index=['서울','대전','부산'])
df2=pd.DataFrame(np.arange(12).reshape(4,3),columns=list('kbs'),index=['서울','대전','제주','목포'])
print(df1)
print(df2)
print()
print(df1+df2) #일치하는 애들끼리 더해짐 그외 결측값
print(df1.add(df2,fill_value=0)) #add 메소드의 속성으로 특정값을 줄 수 있다.
print('---serise vs dataframe---')
seri=df1.iloc[0]
print(seri)
print(df1-seri) #numpy의 Broadcasting이 그대로 적용됨 (seri색인을 dataframe의 색인에 맞춘다)

print('---기술적 통계와 관련된 메소드(함수)---')
df= pd.DataFrame([[1.4,np.nan],[7,-4.5],[np.NaN,None],[0.5,-1]],columns=['one','two'])
print(df)
print(df.drop(1)) #1행삭제 #1행:[7,-4.5]
print(df.isnull()) #null값(결측치) 탐지 True/False 반환
print(df.notnull()) #null값(결측치) 탐지 True/False 반환
print('--na지우기--')
#nan값이 하나라도 있는 행은 제거
print(df.dropna())
print(df.dropna(how='any'))
print(df.dropna(axis='rows'))
#행의 모든 값이 nan값일 때 행을 제거
print(df.dropna(how='all'))
#nan이 포함된 열을 삭제
print(df.dropna(axis='columns'))
#nan값을 0으로 채우기
print(df.fillna(0)) #결측치를 0 또는 평균 등의 값으로 대체
#nan의 앞/뒤 값으로 채우기
print(df.fillna(method='ffill'))
print(df.fillna(method='bfill'))
print(df.dropna(subset=['one'])) #특정열에 NaN이 있는 행 삭제
print('--열의합--')
print(df)
print(df.sum())
print(df.sum(axis=0)) #열의 합
print('--행의합--')
print(df.sum(axis=1)) #행의 합
print('--열의평균--')
print(df.mean(axis=0)) #열의 평균
print(df.mean(axis=0,skipna=True)) #연산할 때 NaN 제외
print(df.mean(axis=0,skipna=False)) #연산할 때 NaN 포함
print('--행의평균--')
print(df.mean(axis=1)) #행의 평균
print(df.mean(axis=1,skipna=True)) #연산할 때 NaN 제외
print(df.mean(axis=1,skipna=False)) #연산할 때 NaN 포함
#요약통계량
print(df.describe())
#구조
print(df.info())








