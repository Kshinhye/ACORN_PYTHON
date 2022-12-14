#채팅 클라이언트

import socket
import threading
import sys

def handle(socket):
    while True: #메세지는 한 번 가는게 아니라 계속 가는거니까
        data=socket.recv(1024)
        if not data:continue
        print(data.decode('utf-8'))
        
#버퍼 깨끗하게 비우는 법
#파이썬의 표준출력은 버퍼링이 되고 있다. 이 때 버퍼를 비우기 
sys.stdout.flush()

name=input('채팅 아이디 입력: ')
cs=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('192.168.0.7',5000))
cs.send(name.encode('utf-8'))

th=threading.Thread(target=handle, args=(cs,)).start()

while True:
    msg=input('>>>')
    sys.stdout.flush()
    if not msg:continue
    cs.send(msg.encode('utf-8'))
    
cs.close()