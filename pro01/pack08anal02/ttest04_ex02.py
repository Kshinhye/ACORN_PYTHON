import numpy as np
import scipy.stats as stats
import pandas as pd
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
    #datas=pd.read_sql(sql,conn)
    
    cdata=[]
    ydata=[]
    for data in cursor.fetchall():
        if data[0]=="총무부":
            cdata.append(data[1])
        elif data[0]=="영업부":
            ydata.append(data[1])   
    
    df1=pd.DataFrame(cdata,columns=['총무부연봉'])
    df2=pd.DataFrame(ydata,columns=['영업부연봉'])
    
    frame=pd.concat([df1,df2],axis=1).fillna(df1.mean())
    
    print(stats.shapiro(frame['총무부연봉']).pvalue)
    #0.014267252758145332
    print(stats.shapiro(frame['영업부연봉']).pvalue)
    #0.02560843899846077
    
    print(stats.wilcoxon(frame['총무부연봉'],frame['영업부연봉']))
    # #pvalue=0.33935546875 > 0.05 이므로 귀무채택 
    
except Exception as e:
    print('err: ',e)
finally:
    cursor.close()
    conn.close()