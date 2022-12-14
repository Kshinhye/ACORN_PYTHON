#서버 무한루핑

import socket
import sys

# HOST='127.0.0.1'
HOST='192.168.0.7'
PORT=7878

serversock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversock.bind((HOST,PORT))  #통로 열어놨으니까 여기로 들어와
    serversock.listen(5)   #동시 접속 최대 수 설정(1~5)
    print('server start...')
    
    while True:
        conn, addr=serversock.accept() #accept() : 연결대기 #무한루프에 빠트린다. 서버는 클라이언트가 올 때 까지 하염없이 기다린다
        print('client info: ',addr[0],addr[1]) #ip address, port number
        #메세지 수신
        #클라이언트가 접속하면서 메세지를 달고 오는데 그걸 서버가 한 번 받아볼게요
        print('from client message: ',conn.recv(1024).decode())
        
        #메세지 송신
        conn.send(('from server: '+str(addr[0])+'안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕안녕').encode('utf-8'))
        
except socket.error as err:
    print('err: ',err)
    sys.exit()
finally:
    serversock.close()
    conn.close()