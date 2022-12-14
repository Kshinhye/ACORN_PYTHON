#네트워킹 프로그래밍
#TCP protocol 기반의 socket(네트워크를 위한 통신 채널 지원 클래스 또는 함수)

import socket

print(socket.getservbyname('http','tcp'))
print(socket.getservbyname('telnet','tcp'))
print(socket.getservbyname('ftp','tcp'))
print(socket.getservbyname('SMTP','tcp'))
print(socket.getservbyname('pop3','tcp'))

print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))
#'223.130.195.95'    '223.130.200.104'
