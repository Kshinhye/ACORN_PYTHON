#MariaDB 자료 웹으로 출력

import MySQLdb
import pickle

print('Content-Type:text/html;charset=utf-8\n') #MIME type 브라우저한테 문서 타입;문자타입을 알려주는것
print('<html><body>')
print('<title>sangpum.py</title>')
print('<h2>상품정보</h2>')
print('<table>')
print('<tr><th>코드</th><th>품명</th><th>수량</th><th>단가</th></tr>')

#with블럭은 close를 할 필요가 엄써
with open('mydb.dat','rb') as obj:
    config=pickle.load(obj)
    
try:
    conn=MySQLdb.connect(**config)
    cursor=conn.cursor()
    cursor.execute("select * from sangdata")
    datas=cursor.fetchall()
    for code,sang,su,dan in datas:
        print('''
            <tr>
                <td>{0}</td>
                <td>{1}</td>
                <td>{2}</td>
                <td>{3}</td>
            </tr>
        '''.format(code,sang,su,dan))
except Exception as e:
    print('처리오류: ',e)
finally:
    cursor.close()
    conn.close()
print('</table>')
print('</html></body>')