#스레드간에 자원이 충돌될 수 있는데 방지에 대해 얘기해보겠습니다.
#여러 스레드 간 공유자원 충돌 방지
#lock: 동기화(줄서기) - 하나의 스레드가 자원을 사용하는 동안 다른 스레드는 공유자원사용을 대기
#여기서는 뜻만 잘 파악하면 돼요~

import threading, time

g_count=0 #전역변수는 자동으로 스레드의 공유자원이 됨
lock=threading.Lock() #줄세우기
#run 하고 g_count보면 정리되어있는 걸 볼 수 있다

def threadCount(id,count):
    global g_count
    for i in range(count):
        #스레드 간 충돌 방지용. 현재 스레드가 공유자원을 점유하고 있는 동안에 다른 스레드를 대기상태로 만드는 것
        lock.acquire()
        #id:스레드의 아이디 /count:각각의 스레드마다 수행되는 i값/ g_count:global
        print('id: %s ===> count: %s, g_count: %s'%(id,i,g_count)) 
        time.sleep(0.1)
        g_count+=1
        lock.release() #공유자원 점유 해제
        
for i in range(1,6):
    threading.Thread(target=threadCount, args=(i,5)).start()
    
time.sleep(5) #'프로그램종료'가 나중에 실행되라고 얘를 쓴거!
print('처리 후 최종 g_count:',g_count)

print('프로그램 종료')