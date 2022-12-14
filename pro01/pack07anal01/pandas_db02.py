#원격 DB와 연동 후 DataFrame으로 처리

import MySQLdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic') #한글깨짐 #malgun gothic
plt.rcParams['axes.unicode_minus']=False # 한글이 있을 때 - 기호 깨짐
import pickle
import csv

try:
    with open('mydb.dat',mode='rb') as obj:
        config=pickle.load(obj)
except Exception as e:
    print('connect err: ',e) 
 
 
try: 
    conn=MySQLdb.connect(**config)
    cursor=conn.cursor()
    sql="""
        select jikwon_no, jikwon_name, jikwon_jik, buser_name, jikwon_gen, jikwon_pay
        from jikwon inner join buser
        on buser_num=buser_no
    """
    cursor.execute(sql)
    #출력1: DataFrame으로 출력
    df1=pd.DataFrame(cursor.fetchall(),
                     columns=['jikwon_no', 'jikwon_name', 'jikwon_jik', 'buser_name', 'jikwon_gen', 'jikwon_pay'])
    print(df1.head(3))
    
    #출력1: csv파일
    with open("직원.csv", mode='w', encoding='utf-8-sig') as fo:
        writer=csv.writer(fo) #write객체를 만들고
        for r in cursor:
            writer.writerow(r)
            
    #직원 csv 읽기
    df2=pd.read_csv('직원.csv')
    print(df2.head(3))
    
    print('-----pandas 지원 sql 사용-----')
    df3=pd.read_sql(sql,conn)
    df3.columns=['번호','이름','직급','부서','성별','연봉']
    print(df3.head(3)) #경고는 무시해도 괜찮아요
    print()
    
    #이제 이걸 가지고 지가 하고싶은걸 하면 됩니다.
    print('-뭐가 궁금해??-')
    print('건수: ',len(df3), df3['이름'].count())
    print('직급별 인원수:\n', df3['직급'].value_counts())
    print('연봉 평균: ', df3.loc[:,'연봉'].mean())
    print('연봉 표준편차: ', df3.loc[:,'연봉'].std())
    ctab=pd.crosstab(df3['성별'],df3['직급'],margins=True) #crosstable 교차표 #margins=True:합
    print(ctab)
    
    #시각화 해볼게요 : 지급별 연봉 평균
    #직급이 몇개 안되니까 pie차트를 쓸게요
    jik_ypay=df3.groupby(['직급'])['연봉'].mean()
    print(jik_ypay)
    print(jik_ypay.index)
    print(jik_ypay.values)
    #wikidocs.net/92114
    colors = ['silver', 'whitesmoke', 'lightgray', 'whitesmoke', 'gold']
    plt.pie(jik_ypay, explode=(0.05,0.05,0.05,0.05,0.2),labels=jik_ypay.index,
            labeldistance=0.7, counterclock=False, colors=colors)
    plt.show()
    
except Exception as e:
    print('process err: ',e)
finally:
    cursor.close()
    conn.close()