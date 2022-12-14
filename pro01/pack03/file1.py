#file i/o 
#filr 인풋아웃풋

import os
print(os.getcwd())

try:
    print('읽기---------------------')
    #mode=r(읽기), w(쓰기), a(추가), b(바인더링)...
    #f1=open(r'C:\work\psou\pro1\pack3\file_testpack03, mode='r', encoding='utf8')
    #f1=open(os.getcwd() + '\\file_test.txt', mode='r', encoding='utf8')
    f1=open('file_test.txt', mode='r', encoding='utf8') #같은경로 
    print(f1)
    print(f1.read())
    f1.close() #자원은 열었으면 닫아라 철칙이야

    print('저장---------------------')
    f2=open('file_test2.txt',mode='w', encoding='utf-8')
    f2.write('My friends\n')
    f2.write('정다정, 윤현성, 김신혜, 최자드, 최호경, 민현진, 변시우')
    f2.close()
   
    print('추가---------------------')
    f3=open('file_test2.txt',mode='a', encoding='utf-8')
    f3.write('\n황이란')
    f3.write('\n이승경')
    f3.close()
    
    print('읽기---------------------')
    f4=open('file_test2.txt',mode='r', encoding='utf-8')
    print(f4.readline())
    print(f4.readline())
   
except Exception as e:
    print('에러: ',e)
