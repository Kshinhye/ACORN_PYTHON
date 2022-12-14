#thread를 사용한 디지털 시간출력
import time

now=time.localtime() #시스템이 가지고있는 날짜와 시간을 가질 수 있다.
print(now)
print('{}년 {}월 {}일 {}시 {}분 {}초'.format(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec))

print('-----------------')
import threading

def cal_show():
    now=time.localtime() #시스템이 가지고있는 날짜와 시간을 가질 수 있다.
    print('{}년 {}월 {}일 {}시 {}분 {}초'.format(
        now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec))

def my_run():
    while True:
        now2=time.localtime()
        if now2.tm_min==3: break
        cal_show()
        time.sleep(1)
        
th=threading.Thread(target=my_run) #함수를 줘야함!! my_run()아님!!
th.start()

th.join()
print('프로그램 종료')