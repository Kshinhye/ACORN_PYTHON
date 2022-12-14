import tensorflow as tf
import os
# SSE 및 AVX 등의 경고는 소스를 빌드 하면 없어지지만, 명시적으로 경고 없애기
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print("즉시 실행 모드: ", tf.executing_eagerly()) # tensorflow 2.0 이상 기능
print("GPU ", "사용 가능" if tf.test.is_gpu_available() else "사용 불가능")
print(tf.__version__) #2.11.0

# 네트워크설계 바로 들어가지않고 기본 명령어 먼저 볼게요
# 텐서(tensor)는 배열(array)이나 행렬(matrix)과 매우 유사한 특수한 자료구조
# 텐서는 GPU나 다른 하드웨어 가속기에서 실행할 수 있다는 점만 제외하면 NumPy 의 ndarray와 유사하다
# tensorflow는 numpy 기반이다.(numpy에서 쓸 수 있는거는 tensorflow에서도 쓸 수 있다)

print('--상수선언--')
# 상수 정의(생성) - 상수 텐서를 생성한다.
print(1, type(1))
print(tf.constant(1), type(tf.constant(1))) # scala: 0-d tensor (0차원)  #1, shape=()
print(tf.constant([1]))   # vector: 1-d tensor (1차원 배열)  #[1], shape=(1,)
print(tf.constant([[1]])) # matrix: 2-d tensor (2차원 배열)  #[[1]], shape=(1, 1)
#차원확인 / tf.rank()
print(tf.rank(tf.constant(1)),'\n',tf.rank(tf.constant([1])),'\n',tf.rank(tf.constant([[1]])))

print()
a=tf.constant([1,2])
b=tf.constant([3,4])
c=a+b
print(c) #tensor + tensor 라서 결과도 tensor다
c=tf.add(a,b)
print(c)
print()
d=tf.constant([3])
# d=tf.constant([[3]])
e=c+d #[4 6] + [3]
print(e) #[7 9] / Broadcasting 연산이 일어난거임

# 이 둘은 연산 동네가 다르다.
print(1+2)
print(tf.constant([1])+tf.constant([2]))
print()
# 동네가 다르지만 서로 교환할 수 있다
# tf.convert_to_tensor()
# tf.cast() 형변환
print(7)
print(tf.convert_to_tensor(7, dtype=tf.float32)) #dtype도 바꿀 수 있다
print(tf.cast(7, dtype=tf.float32))
print(tf.constant(7.0))
print(tf.constant(7, dtype=tf.float32))
# 위 4개의 출력결과는 전부 같다. tf.Tensor(7.0, shape=(), dtype=float32)

print('---type 잘 보세요---')
# numpy의 ndarray와 tensor사이의 type 변환
# tensor 영역에서 작업이 이루어진다.
import numpy as np
arr=np.array([1,2])
print(arr, type(arr)) #[1 2]
#<class 'numpy.ndarray'> 

print(arr+5) #[6 7]
# <class 'numpy.ndarray'>

tfarr= tf.add(arr, 5) 
# ndarray가 자동으로 tensor로 형변환이 된다.

print(tfarr, type(tfarr)) # tf.Tensor([6 7], shape=(2,), dtype=int32)
#<class 'tensorflow.python.framework.ops.EagerTensor'>

print(tfarr.numpy()) #[6 7] 
# tensor가 numpy type으로 강제 형변환됨
print(np.add(tfarr,3)) #[ 9 10] 
#tensor가 numpy type으로 자동 형변환됨
print(type(list(tfarr.numpy()))) #[6, 7] 
#<class 'list'> 파이썬