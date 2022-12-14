#웹 서버를 구축 (아주 심플하게 단순하게 하나 맹글어 본다)

#HttPServer: 기본적인 socket연결을 관리
#SimpleHTTPRequestHandler: 요청을 처리 (get,post)
from http.server import SimpleHTTPRequestHandler, HTTPServer

port=7777

handler=SimpleHTTPRequestHandler #반응만 보이는 단순 서버
serv = HTTPServer(('127.0.0.1',port),handler)
print('웹서비스 시작...')
serv.serve_forever() #인터벌은 안쓰고 기본값으로 가져갈게요