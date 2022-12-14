#멀티 채팅 서버 프로그램 - socket + thread

import socket
import threading

ss=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('192.168.0.7',5000))
ss.listen(5)
print('채팅 서버 서비스 시작..')

users=[] #클라이언트를 이 통에 담아둘게요

def chatUser(conn): #스레드 처리 함수
    name=conn.recv(1024)
    data='[' + name.decode('utf-8')+'] 등장'
    print(data)
    try:
        for p in users:
            p.send(data.encode('utf-8'))
            
        while True:
            msg=conn.recv(1024)
            if not msg:continue
            data='['+ name.decode('utf-8')+' ]님이 말씀하신다:'+msg.decode('utf-8')
            print(data)
            for p in users:
                p.send(data.encode('utf-8'))
            
    except:
        users.remove(conn)
        data=' [' + name.decode('utf-8')+']님 퇴장'
        print(data)
        if users:
            for p in users:
                p.send(data.encode('utf-8'))
        else:
            print('사용자가 없어요')
    
while True:
    conn, addr=ss.accept() #소비자가 컨넥트할때까지 여기서 기다린다
    users.append(conn) #클라이언트를 저장
    th=threading.Thread(target=chatUser, args=(conn,))
    th.start()