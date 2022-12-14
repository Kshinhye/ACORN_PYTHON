import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
plt.rc('font', family='malgun gothic')
'''
[ANOVA 예제 1]
빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.

기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

kind(기름의 종류) quantity(흡수하는 기름의양)
'''
#귀무: 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 평균에 차이가 없다.
#대립: 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 평균에 차이가 있다.

b_data=pd.read_csv("../testdata/bbang.txt",delimiter=' ')
b_data.quantity=b_data.quantity.fillna(np.mean(b_data.quantity))
# print(b_data.describe())
# print(b_data.info())
# plt.boxplot(b_data.quantity)
# plt.show()
# print(b_data.kind.unique()) #[1 2 3 4]

b1=b_data[b_data['kind']==1]['quantity']
b2=b_data[b_data['kind']==2]['quantity']
b3=b_data[b_data['kind']==3]['quantity']
b4=b_data[b_data['kind']==4]['quantity']

#평균
print(b1.mean(), b2.mean(), b3.mean(), b4.mean())
#63.25 68.83 66.75 72.75

#정규성
print(stats.shapiro(b1).pvalue) #0.868 > 0.05만족
print(stats.shapiro(b2).pvalue) #0.592
print(stats.shapiro(b3).pvalue)
print(stats.shapiro(b4).pvalue)

#등분산
print(stats.levene(b1,b2,b3,b4).pvalue) #0.326 > 0.05 만족

# anova 진행
reg = ols('quantity ~ C(kind)', data=b_data).fit()
table =sm.stats.anova_lm(reg, type=2)
print(table) #0.848244 > 0.05 귀무채택
#             df       sum_sq     mean_sq         F    PR(>F)
# C(kind)    3.0   231.304247   77.101416  0.266935  0.848244
# Residual  16.0  4621.432595  288.839537       NaN       NaN

# 사후검증
# post hoc test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukeyResult = pairwise_tukeyhsd(endog=b_data.quantity, groups=b_data.kind) # 알파값은 기본적으로 0.05다
print(tukeyResult)

#사후검정 시각화
tukeyResult.plot_simultaneous(xlabel='mean' , ylabel='group')
plt.show()


'''
[ANOVA 예제 2]
DB에 저장된 buser와 jikwon 테이블을 이용하여
총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.
'''
#귀무: 부서별 연봉의 평균에 차이가 없다.
#대립: 부서별 연봉의 평균에는 차이가 있다.

import MySQLdb
import pickle

with open('mydb.dat',mode='rb') as obj:
    config=pickle.load(obj)
try:
    conn=MySQLdb.connect(**config) #connect method는 dict타입의 파라미터를 원한다.
    cursor=conn.cursor()
    sql="""SELECT buser_name, jikwon_pay
        FROM jikwon INNER JOIN buser
        on jikwon.buser_num=buser.buser_no
        """
    cursor.execute(sql)
    
    #data=pd.DataFrame.from_records(cursor.fetchall(), columns=['부서명','연봉'])
    data=pd.read_sql(sql,conn)
    # print(data) #buser_name  jikwon_pay
    # print(data.describe())
    # print(data.isnull().sum())

    #총무부, 영업부, 전산부, 관리부 연봉 평균 확인
    p1=np.array(data[data.buser_name=='총무부'].jikwon_pay)
    p2=np.array(data[data.buser_name=='영업부'].jikwon_pay)
    p3=np.array(data[data.buser_name=='전산부'].jikwon_pay)
    p4=np.array(data[data.buser_name=='관리부'].jikwon_pay)
    #print(np.mean(p1),np.mean(p2),np.mean(p3),np.mean(p4))
    #5414  4908  5328  6262

    #정규성 확인해보자
    print(stats.shapiro(p1).pvalue) #0.02604 < 0.05 불만족
    print(stats.shapiro(p2).pvalue) #0.02560 < 0.05 불만족
    print(stats.shapiro(p3).pvalue) #0.41940 > 0.05 만족
    print(stats.shapiro(p4).pvalue) #0.90780 > 0.05 만족

    #다시 정규성을 확인해보자.
    print(stats.ks_2samp(p1,p2).pvalue) #0.335774
    print(stats.ks_2samp(p1,p3).pvalue) #0.575174
    print(stats.ks_2samp(p1,p4).pvalue) #0.536363
    print(stats.ks_2samp(p2,p3).pvalue) #0.335774
    print(stats.ks_2samp(p2,p4).pvalue) #0.640659
    print(stats.ks_2samp(p3,p4).pvalue) #0.536363

    #등분산성 확인
    print(stats.bartlett(p1,p2,p3,p4).pvalue) #0.62909
    # print(stats.levene(p1,p2,p3,p4).pvalue) #0.798075

    #데이터의 퍼짐 정도 시각화
    plt.boxplot([p1,p2,p3,p4], showmeans=True)
    plt.show() #못생겼음

    #anova
    print(stats.f_oneway(p1,p2,p3,p4))
    #statistic=0.41244077160708414, pvalue=0.7454421884076983
    #해석: pvalue=0.7454421884076983 > 0.05 귀무채택
    #귀무: 부서별 연봉의 평균에 차이가 없다.

    # 사후검정 post hoc test
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    turkeyResult = pairwise_tukeyhsd(endog=data.jikwon_pay, groups=data.buser_name) #알파값은 0.05 기본
    print(turkeyResult)

    #사후검정 시각화
    turkeyResult.plot_simultaneous(xlabel='mean' , ylabel='group')
    plt.show()

except Exception as e:
    print('err: ',e)

finally:
    cursor.close()
    conn.close()