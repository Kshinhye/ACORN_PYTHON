#원격 데이터베이스 연동 프로그램
#pip install mysqlclient
import MySQLdb

# conn=MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test', port=3306)
# print(conn)
# conn.close()

#sangdata table과 연동 #connect()는 dict 타입을 원한다.
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn=MySQLdb.connect(**config)
    #print(conn)
    cursor=conn.cursor()
    
    #insert
    # sql="INSERT INTO sangdata(code, sang, su, dan) values(10,'신상1',5,5000)"
    # cursor.execute(sql)
    # sql="INSERT INTO sangdata values(%s,%s,%s,%s)"
    # sql_data=('11','아아',12,5500)
    # count=cursor.execute(sql,sql_data)    
    # print(count) #insert성공하면 1이 리턴됨
    # conn.commit()
    
    #update 
    sql="UPDATE sangdata set sang=%s, su=%s where code=%s"
    sql_data=('파이썬',50,11)
    count=cursor.execute(sql,sql_data)   
    print(count)
    conn.commit()
    
    #delete (이렇게 문자열 더하기로 짜면 팀장님한테 욕 디지게 먹습니다)
    # code='10'
    # sql="DELETE FROM sangdata WHERE code="+code #secure coding 가이드에 위배가 된다.
    # cursor.execute(sql)
    # conn.commit()
    
    #delete 방법1
    #code='10'
    #sql="DELETE FROM sangdata WHERE code='{0}'".format(code)
    #cursor.execute(sql)
    #conn.commit()

    #delete 방법2
    code='11'
    sql="DELETE FROM sangdata WHERE code=%s"
    cursor.execute(sql,(code,))
    conn.commit()
    
    #select
    sql="SELECT code, sang, su, dan from sangdata"
    cursor.execute(sql)
    
    #방법1
    for data in cursor.fetchall():
        #print(data)
        print('%s %s %s %s'%data)
    
    #방법2
    print()
    for r in cursor:
        print(r[0],r[1],r[2],r[3])
        
    #방법3
    print()
    for (code,sang,su,dan) in cursor:
        print(code,sang,su,dan)
    
    #방법3-1
    print()
    for (a, 품명, su, kbs) in cursor:
        print(a, 품명, su, kbs)
    
except Exception as e:
    print('err: ',e)
    
finally:
    cursor.close()
    conn.close()