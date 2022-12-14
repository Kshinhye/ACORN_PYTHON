#웹 서버를 구축 (동적으로 웹서버 운영가능)

#HttPServer: 기본적인 socket연결을 관리
#CGIHTTPRequestHandler :동적으로 웹서버 운영가능
#CGI : 웹서버와 외부프로그램 사이에서 정보를 주고받는 방법 또는 규약(약속)
from http.server import CGIHTTPRequestHandler, HTTPServer

port=8888

class Handler(CGIHTTPRequestHandler):
    cg_directories=['/cgi-bin'] #tuple type으로도 가능  멤버cg_directories 한테 '/cgi-bin'(경로)를 알려준다.
    
serv = HTTPServer(('127.0.0.1',port),Handler)
print('웹서비스 시작...')
serv.serve_forever()