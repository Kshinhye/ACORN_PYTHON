# Matplotlib
# - http://matplotlib.org
# - 플로팅 라이브러리로 matplotlib.pyplot 모듈을 사용하여 그래프 등의 시각화 가능.
# - 그래프 종류 : line, scatter, contour(등고선), surface, bar, histogram, box, ...
# - Figure
#
# 모든 그림은 Figure라 부르는 matplotlib.figure.Figure 클래스 객체에 포함.
# 내부 plot이 아닌 경우에는 Figure는 하나의 아이디 숫자와 window를 갖는다.
# figure()를 명시적으로 적으면 여러 개의 윈도우를 동시에 띄우게 된다.

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic') #한글깨짐 #malgun gothic
plt.rcParams['axes.unicode_minus']=False # 한글이 있을 때 - 기호 깨짐

# x=['서울','수원','인천'] #[0,1,2] #문자는 시각화 할 수 없다. 얘는 list 자료 안에 있으므로 인덱스로 들어간다. 
# y=[5,3,7]
# plt.xlim([-2,3])  #x축 : 최솟값 -1, 최댓값 3
# plt.ylim([0,10])  #y축 
#
# plt.plot(x,y)
# plt.yticks(list(range(-3,11,3))) #tick값 0부터 11까지/ 표식은 3단위
# plt.show()

# #y축 value x축 범주
# data = np.arange(1,11,2)
# print(data)
# plt.plot(data) #그냥 data하나만 주면 첫번째값은 y축이된다.
# #구간 값 찍어보기
# x=[0,1,2,3,4]
# for a,b in zip(x,data):  #zip() : 쌍을 만들어주는 함수
#     #print(a,b) 
#     plt.text(a,b,str(b)) #선위에 숫자가 적혀있음
#
# plt.show()

# x=np.arange(10)
# y=np.sin(x)
# print(x,y)
# plt.plot(x,y,'yo--',linewidth=2) #'bo'파란점 'r+' 빨간십자가
# plt.show()

# hold : 복수의 차트를 하나의 영역에 겹쳐서 출력
x=np.arange(0,np.pi*3,0.1) #0.1은 증가치
y_sin=np.sin(x)
y_cos=np.cos(x)

plt.plot(x,y_sin,'r')
plt.plot(x,y_cos,'b')
plt.title('사인 & 코사인')
plt.legend(['사인','코사인'])  #범례
plt.show()

# 이번에는 쪼개볼게
# subplot : figure를 여러개로 나눔
plt.subplot(2,1,1) #2행1열(1부터 출발) #나는1행에 있어요
plt.plot(x,y_sin,'r')
plt.subplot(2,1,2) #2행1열(1부터 출발) #나는1행에 있어요
plt.plot(x,y_cos)
plt.show()

#꺾은 선 그래프
irum='a','b','c','d','e'
kor=[80,50,70,70,90]
eng=[60,70,80,70,60]

plt.plot(irum,kor,'ro-') #빨간색 동그라미 실선 
plt.plot(irum,eng,'gs--') #초록색 스퀘어 점선
plt.ylim([0,100])
plt.legend(['국어','영어'],loc=3) #legend() 범례, loc=위치 1234 시계 반대방향으로 돌아가고 안쓰면 지가 베스트 찾음
plt.grid(True)

fig=plt.gcf() #저장할거야!!
plt.show()
fig.savefig('차트.png') #보여준걸 저장하기때문에 show뒤에 저장!

#저장한거 불러와볼까
from matplotlib.pyplot import imread
img=imread('차트.png')
plt.imshow(img)
plt.show()
