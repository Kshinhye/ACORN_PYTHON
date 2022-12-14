#예외 처리 : 작업 도중 발생하는 에러에 대처하기
#try ~ except

def divide(a,b):
    return a/b

print('이런 저런 작업을 하다가...')

c=divide(5,2)
#c=divide(5,0) #ZeroDivisionError: division by zero

print(c)

try:
    #c=divide(5,0)
    c=divide(5,2)
    print(c)
    
    aa=[1,2]
    print(aa[0])
    #print(aa[5]) #IndexError: list index out of range
    
    #open('c:/abc.txt')

except ZeroDivisionError:
    print('에러: 0으로 나누면 안돼~~')

except IndexError as err:
    print('에러 원인은',err)  #console: 에러 원인은 list index out of range
    
except Exception as e:
    print('기타에러:',e) #console: 기타에러: [Errno 2] No such file or directory: 'c:/abc.txt'
finally:
    print('에러 유무에 상관없이 반드시 실행')
print('프로그램 종료')
