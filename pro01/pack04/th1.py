#실행중인 프로그램을 의미함. 자신만의 메모리를 확보하고 공유하지 않음
#thread: light weight process라고도 함. 하나의 process내에는 한 개의 thread가 존재함
#process 내에 여러개의 thread를 운영하여 여러개의 작업을 동시에 하는 것
#multi thread로 multi tasking이 가능

import threading, time

#스레드가 실행하고 있는메소드가 종료되면 스레드고 끝난다
#메인스레드
def run(id):
    for i in range(1,31):
        print('id:{}--->{}'.format(id,i))
        time.sleep(0.2)
        
#thread를 사용하지 않은 경우
# run(1)
# run(2)

#thread를 사용한 경우
#threading.Thread(target=수행함수명)
th1=threading.Thread(target=run,args=('일',)) #꼭 tuple 타입이어야한다.
th2=threading.Thread(target=run,args=('둘',))
#사용자 정의 스레드
th1.start()
th2.start()
#사용자 정의 스레드가 끝나기전까지 메인스레드를 끝내고싶지 않을 때
#join을 쓰면 메인스레드가 대기타고 있다가 사용자 정의스레드가 끝나면 메인도 끝난다.
th1.join()
th2.join()

print('프로그램 종료')