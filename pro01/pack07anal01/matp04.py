# 자전거 공유 시스템 분석용
#  : kaggle 사이트의 Bike Sharing in Washington D.C. Dataset를 편의상 조금 변경한 dataset을 사용함
#
# columns : 
#  'datetime', 
#  'season'(사계절:1,2,3,4), 
#  'holiday'(공휴일(1)과 평일(0)), 
#  'workingday'(근무일(1)과 비근무일(0)), 
#  'weather'(4종류:Clear(1), Mist(2), Snow or Rain(3), Heavy Rain(4)), 
#  'temp'(섭씨온도), 'atemp'(체감온도), 
#  'humidity'(습도), 'windspeed'(풍속), 
#  'casual'(비회원 대여량), 'registered'(회원 대여량), 
#  'count'(총대여량)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import ylabel
plt.rc('font',family='malgun gothic') #한글깨짐 #malgun gothic
plt.rcParams['axes.unicode_minus']=False # 한글이 있을 때 - 기호 깨짐
#datetime 컬럼 타입이 object인데 datetime타입으로 바꿈
train=pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/data/train.csv",parse_dates=['datetime'])
print(train.head(3))
print()
print(train.shape)
print()
print(train.columns)
print()
print(train.info())

print(train.temp.describe())
#null 확인해볼까
print(train.isnull().sum) #없네여

# #null이 포함된 칼럼 확인용 시각화
# #pip install missingno #pip가 안먹히면 conda install missingno
# import missingno as msno
#
# msno.matrix(train,figsize=(12,5)) #figsize=(w,h)
# plt.show()

#칼럼을 재조정/ 년원일 시분초를 별도 칼럼으로추가
train['year']=train['datetime'].dt.year
train['month']=train['datetime'].dt.month
train['day']=train['datetime'].dt.day
train['hour']=train['datetime'].dt.hour
train['minute']=train['datetime'].dt.minute
train['second']=train['datetime'].dt.second

print(train.head(2))
print(train.columns)

#대여량 시각화 bar
figure, (ax1,ax2,ax3,ax4)=plt.subplots(nrows=1,ncols=4)
figure.set_size_inches(15,5) #(w,h)
sns.barplot(data=train, x='year',y='count',ax=ax1)
sns.barplot(data=train, x='month',y='count',ax=ax2)
sns.barplot(data=train, x='day',y='count',ax=ax3)
sns.barplot(data=train, x='hour',y='count',ax=ax4)

ax1.set(ylabel='Count',title='연도별 대여량')
ax2.set(ylabel='Count',title='월별 대여량')
ax3.set(ylabel='Count',title='일별 대여량')
ax3.set(ylabel='Count',title='시간별 대여량')

plt.show()

# 대여량 시각화: boxplot
figure, axes = plt.subplots(nrows=2, ncols=2)
figure.set_size_inches(12, 8)

sns.boxplot(data=train, y='count', orient='v',ax = axes[0][0])
sns.boxplot(data=train, y='count', x='season', orient='v',ax = axes[0][1]) #orient:방향
sns.boxplot(data=train, y='count', x='hour', orient='v',ax = axes[1][0])
sns.boxplot(data=train, y='count', x='workingday', orient='v',ax = axes[1][1])

axes[0][0].set(ylabel='대여량', title='대여량')
axes[0][1].set(ylabel='대여량',xlabel='계절별', title='계절별 대여량')
axes[1][0].set(ylabel='대여량',xlabel='시간별', title='시간별 대여량')
axes[1][1].set(ylabel='대여량',xlabel='근무여부', title='근무여부별 대여량')
#plt.legend() #들어올 자리 없음
plt.show()


#산점도의 일종으로 rugplot이 있다
#temp, windspeed, humidity 
fig, (ax1, ax2,ax3)= plt.subplots(ncols=3)
fig.set_size_inches(10,5)

#판다스와 데이터 엮어봐야해요
sns.rugplot(x='temp', y='count', data=train, ax=ax1)
sns.rugplot(x='windspeed', y='count', data=train, ax=ax2)
sns.rugplot(x='humidity', y='count', data=train, ax=ax3)
plt.show()










