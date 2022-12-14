import numpy as np
import scipy.stats as stats
import pandas as pd
'''
[two-sample t 검정 : 문제1] 
다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다. 
포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 검정하시오.
'''
blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]
#귀무: 포장지 색상에 따른 제품의 매출액에 차이가 존재하지않는다.
#대립: 포장지 색상에 따른 제품의 매출액에 차이가 존재한다.

#정규성검정도 해보자
print(stats.shapiro(blue).pvalue) #0.05 이상으로 정규성 만족
print(stats.shapiro(red).pvalue)

print(np.mean(blue),' ',np.mean(red)) #72.81818181818181 vs  63.81818181818182 ???
print(stats.ttest_rel(blue, red))
#statistic=3.2529905845956475, pvalue=0.008676456444140185
# pvalue=0.008676456444140185 < 0.05 귀무기각 / 포장지 색상에 따른 제품의 매출액에 차이가 존재한다.
print(stats.ttest_ind(blue,red))
#statistic=2.9280203225212174, pvalue=0.008316545714784403

'''
[two-sample t 검정 : 문제2]  
아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여
혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.
'''
남자 = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
여자 = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]
#귀무: 남녀의 혈관 내 콜레스테롤 양에는 차이가 없다.
#대립: 남녀의 혈관 내 콜레스테롤 양에는 차이가 있다.


# man= np.random.choice(남자,size=15)
# women=np.random.choice(여자,size=15)
import random
random.seed(123)
man=random.sample(남자,15)
women=random.sample(여자,15)

#정규성 확인결과 만족안함
#그러므로 ttest_ind를 쓰면안된다. wilcoxon 사용
print('여기야',stats.shapiro(man).pvalue) #0.0376255065202713
print(stats.shapiro(women).pvalue) #0.0014988253824412823

print(np.mean(man), ' ', np.mean(women))

print(stats.wilcoxon(man, women)) #statistic=59.0, pvalue=0.97796630859375
# print(stats.ttest_ind(man,women))
# pvalue=0.97796630859375 > 0.05 귀무 채택 / 남녀는 혈관 내의 콜레스테롤 양에 차이가 없다.

'''
[two-sample t 검정 : 문제3]
DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.
'''
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
    
    df1=pd.DataFrame(cursor.fetchall(),columns=['부서명', '연봉'])
    #print(df1)
    data1=df1[df1['부서명']=="총무부"]['연봉']
    data1.index=[1,2,3,4,5,6,7]
    data2=df1[df1['부서명']=="영업부"]['연봉']
    data2.index=[1,2,3,4,5,6,7,8,9,10,11,12]
    
    frame=pd.concat([data1,data2],axis=1)
    frame.columns=['총무부연봉','영업부연봉']
    frame['총무부연봉']=frame['총무부연봉'].fillna(frame['총무부연봉'].mean())
    print(frame)
    
    print(stats.shapiro(frame['총무부연봉']).pvalue)
    #0.014267252758145332
    print(stats.shapiro(frame['영업부연봉']).pvalue)
    #0.02560843899846077
    
    print(stats.wilcoxon(frame['총무부연봉'], frame['영업부연봉']))
    #pvalue=0.33935546875 > 0.05 이므로 귀무채택 
    
except Exception as e:
    print('err: ',e)
finally:
    cursor.close()
    conn.close()

'''
[대응표본 t 검정 : 문제4]
어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다.
이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?
'''
#귀무: 매년 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다 / 학업능력이 변화가 없다.
#대립: 매년 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고있지 않다. / 학업능력이 변화가 있다.
    
중간 = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
기말 = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

# print(np.mean(중간), ' ',np.mean(기말)) # 74 vs 81 ??

#정규성 확인 결과 만족
print(stats.shapiro(중간).pvalue) #0.3681465983390808
print(stats.shapiro(기말).pvalue) #0.19300280511379242

print(stats.ttest_rel(중간, 기말)) #-2.6281127723493993, pvalue=0.023486192540203194
# 해석: pvalue=0.02348 < 0.05 귀무 기각

