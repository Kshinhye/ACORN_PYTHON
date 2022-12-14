import MySQLdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
        select jikwon_no, jikwon_name, buser_name,jikwon_pay, jikwon_jik
        from jikwon inner join buser
        on buser_num=buser_no
    """
    cursor.execute(sql)
    
    #Q.사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
    df1=pd.DataFrame(cursor.fetchall(),
                 columns=['사번', '이름','부서명','연봉','직급'])
    print(df1)
    
    #Q.DataFrame의 자료를 파일로 저장
    with open("직원test.csv", mode='w', encoding='utf-8-sig',newline='') as fo:
        writer=csv.writer(fo) #write객체를 만들고
        title="사번 이름 부서명 연봉 직급".split()
        writer.writerow(title)
        for r in cursor:
            writer.writerow(r)
    
    #Q.부서명별 연봉의 합, 연봉의 최대/최소값을 출력
    #df2=pd.read_csv("직원test.csv") #csv 읽어와서 하는 방법
    #하지만 경배하라 pandas 지원 sql 이용
    df2=pd.read_sql(sql,conn)
    df2.columns=['사번', '이름', '부서명', '연봉', '직급']
    bu_ypay=df2.groupby(['부서명'])['연봉']
    print('\n부서별 연봉합\n', bu_ypay.sum())
    print('\n부서별 최대값\n',bu_ypay.max())
    print('\n부서별 최소값\n',bu_ypay.min())
    
    #Q.부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))
    ctab=pd.crosstab(df2['부서명'],df2['직급'])
    print(ctab)
    
    #Q.직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
    
    
    #Q.부서명별 연봉의 평균으로 가로 막대 그래프를 작성
    data=bu_ypay.mean()
    print(data)
    plt.barh(data.index,data,color=['silver','silver','silver','silver'])
    plt.show()
    
    sql2="""
        select jikwon_gen, buser_name,jikwon_pay
        from jikwon inner join buser
        on buser_num=buser_no
    """
    cursor.execute(sql2)
    df3=pd.read_sql(sql2,conn)
    df3.columns = ['성별','부서','연봉']
    print(df3)
    
    #Q.pivot_table을 사용하여 성별 연봉의 평균을 출력
    gen_pivot=df3.pivot_table(values=['연봉'], index=['성별'], aggfunc=np.mean)
    print(gen_pivot)
    
    #Q.성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프
    # 해결못한이유: 평균값을 계산하지 않고 넣어서 실패(이해를 못했다는거지)
    # sns.barplot(x='jikwon_gen',y='jikwon_gen',data=gen_pivot)
    # plt.show()
    
    #선생님 답
    m = df3[df3['성별'] == '남'] #성별 칼럼 중 "남"자의 행만 걸러내
    m_pay_mean = m.loc[:,'연봉'].mean() #그 모든행의 연봉의 평균을 구하고
    f = df3[df3['성별'] == '여']
    f_pay_mean = f.loc[:,'연봉'].mean()
    mean_pay = [m_pay_mean, f_pay_mean]

    plt.bar(range(len(mean_pay)), mean_pay, color=['black','yellow'])
    plt.xlabel('성별')
    plt.ylabel('연봉')
    plt.xticks(range(len(mean_pay)), labels=['남성','여성'])
    plt.show()
    
    #Q.부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))
    ctab2=pd.crosstab(df3['부서'],df3['성별'])
    print(ctab2)
    
except Exception as e:
    print('process err: ',e)
finally:
    cursor.close()
    conn.close()
