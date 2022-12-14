s1='어디서 만든거야?!'
s2='파이썬에서 만들었습니다.'

print('Content-Type:text/html;charset=utf-8\n') #MIME type 브라우저한테 문서 타입;문자타입을 알려주는것
print('''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>index.html</title>
</head>
<body>
    <h1>반갑데이</h1>
    <p>[ 자료출력 ]</p>
    <p>{0}</p>
    <p>{1}</p>
    <br/>
    <img src='../images/duam_logo.png' width='60%'/>
    <br/>
    <a href='../index.html'>메인으로</a>
</body>
</html>
'''.format(s1,s2))