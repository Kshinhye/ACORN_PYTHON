import pandas as pd
import scipy.stats as stats

#===============================================================================
# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
#   예제파일 : cleanDescriptive.csv
#   칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부 (둘 다 빈도수로하니까 범주형)
#   조건 :  level, pass에 대해 NA가 있는 행은 제외한다.
#===============================================================================

#dropna(subset(조건))
data1=pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/cleanDescriptive.csv").dropna(subset=['level','pass'])
print(data1.head(3))
# print(data1.describe)
#null인지 아닌지 확인
print(data1.isnull().sum()) #level과 pass에만 null 이없으면된다.

print(data1['level'].unique()) #[1. 2. 3.] # 1(고졸) 2(대졸) 3(대학원졸) 이라고 하자.
print(data1['pass'].unique()) #[2. 1.] # 1(합격) 2(불합격)

#가설을 세워보자(대립가설은 먼저 세워보까. 통계에서는 귀무가설이 중심이에요)
#귀무가설 : 부모학력 수준이 자녀의 진학여부와 관련이 없다.
#대립가설 : 부모학력 수준이 자녀의 진학여부와 관련이 있다.
#신뢰수준은 따로 얘기 안했으니 95 유의수준은 0.05 오류값은 5%(1종오류/귀무가설이 맞았는데 틀렸다고 하는거)

ctab=pd.crosstab(index=data1['level'],columns=data1['pass']) #level: 부모의학력수준이 pass에 영향을 준다.
ctab.columns=['합격','불합격']
ctab.index=['고졸','대졸','대학원졸']
print(ctab)

chi2,p,ddof,_=stats.chi2_contingency(ctab)
print('chi2:{}, p:{}, ddof: {}'.format(chi2,p,ddof))
#chi2:2.7669512025956684, p:0.25070568406521365, ddof: 2
#해석: p:0.25070568406521365 > 0.05 이므로 귀무가설 채택=부모학력 수준이 자녀의 진학여부와 관련이 없다.

#===============================================================================
# 카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 
#
# 그렇다면 jikwon_jik과 jikwon_pay 간의 관련성 여부를 통계적으로 가설검정하시오.
# 예제파일 : MariaDB의 jikwon table 
# jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
# jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
#
# 조건 : NA가 있는 행은 제외한다.
#===============================================================================
# 대립가설: 직급과 연봉은 관련이 있다.
# 귀무가설: 직급과 연봉은 관련이 없다.

import MySQLdb
import pickle

with open('mydb.dat',mode='rb') as obj:
    config=pickle.load(obj)

try:
    conn=MySQLdb.connect(**config) #connect method는 dict타입의 파라미터를 원한다.
    cursor=conn.cursor()
    sql="SELECT jikwon_jik, jikwon_pay FROM jikwon"
    cursor.execute(sql)
    
    ar=[]
    for data in cursor.fetchall():
        jik=0
        pay=0
        if data[0]=='이사':
            jik=1
        elif data[0]=='부장':
            jik=2
        elif data[0]=='과장':
            jik=3
        elif data[0]=='대리':
            jik=4
        elif data[0]=='사원':
            jik=5
        else:
            jik=0
            
        if 1000 <= data[1] <3000:
            pay=1               
        elif 3000 <= data[1] <5000:
            pay=2   
        elif 5000 <= data[1] <7000:
            pay=3   
        elif 7000 <= data[1]:
            pay=4   
        else:
            pay=0   
        
        ar.append((jik,pay))
    
    #print(ar)
    #이제 빈도표를 작성해보자 df에 넣을거야
    df=pd.DataFrame(ar,columns=['직급','연봉']).dropna()
    
    print(df)
    ctab2=pd.crosstab(index=df['직급'],columns=df['연봉'])
    ctab2.index=['이사','부장','과장','대리','사원']
    ctab2.columns=['1,2천','3,4천','5,6천','7천']
    print(ctab2)
    
    chi2,p,ddof,_=stats.chi2_contingency(ctab2)
    print('chi2:{}, p:{}, ddof: {}'.format(chi2,p,ddof))
    #chi2:37.40349394195548, p:0.00019211533885350577, ddof: 12
    #해석 : p:0.00019211533885350577 < 0.05 이므로 귀무가설 기각, 대립가설 채택(직급과연봉이 관련있다는 소수의견을 받아들이기로함)
    
    
except Exception as e:
    print('err: ',e)
finally:
    cursor.close()
    conn.close()
    
    