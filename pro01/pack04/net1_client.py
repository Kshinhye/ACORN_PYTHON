#단순 클라이언트

from socket import *

clientsock=socket(AF_INET,SOCK_STREAM)
clientsock.connect(('127.0.0.1',8888)) #능동적으로 server에 접속
clientsock.send('안녕 반가워'.encode(encoding='utf-8', errors='strict'))  #strict: 나 엄격하게 에러 체크할거햐
clientsock.close()