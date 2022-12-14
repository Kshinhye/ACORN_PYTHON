# 연산자와 기본 함수 경험
import tensorflow as tf
import numpy as np
x=tf.constant(7)
y=tf.constant(3)

print(x+y)
print(tf.add(x,y))
print(tf.cond(x>y, lambda:tf.add(x,y),lambda:tf.subtract(x,y)))

#TypeError: Each entry in 'pred_fn_pairs' must be a 2-tuple. Received True.
f1=lambda:tf.constant(123)
f2=lambda:tf.constant(456)
print(tf.case([(tf.greater(x,y), f1)],default=f2)) # if(x>y) return 123 else return 456 
#tf.less
print()
print('관계 연산')
print(tf.equal(1,2).numpy()) #False
print(tf.not_equal(1,2).numpy()) #True
print(tf.greater(1,2).numpy()) #False
print(tf.greater_equal(1,2).numpy()) #False
print(tf.less_equal(1,2).numpy()) #True
print(tf.less(1,2).numpy()) #True
print()
print('논리 연산')
print(tf.logical_and(True,False).numpy()) #False
print(tf.logical_or(True,False).numpy()) #True
print(tf.logical_not(True).numpy()) #False
print(tf.logical_not(False).numpy()) #True
print('tf.unique')
kbs=tf.constant([1,2,2,2,3])
val, idx=tf.unique(kbs)
print(val.numpy(), idx.numpy()) #value: [1 2 3] #index:[0 1 1 1 2]
print('tf.reduce~ :차원축소')
#tf.reduce~ :차원축소 (꽤 쓰입니다)
ar=[[1,2],[3,4]]
print(tf.reduce_mean(ar)) #tf.Tensor(2, shape=(), dtype=int32)
print(tf.reduce_mean(ar, axis=0).numpy()) #열평균 [2 3]
print(tf.reduce_mean(ar, axis=1).numpy()) #행평균 [1 3]

t=np.array([[[0,1,2],[3,4,5],[6,7,8],[9,10,11]]])
print(t.shape) #(1, 4, 3) 1면 4행 3열
t=np.array([[[0,1,2],[3,4,5]],[[6,7,8],[9,10,11]]])
print(t.shape) #(2, 2, 3) 2면 2행 3열
print(tf.reshape(t,shape=[2,6])) #차원변경 shape=(2, 6)
print(tf.reshape(t,shape=[-1,6])) #차원변경 shape=(2, 6)
print(tf.reshape(t,shape=[2,-1])) #차원변경 shape=(2, 6)
print()
print('차원축소: squeeze()')
aa=np.array([[1],[2],[3],[4]])
print(aa.shape) #(4, 1) 4행 1열짜리가
bb=tf.squeeze(aa)
#squeeze는 열 요소가 1일 경우에만 차원축소가 가능하다.
print(bb.shape) #(4,) 4열짜리로 바꼈다.

aa2=np.array([[[1],[2]],[[3],[4]]])
print(aa2.shape) #(2, 2, 1)
print(aa2)
bb2=tf.squeeze(aa2)
print(bb2.shape) #(2, 2)
print()
print(t.shape) #(2, 2, 3)
t2=tf.squeeze(t) #열 요소가 한개일때만 차원 축소 가능
print(t2.shape) #(2, 2, 3)
print()
print('차원확대: expand.dims()')
tarr=tf.constant([[1,2,3],[4,5,6]])
print(tf.shape(tarr)) #tf.Tensor([2 3], shape=(2,), dtype=int32)
print(tarr)
sbs=tf.expand_dims(tarr,0) #첫번째 차원을 추가해 차원확장
print(sbs, tf.shape(sbs)) #shape=(1, 2, 3)
print()
sbs2=tf.expand_dims(tarr,1) #두번째 차원을 추가해 차원확장
print(sbs2, tf.shape(sbs2)) #shape=(2, 1, 3)
print()
sbs3=tf.expand_dims(tarr,2) #세번째 차원을 추가해 차원확장
print(sbs3, tf.shape(sbs3)) #shape=(2, 3, 1)
print()
sbs4=tf.expand_dims(tarr,-1) #제일 뒤에 차원을 추가해 차원 확장
print(sbs4, tf.shape(sbs4)) #shape=(2, 3, 1)
print()
print('one-hot / argmax')
# 많이 나오는 녀석들이라 슬쩍 볼게요
print(tf.one_hot([0,1,2,3], depth=4))
print(tf.argmax(tf.one_hot([0,1,2,3], depth=4)).numpy()) #[0 1 2 3]