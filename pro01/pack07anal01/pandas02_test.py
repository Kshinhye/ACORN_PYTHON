import pandas as pd
import numpy as np
from pandas import Series,DataFrame
'''
  a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오. 
    np.random.randn(9, 4)
  b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정하시오
  c) 각 컬럼의 평균을 구하시오. mean() 함수와 axis 속성 사용
'''
np.random.seed(1)
df = pd.DataFrame(np.random.randn(9, 4),columns=['No1','No2','No3','No4'])
dfm = df.mean(axis=0)
print(dfm)

'''
2번문제
'''
# DataFrame으로 위와 같은 자료를 만드시오
df2= pd.DataFrame(Series([10, 20, 30, 40], index=['a','b','c','d'],name='numbers'))
print('답 df2:\n', df2)
# c row의 값을 가져오시오.
print('답 c row:\n', df2.loc['c']) 
# a, d row들의 값을 가져오시오.
print('답 a,d row:\n', df2.loc[['a','d']])
# numbers의 합을 구하시오.
print(df2.sum(axis=0))
# numbers의 값들을 각각 제곱하시오. 
print(df2.pow(2))
df2['floats']=df2['numbers']/10+0.5
print(df2)
# names라는 이름의 다음과 같은 칼럼을 위의 결과에 또 추가하시오. Series 클래스 사용.
df2['names']=pd.Series(['길동','징어','팔계','오공'],index=['d','a','b','c'])
print(df2)