# DataFrame의 재구조화: stack/unstack
import numpy as np
import pandas as pd
print('---list가꼬 해볼게요---')
df = pd.DataFrame(1000+np.arange(6).reshape(2,3),columns=['칼럼1','칼럼2','칼럼3'],index=['대전','서울'])
print(df)
print()
print('---stack/unstack---')
#인덱스를 기준으로 칼럼쌓기 (열을 인덱스로 가져옴)
df_row=df.stack()
print(df_row)
#다시풀기(stack 결과 원복)
#인덱스를 열로 보내기
df_col=df_row.unstack()
print(df_col)
print()
print('---데이터 범주화 (연속형 -> 번주형) ---')
price=[10.3,5.5,7.8,3.6] 
#구간(범주) 나누기 / 적당히 나눠보까아
cut=[3,7,9,11] #구간 기준값
result_cut=pd.cut(price,cut) #cut(대상,어떻게?)
print(result_cut)
# [(9, 11], (3, 7], (7, 9], (3, 7]] = (초과, 이하] = 9<데이터<=11
print(pd.value_counts(result_cut))
#범주 내 몇개의 데이터가 들어있는지 알 수 있다.

print('---Series으로 해볼게요---')
datas=pd.Series(np.arange(1,1001))
print(datas) #[1000 rows x 1 columns]
print(datas.head(2))
print(datas.tail(2))

print()
cut2=[1,500,1000]
result_cut2=pd.cut(datas,cut2)
print(result_cut2)

result_cut2=pd.qcut(datas,3) #qcut : 범주화할 데이터가 너무 많을 때 
print(result_cut2)
print(pd.value_counts(result_cut2))

print('---dataframe으로 해볼게요---')
datas3=pd.DataFrame(np.arange(1,1001),columns=["nums"])
print(datas3) #[1000 rows x 1 columns]
print(datas3.head(2))
print(datas3.tail(2))

print()
cut2=[1,500,1000]
result_cut3=pd.cut(datas3["nums"],cut2)
print(result_cut2)

result_cut3=pd.qcut(datas3["nums"],3) #qcut : 범주화할 데이터가 너무 많을 때 
print(result_cut3)
print(pd.value_counts(result_cut3))

print()
#각 범주의 그룹별 연산
#groupby() : 그룹 객체 만들기
group_col = datas.groupby(result_cut2)
#agg() : 집계, 그룹 함수 / 여러개의 함수를 여러 열에 적용
#agg('함수이름')
print(group_col.agg(['count','mean','std','min']))

#직접 함수 작성
def summary_func(gr):
    return{
        'count':gr.count(),
        'mean':gr.mean(),
        'std':gr.std(),
        'min':gr.min(),
    }

#apply() : 함수를 실행하는 함수
print(group_col.apply(summary_func))








