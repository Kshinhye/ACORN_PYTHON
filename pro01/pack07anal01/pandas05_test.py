import pandas as pd

print('---문제 3)  타이타닉 승객 데이터를 사용하여 아래의 물음에 답하시오.---')

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv")
print(df)
#1) 데이터프레임의 자료로 나이대(소년, 청년, 장년, 노년)에 대한 생존자수를 계산한다.
bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]
naidae=pd.cut(df["Age"],bins,labels=labels)
#print(naidae)
#df2=df.groupby(result_cut)['Survived'].value_counts().to_frame().unstack()
data=df.groupby(naidae).agg(['sum'])
print(data[['Survived']])

#2) 성별 및 선실에 대한 자료를 이용해서 생존여부(Survived)에 대한 생존율을 피봇테이블 형태로 작성한다.
df_sur=df.pivot_table(values=['Survived'], index=['Sex'],columns='Pclass')
print(df_sur)
print()

print(df_sur)
print('---pandas 문제 4---')
'''
 1) human.csv 파일을 읽어 아래와 같이 처리하시오.
'''
hm=pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/human.csv"
               ,sep=',')
#print(hm)
#Group이 NA인 행은 삭제
print(hm[hm[' Group']!=' NA'])
#Career, Score 칼럼을 추출하여 데이터프레임을 작성
hm2=pd.DataFrame(hm[[' Career',' Score']])
print(hm2)
#Career, Score 칼럼의 평균계산
print(hm2.mean(axis=0,skipna=True))



print('------------------선생님 답----------------------')
human_df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/human.csv')

human_df = human_df.rename(columns=lambda x: x.strip())  # 데이터 앞 공백 제거
print(human_df.head(2))

human_df['Group'] = human_df['Group'].str.strip()  # Group 앞 공백 제거
print(human_df.head(2))

human_df = human_df[human_df['Group']!='NA']
print(human_df.head(5),"\n")

cs_df = human_df[human_df.columns[2:4]] # Career, Score 칼럼의 평균계산
print(cs_df.head(5),"\n")
print(cs_df.mean())