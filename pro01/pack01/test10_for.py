#반복문 for
#for 변수 in 집합형 자료:...
#target in object:

##list
#for i in [1,2,3,4,5]: #하나씩 뽑아내서 i가 받을거야
##tuple
#for i in (1,2,3,4,5):
##set
for i in {1,2,3,4,5}:
    print(i, end=' ')
print()
soft={'java':'웹용언어','python':'만능언어','MariaDB':'데이터처리'}

print(soft.items())
#list안에 items을 tuple로 처리
#dict_items([('java', '웹용언어'), ('python', '만능언어'), ('MariaDB', '데이터처리')])

#아이템 꺼내기
for i in soft.items():
    print(i)
    print(i[0]+':'+i[1])
print()
#키 꺼내기
for k in soft.keys():
    print(k)
print()
#값 꺼내기
for k in soft.values():
    print(k)
print()

li=['a','b','c']
for d in li:
    print(d)
    
#각각의 데이터에 인덱싱하기: enumerate(집합형 데이터 값)    
li=['a','b','c']
for idx, data in enumerate(li):
    print(idx,data)    
print()

print('\n평균, 분산, 표준편차 구하기')
jum=[6,5,4,7,3]
print(jum)

#평균
tot=0
for i in jum:
    tot+=i #tot는 i값을 누적
avg=tot/len(jum)
print('mean:',avg)

#분산
tot=0
for i in jum:
    # tot는 분산 #편차i-avg
    tot+=(i-avg)**2 #편차 제곱의 합

var=tot/len(jum)
print('var:',var) #분산:편차 제곱합의 평균
import math
print('std:',math.sqrt(var)) #표준편차1
print('std:',var**0.5) #표준편차2

print('------------------------------')
for n in [2,3]:
    print('---{}단---'.format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{}*{}={}'.format(n,i,n*i))

print()
datas=[1,2,3,4,5]
for i in datas:
    if i ==3: continue #3이면 for문으로 점프
    if i ==4: break #i가 4면 강제종료 print를 못만남
    print(i,end=' ')
else:
    print('정상 종료일 때 수행')
    
#for문 안에 if블럭
print()
jumsu=[95,70,60,50,100]
number=0
for jum in jumsu:
    number+=1 #첫번째라는 말이 익순하니 우선 1을 누적
    if jum<70:continue #합격 출력에서 제외
    print('%d번째 수험생은 합격' %number)
    
#다중 for문
print()
li1=[3,4,5]
li2=[0.5,1,2]
result=[]
for a in li1:
    for b in li2:
        #print(a+b, end=' ')
        result.append(a+b) #result에 담는 방법
print(result)

#comprehension
datas=[a+b for a in li1 for b in li2]
print(datas)

print('\n다량의 문자열 데이터 중 단어 수 출력')
import re
#web에서 가져왔다고 가정
ss='''5일 코로나19 신규확진자 수가 3만4739명을 기록했다.
위중증 환자와 사망자 등 방역 관련 모든 지표가 안정세다.
위중증 환자와 사망자 등 방역 관련 모든 지표가 안정세다.
위중증 환자와 사망자 위중증 환자와 사망자 위중증 환자와 사망자
전일보다 1420명 줄었다. 위중증 환자와 사망자 등 방역 관련 모든 지표가 안정세다.
이제 방역 관건은 코로나19 자체보다 독감이라는 말이 의료계에서 나온다.
3년만에 독감 유행이 예고됐으며 독감과 코로나19가 동시 유행할 경우 환자 중증도가 크게 올라갈 우려가 있어서다.
게다가 올해 유행할 독감은 독감 바이러스 중에서도 가장 강한 'A형 H3N2'다.
적극적 독감백신 접종이 필요하다는 것이 방역당국과 의료계 공통된 의견이다.
중앙방역대책본부는 이날 0시 기준 신규확진자 수가 3만4739명을 기록했다고 밝혔다.
이 가운데 해외 유입사례 69명을 제외한 국내 확진자 수는3만4670명이었다.
수도권에서 전체 국내 확진의 56.5% 비중인 1만9587명이 확진됐다.
'''
print(ss)
print()
ss2=re.sub(r'[^가-힣\s]', '', ss)#한글, 공백을 제외한 나머지는 날림('')
print(ss2)
ss3=ss2.split(' ') #공백을 기준으로 잘라보자
print(ss3)


cou={} #단어의 반생횟수를 dict로 저장
for i in ss3:
    if i in cou: #같은 단어가 있으면 
        cou[i]+=1 #누적
    else: #없다면
        cou[i]=1 #1을 준다
print(cou)
print()
for test_str in ['111-1234','일이삼-사오육칠','2232-1234']:
    if re.match(r'^\d{3,4}-\d{4}$', test_str): #맞냐아니냐
        print(test_str,'전화번호 맞아영')
    else:
        print(test_str,'음....')
#내장함수 sum 연습
print(sum([1,2,3]))

#
print('사전형 자료로 과일값 출력')
price={'사과':2000,'감':500,'배':1000}
guest={'사과':2,'감':3}
bill=sum(price[f]*guest[f] for f in guest)
print('총액:{}원'.format(bill))

print('-----comprehension 연습------')
temp=[1,2,3]
for i in temp:
    print(i,end=' ')
print()
print([i for i in temp]) #temp값을 하나씩 꺼내서 list로 반환 (타입을 적어줘야한다.)
print({i for i in temp}) #set type

temp2=list()
for i in temp:
    temp2.append(i+10)
print(temp2)
temp2=[i+10 for i in temp]
print(temp2)

print()
datas=[1,2,'a',True,3]
li=[i*i for i in datas if type(i)==int]
print(li)

print()
datas={1,1,2,2,2,3} #set type으로 주면 미리 중복값을 걸러서 준다
se = {i*i for i in datas}
print(se)

print()
id_name={1:'tom',2:'james'} #dict type
name_id={value:key for key,value in id_name.items()}
print(name_id)
