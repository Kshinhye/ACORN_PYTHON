#Scope rule: 변수의 생존 범위
#변수 접근 순서 : Local > Enclosing function(자식을 포함하고있는 부모 함수?) > Global
#파이썬의 특성을 자알 파악하셔야해요

player='전국대표' #전역변수
def funcSoccer():
    player='지역대표' 
    name='신기해' #지역변수
    print(name,player)
funcSoccer()
print(player)

print('------------')
a=10; b=20; c=30 #전역변수
print('1) a:{},b:{},c:{}'.format(a,b,c))
def func1():
    a=444
    b=555
    c=666
    def func2():
        #c=600
        func_local=7 #local func2에서만 유효함
        global c #global을 외쳐주면 지역변수가 아니라 이제 전역변수가 된다
        nonlocal b
        print('2) a:{},b:{},c:{}'.format(a,b,c))
        c=666 #global 없이:UnboundLocalError: local variable 'c' referenced before assignment
        b=70
    func2()
    print('3) a:{},b:{},c:{}'.format(a,b,c))
func1()
print('함수 수행 후) a:{},b:{},c:{}'.format(a,b,c))

