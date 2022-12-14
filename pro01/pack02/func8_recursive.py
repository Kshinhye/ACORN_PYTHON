#재귀함수(Recursive function): 함수가 자기 자신을 호출 => 반복처리

def CountDown(n):
    if n==0:
        print('완료')
    else:
        print(n,end=' ')
        CountDown(n-1) #<==요거 countdown이라는 함수를 호출하면서 n-1 값을 매개변수로 넣어주라는 뜻

CountDown(5)
print()
print('1~10까지의 합 구하기')
def tot(n):
    if n==1:
        print('탈출')
        return True #명시적으로 써줄 수 있다. 안써도 됨!!
    return n+tot(n-1)

result=tot(10)
print('1~10까지의 합은',result)

print('factorial(n!): 1부터 어떤 양의 정수n까지의 정수를 모두 곱한 것')
#5!=5*4*3*2*1

def factoFunc(a):
    if a==1:return 1
    print(a, end=' ')
    return a*factoFunc(a-1)

result=factoFunc(5)
print('5!:',result)