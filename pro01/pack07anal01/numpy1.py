# numpy:
# Numpy는 C언어로 구현된 파이썬 라이브러리로써, 고성능의 수치계산과 선형대수학을 위해 제작되었다.
# Numerical Python의 줄임말이기도 한 Numpy는 벡터 및 행렬 연산에 있어서 매우 편리한 기능을 제공

#표본집단-> (통계량) 모집단->(모수) 를 구할 수 있다.

#우선 list로 해볼게요.
grades = [1,3,-2,4] #변량(숫자로 나타낸 자료들)

print('--------------하나씩 계산----------------')
def grades_sum(grades):
    tot=0
    for g in grades:
        tot +=g
    return tot

def grades_avg(grades):
    tot = grades_sum(grades)
    ave = tot/len(grades)
    return ave

#분산: 편차를 제곱해서 전체를 더한다 (편차제곱의 평균)
#분산이 얼마나 떨어져 있는지 눈에 확 띄게 잘 보여준다. 그래서 웬만한 작업은 분산을 쓴다.
def grades_variance(grades):
    #평균구하기
    ave = grades_avg(grades)
    vari = 0
    for su in grades:
        #편차제곱의합
        vari += (su-ave)**2
    #return vari/len(grades) #파이썬에서 할 때는 모집단으로 보고 전체개수를 나눈다.
    return vari/(len(grades)-1) #R에서는 표본집단으로 보고 자유도를 사용해서 파이썬이랑 답이 다르게 나온다.

#표준편차구하기
def grades_std(grades):
    return grades_variance(grades) ** 0.5 

print('합은', grades_sum(grades))
print('평균은', grades_avg(grades))
print('분산은', grades_variance(grades))
print('표준편차는', grades_std(grades))


print('---------------numpy사용-----------------')

import numpy

print('합은', numpy.sum(grades))
print('평균은', numpy.mean(grades))
print('분산은', numpy.var(grades))
print('표준편차는', numpy.std(grades))