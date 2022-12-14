#DataFrame merge
import numpy as np
import pandas as pd
print('\n---------------merge/concat-----------------')
df1=pd.DataFrame({'data1':range(7),'key':['b','b','b','c','a','a','b']})
print(df1)
df2=pd.DataFrame({'key':['a','b','d'],'data2':range(3)})
print(df2)

print()
print(pd.merge(df1,df2,on='key')) #on='공통칼럼' key를 기준으로 병합
print(pd.merge(df1,df2,on='key',how='inner')) #how='inner'/ inner join
print(pd.merge(df1,df2,on='key',how='outer')) #how='outer'/ full outer join
print(pd.merge(df1,df2,on='key',how='left')) #how='left' / left outer join
print(pd.merge(df1,df2,on='key',how='right')) #how='right' / right outer join
print()
#df1 vs df3 / data1/key, data2/key2공통 칼럼이 없는 경우 
df3=pd.DataFrame({'key2':['a','b','d'],'data2':range(3)})
print(df3)
print(pd.merge(df1,df3,left_on='key', right_on='key2')) #df1의 key와 df3의 key2가 같다
#concat() : 이어붙이기(merge가 아님)
print(pd.concat([df1,df3]))
print(pd.concat([df1,df3],axis=1))

print('\n----------그룹화 연산: pivot, groupby,pivot_table----------')
#엑셀 피벗테이블
#위에랑은 조금 다른 얘기야~
#데이터 열 중에서 두개의 키를 사용하여 데이터를 선택 후 연산, 구조 변경 후 집계표 작성
data={
    'city':['강남','강북','강남','강북'], #명목척도
    'year':[2000,2001,2002,2002],
    'pop':[3.3,2.5,3.0,2.0] #pop:인구수
}
df=pd.DataFrame(data)
print(df.pivot('year', 'city', 'pop'))
print(df.pivot('city', 'year', 'pop')) #index / columns / values
print(df.set_index(['city', 'year']).unstack()) #위에랑 모양 같음

print()
#df.groupby(['city']) : city별로 객체 생성한 후, pop과 year에 대한 합을 구함 
print(df.groupby(['city']).sum())
print(df.groupby(['city']).agg('sum'))
print(df.groupby(['city','year']).mean()) #평균

print('----pivot_table----')
print(df.pivot_table(index=['city'],aggfunc=np.mean)) #aggfunc=np.mean 기본값
print(df.pivot_table(index=['city'])) #city별 인구,년도의 평균을 구한다.
print(df.pivot_table(index=['city','year'],aggfunc=[len,np.sum]))  #len(개수)와 합을 구한다.
#values = '연산대상'
print(df.pivot_table(values=['pop'],index=['city'])) #city별 pop의 평균
print(df.pivot_table(values=['pop'],index=['city'],columns='year'))
#margins=True: 행렬의 합  / fill_value=0 : 결측치는 0으로 채운다
print(df.pivot_table(values=['pop'],index=['year'],columns='city',margins=True,fill_value=0)) 