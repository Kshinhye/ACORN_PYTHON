import pandas as pd

df=pd.read_csv("../testdata/서울상권.csv", encoding='cp949')
pd.set_option('display.max_row',None)
pd.set_option('display.max_columns',None)
print(df['상권_코드_명'].unique())
# print(df['상권_코드_명'].value_counts())
