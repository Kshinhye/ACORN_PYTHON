# 기술통계(Descriptive Statistics)
# - 자료를 정리 및 요약하는 기초적인 통계
# - 데이터 분석 전에 전체적인 데이터 분포의 이해와 통계적 수치 제공
# - 추론통계의 기초자료로 많이 쓰인다.
#
# 기술통계량 유형 - 대표값, 산포도, 비대칭도 : 왜도, 첨도
# 기술 통계 분석 - 정보의 손실을 최대로 줄이면서 데이터를 효과적으로 요약할 수 있는 분석방법.

#도수 분포표 : 특정 구간에 속하는 자료이 수를 나타내는 표

print('----일변량(one variavle) / 명목형 / 빈도분석---')
import pandas as pd
import matplotlib.pyplot as plt

#자료 읽어오기
frame=pd.read_csv("../testdata/ex_studentlist.csv")
#print(frame)
print(frame.info())

print(frame['age'].mean(), frame['age'].var(), frame['age'].std()) #.age로 해도 되지만 사람들은 이렇게 쓰는걸 더 좋아한다.
#22살이 1.11 만큼 떨어져있다 (많이 안떨어져있다 가까이 있다)
#plt.plot(frame['age'])
#plt.show()

#bloodtype으로 볼까요
#print(frame['bloodtype'].mean()) #mean() #err numeric이 아니기 때문
print(frame['bloodtype'].unique())

#bloodtype별 인원수
data1=frame.groupby(['bloodtype'])['bloodtype'].count()
print(data1)

#crosstab 해볼까
data2=pd.crosstab(index=frame['bloodtype'], columns='count')
print(data2)
print()
print('----이변량(two variavle) / 명목형(성별, 혈액형) / 빈도분석---')
data3=pd.crosstab(index=frame['bloodtype'], columns=frame['sex'])
print(data3)
data4=pd.crosstab(index=frame['bloodtype'], columns=frame['sex'], margins=True)
print(data4)
data4.columns=['남','여','합계']
data4.index=['A형',"AB형",'B형','O형','합계']
print(data4)