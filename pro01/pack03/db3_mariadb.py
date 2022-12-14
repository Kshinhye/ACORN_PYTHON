#키보드에서 부서 번호를 입력받아 해당 부서 직원자료를 출력(사번, 이름, 부서, 연봉, 직급 출력)

import MySQLdb
import pickle

with open('mydb.dat',mode='rb') as obj:
    config=pickle.load(obj)

def chulbal():
    try:            
        conn=MySQLdb.connect(**config)
        print(conn)
        cursor=conn.cursor()
        buser_info=input('부서이름: ')
        sql="""
            SELECT jikwon_no,jikwon_name,buser_num,jikwon_pay,jikwon_jik
            FROM jikwon INNER JOIN buser
            on jikwon.buser_num=buser.buser_no
            WHERE buser_name='{0}'
        """.format(buser_info)
        #print(sql)
        
        cursor.execute(sql)
        datas=cursor.fetchall()
        #print(datas,len(datas))
        
        if len(datas)==0:
            print('['+str(buser_info)+']에 해당되는 자료는 없어요')
            return #return은 함수 탈출 sys.exit(0) 프로그램 강제 종료
        
        for jikwon_no,jikwon_name,buser,jikwon_pay,jikwon_jik in datas:
            print(jikwon_no,jikwon_name,buser,jikwon_pay,jikwon_jik)
            
        print('인원수: {}'.format(len(datas)))
        
        
    except Exception as e:
        print('err: ',e)
    finally:
        cursor.close()
        conn.close()

if __name__=='__main__':
    chulbal()