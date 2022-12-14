#개인용 DB : sqlite3: 파이썬 기본 개인용 데이터베이스

import sqlite3
print(sqlite3.sqlite_version)

print()
#conn=sqlite3.connect('exam.db')
conn=sqlite3.connect(':memory:') #1회용/ ram에 일시적으로 data가 저장됨(휘발성) 테스트용으로 많이 사용됨


try:
    cursor=conn.cursor() #SQL문 처리
    
    #table 생성
    cursor.execute("create table if not exists fritab(name text, phone text)") #사실 SQL문은 대문자로 써야해요 특히 테이블명도 소문자 인정안함 #""를 쓰자
    
    #자료 추가
    cursor.execute("insert into fritab(name,phone) values('한국인','111-1111')")
    cursor.execute("insert into fritab values('우주인','222-2222')")
    cursor.execute("insert into fritab values(?,?)",('신기해','333-3333'))
    inputdata=('신기루','444-4444')
    cursor.execute("insert into fritab values(?,?)", inputdata)
    conn.commit()
    
    #select
    cursor.execute("select * from fritab")
    print(cursor.fetchone()) #하나만
    print(cursor.fetchall()) #모그래서 을 읽을 때
    
    
    
except Exception as e:
    print('err: ',e)
    conn.rollback()
    
finally:
    conn.close()