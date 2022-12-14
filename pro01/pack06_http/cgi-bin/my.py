#사용자가 전송한 정보를 수신 후 어쩌구 저쩌구 할게요.

import cgi

#이거는 CGIHandler가하지 SImple 걔는 못해
form=cgi.FieldStorage()
irum=form['name'].value
nai=form['age'].value

print('Content-Type:text/html;charset=utf-8\n') #MIME type 브라우저한테 문서 타입;문자타입을 알려주는것
print('''
    <html><body>
    <title>my.py</title>
    이름은 {0}
    <br/>
    나이는 {1}
    </html></body>
'''.format(irum,nai)) #이름과 나이 맵핑
