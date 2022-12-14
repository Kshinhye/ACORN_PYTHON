#일급함수: 함수안에 함수를 선언할 수 있으면된다. 인자로 함수를 전달 할 수 있어야한다. 반환값으로 함수를 쓸 수 있다.
def func1(a,b):
    return a+b

func2=func1
print(func1(3, 4))
print(func2(3, 4))

print()
def func3(func): #가인수로 함수 수신
    def func4(): #함수 안에 함수를 선언할 수 있다.
        print('나는 중첩(내부) 함수야')
    func4()
    return func  #반환값이 함수다.

#치환:변수에 값 전달하는 방법1 치환하기 a=b
#인수로전달:함수나 메소드를 고르면서 인수로 전달하는 방법
mbc=func3(func1) #실인수(엑츄얼아규먼트)로 함수를 전달하고 있다.
#mbc도 func1의 주소를 가지고있다
print(mbc)
print(id(func1),id(mbc))
print(mbc(3,4))

print('------Lambda:축약함수(단발성, 일회성),이름이 없는 한 줄 짜리 함수------')
#형식은 간단합니다: lambda 인자,...:표현식 / return 없이 결과 반환
#def를 쓸 정도로 복잡하지 않거나 def를 적용할 수 있 없는 곳에 사용하면 효과적
def Hap(x,y):
    return x+y

print(Hap(1,2))
#위 코드를 람다함수로 바꾸면 아래와 같다
print((lambda x, y:x+y)(1,2))

g=lambda x,y:x+y
print(g)
print(g(3,4))

kbs=lambda a,su=10:a+su
print(kbs(5))
print(kbs(5,6))

sbs=lambda a,*tu,**di:print(a,tu,di)
sbs(1,2,3,m=4,n=5)

print()
li=[lambda a,b:a+b, lambda a:a+5]
print(li[0](3,4))
print(li[1](3))

print('--어떤 함수의 인자로 람다를 사용--')
#filter(함수,집합형 자료)
print(list(filter(lambda a: a<5 ,range(0,10)))) #반환값 list/0부터9까지 숫자 중 a값이 5보다 작은애들만 거를거야
print(list(filter(lambda a: a%2 ,range(10))))
print(list(filter(lambda a: a%2==1 ,range(10))))

#1~100 사이의 정수 중 5의 배수이거나 7의 배수 이거나 7의 배수만 걸러서 출력
print(list(filter(lambda a: a%5==0 or a%7==0 ,range(1,101))))

