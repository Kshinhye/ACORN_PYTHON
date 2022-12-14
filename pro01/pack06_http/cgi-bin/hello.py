#웹서비스 대상 파일
#이때 print는 콘솔이 아니라 브라우저에 찍겠다는 의미! JAVA에서 썼던 써블릿을 생각해라~

kor=50
eng=60
tot=kor+eng

print('Content-Type:text/html;charset=utf-8\n') #MIME type 브라우저한테 문서 타입;문자타입을 알려주는것
print('<html><body>')
print('<title>my.py</title>')
print('<b>안녕하세요</b> 파이썬 모듈로 작성했습니당<br>')
print('총점은 %s'%(tot))
print('</body></html>')
