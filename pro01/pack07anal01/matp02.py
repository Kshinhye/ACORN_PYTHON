#차트 종류 구경해볼게욤
#data의 성격에 따라 차트를 적용하는것이 중요하다

import numpy as np
import matplotlib.pyplot as plt
'''
#차트 영역 객체 선언시 인터페이스 유형
#크게 두가지를 알면된다

x=np.arange(10)

#방법1 : matplotlib 스타일
plt.figure()
plt.subplot(2,1,1) #subplot(row,col,panel number(active))
plt.plot(x,np.sin(x))
plt.subplot(2,1,2) #subplot(row,col,panel number(active))
plt.plot(x,np.cos(x))
plt.show()

#방법2 : 객체지향 인터페이스
fig,ax=plt.subplots(nrows=2,ncols=1)
ax[0].plot(x,np.sin(x))
ax[1].plot(x,np.cos(x))
plt.show()
'''

'''
fig=plt.figure() #명시적으로 차트영역객체 선언 (방법1이랑 비슷)
ax1=fig.add_subplot(1,2,1) #변형 살짝 줘봤다
ax2=fig.add_subplot(1,2,2) #변형 살짝 줘봤다

#히스토그램을 그려보자
ax1.hist(np.random.randn(10),bins=5,alpha=0.9) #hist( 데이터, 구간, 투명도)
ax2.plot(np.random.rand(10))
plt.show()
'''

'''
#막대그래프 그려볼게 plt.bar()
data=[50,80,100,70,90]
plt.bar(range(len(data)),data)
plt.show()

#가로막대 이리와암 plt.barh()
data=[50,80,100,70,90]
plt.barh(range(len(data)),data)
plt.show()

data=[50,80,100,70,90]
err=np.random.rand(len(data))
plt.barh(range(len(data)),data,xerr=err)
plt.show()
'''
'''
#원형그래프
data=[50,80,100,70,90]
plt.pie(data,explode=(0.1,0.1,0.1,0.1,0.1))
plt.show()
'''
'''
#boxplot 요거는 중요하지
plt.boxplot(data)
plt.show()
'''
#seabon을 볼게요
import seaborn as sns #matplotlib의 기능을 추가
import pandas as pd

titanic=sns.load_dataset('titanic')
pd.set_option('display.max_columns',500)
print(titanic.head(3))
print(titanic.info())

sns.distplot(titanic['age'])
plt.show()

sns.boxplot(y='age',data=titanic)
plt.show()

ti_pivot=titanic.pivot_table(index='class',columns='sex',aggfunc='size')
print(ti_pivot)
sns.heatmap(ti_pivot)
plt.show()

