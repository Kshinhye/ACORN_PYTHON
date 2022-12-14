#함수 장식자(decorator:@) @override (자바에서 어노테이션)
#장식자는 또다른 함수를 감싼 함수다. 주 함수가 호출되면 그의 반환값이 장식자에게 건네진다.
#그러면 장식자는 포장된 함수로 교체하여 함수를 돌려준다.

#decorator:a -meta 기능이 있다.
#함수에다가 이런걸 쓰면 어떠한 기능이 발휘한다~

#장식자 없이 먼저
def make2(fn):
    return lambda:'안녕 '+fn() #주소 리턴
def make1(fn):
    return lambda:'반가워 '+fn()
def hello():
    return '홍길동'
hi=make2(make1(hello))
print(hi())

print()
@make2
@make1
def hello2():
    return '고길동'

print(hello2())