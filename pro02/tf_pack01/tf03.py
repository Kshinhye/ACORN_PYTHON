# tf.constant(): 텐서(일반적으로 상수)를 직접 기억
# tf.Variable(): 텐서가 저장된 주소를 참조

import tensorflow as tf
import numpy as np

node1=tf.constant(3, tf.float32)
node2=tf.constant(4.0)
print(node1)
print(node2)
imsi=tf.add(node1,node2)
print(imsi)

print()
node3=tf.Variable(3, dtype=tf.float32)
node4=tf.Variable(4.0)
print(node3)
print(node4)
node4.assign_add(node3) #누적
print(node4)

print()
a=tf.constant(5)
b=tf.constant(10)
c=tf.multiply(a,b)
print(c)
result=tf.cond(a<b, lambda:tf.add(10,c), lambda:tf.square(a))
print(result.numpy())

print('---------함수관련: autograph--------')
v=tf.Variable(1)

@tf.function
def find_next_func():
    v.assign(v+1)
    if tf.equal(v%2,0):
        v.assign(v+10)
        
find_next_func()
print(v.numpy())
print(type(find_next_func))
#<class 'function'>
#@tf.function을 사용해 그래프 영역으로 끌고가 연산하는것을 권장
# <class 'tensorflow.python.eager.polymorphic_function.polymorphic_function.Function'>

print('^^^^^^func1: constant^^^^^^')
def func1():  #1부터 3까지 증가
    imsi=tf.constant(0)
    su=1
    for _ in range(3):
        # imsi=tf.add(imsi, su)
        # imsi=imsi+su
        imsi+=su
        
    return imsi

kbs=func1()
print(kbs.numpy(), '', np.array(kbs))    
    
print('^^^^^^func2: constant^^^^^^')
imsi=tf.constant(0)
@tf.function
def func2():  #1부터 3까지 증가
    #UnboundLocalError: local variable 'imsi' referenced before assignment
    #global을 선언함으로써 에러 해결
    global imsi
    su=1
    for _ in range(3):
        # imsi=tf.add(imsi, su)
        # imsi=imsi+su
        imsi+=su
        
    return imsi

mbc=func2()
print(mbc.numpy(), '', np.array(kbs))    
       
    
print('^^^^^^func3: Variable^^^^^^')    
imsi=tf.Variable(0)
@tf.function
#ValueError: tf.function only supports singleton tf.Variables created on the first call. Make sure the tf.Variable is only created once or created outside tf.function. See https://www.tensorflow.org/guide/function#creating_tfvariables for more information.
# auto graph에서는 Variable()은 함수 밖에서 선언!
def func3():
    su=1
    for _ in range(3):
        # imsi=tf.add(imsi, su)
        # imsi=imsi+su
        # imsi+=su 
        
        imsi.assign_add(su)
        
    return imsi
    
sbs=func3()
print(sbs.numpy(),'',np.array(sbs))
    
print('----구구단 출력----')
def gugu1(dan): 
    su=0 #su=tf.constant(0)
    for _ in range(9):
        su=tf.add(su, 1)
        print(su.numpy())
        print('{}*{}={:2}'.format(dan,su,dan*su))
        
gugu1(3)   

@tf.function
#그렇게 잘되던 녀석이 얘만 쓰면 이렇게된다.
#auto graph에서는 numpy를 사용할 수 없다.
def gugu2(dan): 
    su=0 #su=tf.constant(0)
    for _ in range(9):
        su=tf.add(su, 1)
        # print(su.numpy()) # auto graph에서는 tensor연산에만 집중
        # AttributeError: 'Tensor' object has no attribute 'numpy'
        # print('{}*{}={:2}'.format(dan,su,dan*su)) # auto graph에서는 tensor연산에만 집중
        # TypeError: unsupported format string passed to Tensor.__format__
        # 예쁘게 찍고싶으면 밖에서 찍어라
        
gugu2(3)   
    
print()
@tf.function
def gugu3(dan):
    for i in range(1,10):
        result=tf.multiply(dan,i) #원소 곱하기 #tf.matmul:행렬곱
        print('{}*{}={:2}'.format(dan, i,result))
    
gugu3(3)      
    
    
    
    
    
    
    
    