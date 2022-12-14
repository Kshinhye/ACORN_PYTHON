import cgi

form=cgi.FieldStorage()

name=form["name"].value #request.getParameter("name") : java
phone=form["phone"].value 
gen=form["gen"].value 

print('Content-Type:text/html;charset=utf-8\n') #MIME type 브라우저한테 문서 타입;문자타입을 알려주는것
print('''
    <html><body>
    <title>my.py</title>
    친구 이름은 {0}
    <br/>
    전화번호는 {1}
    <br/>
    성별은 {2}
    </html></body>
'''.format(name,phone,gen)) #이름과 나이 맵핑