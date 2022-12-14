#단순 클라이언트

from socket import *

clientsock=socket(AF_INET,SOCK_STREAM)
clientsock.connect(('192.168.0.19',7979)) #능동적으로 server에 접속
clientsock.send('안녕, 나는 황이란이야'.encode(encoding='utf-8'))  #송신
re_msg=clientsock.recv(1024).decode() #수신
print('수신자료: ',re_msg)
clientsock.close()