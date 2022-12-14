#스레드간 자원공유 + 스레드 활성화/비활성화
#이벤엔 메쏘드로 해보께요
#acquire() / release() 세트
#lock.wait() / notify() 세트

import threading, time

bread_plate=0 #빵접시 : 스레드의 공유자원으로 자동등록된다.
lock=threading.Condition()

#(threading.Thread) 스레드를 상속받으면 스레드의 대상 메소드가 된다.
class Maker(threading.Thread):  #생산자
    def run(self):
        global bread_plate
        for i in range(30): #빵개수 제한
            lock.acquire() #공유자원 충돌 방지
            while  bread_plate>=10:
                print('빵 생산 초과로 대기')
                lock.wait() #스레드의 비활성화
            bread_plate+=1
            print('빵생산: ',bread_plate)
            lock.notify() #lock 해제
            lock.release()  #공유자원 점유 해제
            time.sleep(0.05)
            
class Consumer(threading.Thread):
    def run(self):
        global bread_plate
        for i in range(30):
            lock.acquire() #공유자원 충돌 방지
            while  bread_plate<1:
                print('빵 소비 초과로 대기')
                lock.wait() #스레드의 비활성화
            bread_plate-=1
            print('빵소비: ',bread_plate)
            lock.notify() #lock 해제
            lock.release()  #공유자원 점유 해제
            time.sleep(0.06)
            
mak=[]; con=[]
for i in range(5): #생산자 수 #빵 만드는 사람 5명
    mak.append(Maker())  #Maker생성자를 부르고있어요~
    
for i in range(5): #소비자 수 #하루에 삼십게먹고
    con.append(Consumer())

for th1 in mak:
    th1.start()

for th2 in con:
    th2.start()
    
for th1 in mak:
    th1.join()

for th2 in con:
    th2.join()
    
print('오늘 영업 끝~~~~~~')