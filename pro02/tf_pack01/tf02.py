# 변수: 모델 학습 시, 매개변수 갱신 등을 위한 사용
# tf.Variable()

import tensorflow as tf

f= tf.Variable(1.0)
v= tf.Variable(tf.ones((2,))) #tf.ones 2열짜리를 1로 채운다.
m= tf.Variable(tf.ones((2,1))) #tf.ones  2행1열을 1로 채운다
print(f) #numpy=1.0
print(v) #numpy=array([1., 1.], dtype=float32)
print(m)
print(m.numpy())
# numpy=array([[1.],
#             [1.]]
print()
print('--치환--')
print('---0-d tensor---')
# v1=7 #err: AttributeError: 'int' object has no attribute 'assign'
v1=tf.Variable(1)  # 0-d tensor
print(v1)
v1.assign(10) #변수의 값 치환 / .assign()
print(v1, v1.numpy(), type(v1))
print('---1-d tensor---')
v2=tf.Variable(tf.ones(shape=(1)))  # shape=(1): 1-d tensor
v2.assign([20])
print(v2, v2.numpy(), type(v2))
print('---2-d tensor---')
v3=tf.Variable(tf.ones(shape=(1,2)))  # shape=(1,2): 2-d tensor
v3.assign([[20,30]])
print(v3, v3.numpy(), type(v3))

print()
v1=tf.Variable([3])
v2=tf.Variable([5])
v3=v1*v2+10
print(v3) #tf.Tensor([25], shape=(1,), dtype=int32)
print()

var=tf.Variable([1,2,3,4,5], dtype=tf.float32)
result1=var+10
print(var) #numpy=array([1., 2., 3., 4., 5.]
print(result1) #tf.Tensor([11. 12. 13. 14. 15.]
print()
w=tf.Variable(tf.ones(shape=(1,)))
b=tf.Variable(tf.ones(shape=(1,)))
w.assign([2])
b.assign([3])

def func1(x):
    return w*x+b
out_a1=func1(3)
print('out_a1: ',out_a1)
# tf.Tensor([9.], shape=(1,), dtype=float32)

print()
@tf.function #auto graph 기능이 적용된 함수: tf.Graph + tf.Session 이 적용
def func2(x):
    return w*x+b

print(type(func2))
out_a2=func2([1,2])
print('out_a2: ',out_a2) #.eager: 설계도에 있는 내용을 바로 볼 수 있어, 신경쓰지마 그냥 function에 있는거야

print()
rand1=tf.random.uniform([5],minval=0, maxval=1) #tf.random.uniform(shape, 최댓값, 최솟값) # 균등분포를 따르기때문에 음수는 안나온다
print(rand1.numpy())
rand2=tf.random.normal([5],mean=0, stddev=1) #tf.random.normal(shape, 평균, 표준편차) # 정규분포를 따른다.
print(rand2.numpy())
rand=tf.random.uniform([5]) #tf.random.uniform(shape, 최댓값, 최솟값) # 균등분포를 따르기때문에 음수는 안나온다
print(rand.numpy())

print()
aa=tf.ones((2,1))
print(aa.numpy())
m=tf.Variable(tf.zeros((2,1)))
print(m.numpy())
#치환
m.assign(aa)
print(m.numpy())
#누적
#assign_add : m+=aa(대충 이런 개념)
m.assign_add(aa)
print(m.numpy())
#빼기
m.assign_sub(aa)
print(m.numpy())

print('\n\n--------TF의 구조 (Graph로 설계된 내용은 Session에 실행)--------')
# 그래프가 내부적으로 쓰이는데 이것을 명시적으로 선언할 수 있다.
g1=tf.Graph()

with g1.as_default(): #특정 자원 처리를 한 후 자동 close()
    c1=tf.constant(1, name='c_one') 
    #c1이라고 하는 녀석은 c_one이라는 이름을 가지고, 정수값 1 하나를 가지고 있는 텐서 상수를 가진, 주소를 기억하고 있는 녀석이다.
    print(c1)
    #Tensor("c_one:0", shape=(), dtype=int32)
    c1_1=tf.constant(1, name='c_one_1') 
    print(c1_1)
    
    
    print(type(c1)) # Tensor 타입의 객체이다.
    #<class 'tensorflow.python.framework.ops.Tensor'>
    print(c1.op) #tf.Operation 객체
    print('-----------')
    print(g1.as_graph_def())
    
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
g2=tf.Graph()
with g2.as_default(): #특정 자원 처리를 한 후 자동 close()
    v1=tf.Variable(initial_value=1, name='v1')
    print(v1)
    print(type(v1))
    print(v1.op)

print('~~~~~~~')    
print(g2.as_graph_def())