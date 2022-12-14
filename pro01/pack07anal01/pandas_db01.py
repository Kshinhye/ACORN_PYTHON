# local DB와 

import sqlite3
import pandas as pd

sql="create table if not exists test(product varchar(10), maker varchar(10), weight real, price integer)"
conn=sqlite3.connect(':memory:')
conn.execute(sql)
conn.commit()

data=[('mouse','samsong',12.5,5000),('keyboard','alg',50.5,35000)]
stmt="insert into test values(?,?,?,?)"
conn.executemany(stmt,data)
conn.commit()

data1=('monitor','abc',100.0,550000)
conn.execute(stmt,data1)
conn.commit()

cursor=conn.execute("select * from test")
rows=cursor.fetchall()
for a in rows:
    print(a)
   
# DataFrame에 자료를 기억
df1=pd.DataFrame(rows,columns=['product','maker','weight','price'])
print(df1)


print('------------------------------------')
#요번에는요 pandas의 SQL기능을 사용해볼게요
#판다쓰 와~우 경배하라 판다쓰
#읽기는 read_sql / 저장은 to_sql
df2=pd.read_sql("select * from test",conn)
print(df2)
print()
#DataFrame의 자료를 DB로 저장
data={
    'product':['연필','볼펜','지우개'],
    'maker':['모나미','오나미','사나미'],
    'weight':[2.3,5.5,12.0],
    'price':[500,1500,1000]
}

frame=pd.DataFrame(data)
print(frame)
print()
#이제 넣을거야
frame.to_sql("test",conn,if_exists='append',index=False)
df3=pd.read_sql("select * from test", conn)
print(df3)
print()
print(pd.read_sql("select count(*) as 건수 from test",conn))


