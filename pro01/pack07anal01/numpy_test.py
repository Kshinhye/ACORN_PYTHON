import numpy as np

'''
1) step1 : array 관련 문제
 정규분포를 따르는 난수를 이용하여 5행 4열 구조의 다차원 배열 객체를 생성하고, 각 행 단위로 합계, 최댓값을 구하시오.
'''
ran = np.random.rand(5,4)
ran_min1 = np.min(ran[:,1])
ran_max1 = np.max(ran[:,1])
print(ran)
print(ran_max1)

'''
2) step2 : indexing 관련문제
문2-1) 6행 6열의 다차원 zero 행렬 객체를 생성한 후 다음과 같이 indexing 하시오.
'''
a=np.zeros((6,6))
print(a)

'''
문2-2) 6행 4열의 다차원 zero 행렬 객체를 생성한 후 아래와 같이 처리하시오.
'''