#일회용 먼저 보여줄게요~
#client / server(echo 에코서버, 멍텅구리서버, 그냥 메아리만 쳐주는거야) 프로그래밍
#server

from socket import *

#socket으로 서버 구성
serversock=socket(AF_INET,SOCK_STREAM)  #socket(소켓의 종류, 소켓의 유형)
serversock.bind(('127.0.0.1',8888))  #통로 열어놨으니까 여기로 들어와
serversock.listen(1)   #동시 접속 최대 수 설정(1~5)
print('server start...')

conn, addr=serversock.accept() #accept() : 연결대기 #무한루프에 빠트린다. 서버는 클라이언트가 올 때 까지 하염없이 기다린다
print('addr: ', addr)
print('conn: ', conn)
#클라이언트가 접속하면서 메세지를 달고 오는데 그걸 서버가 한 번 받아볼게요
print('from client message: ',conn.recv(1024).decode())
conn.close()
serversock.close()

