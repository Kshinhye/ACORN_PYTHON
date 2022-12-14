#집합형(묶음형) 자료: str, list, tuple, set, dict
#나중에 빛을 발하는 아이들입니다.

print('----------tuple----------')
#tuple: 순서O, 수정X
#list와 유사하나 읽기 전용이다. list보다 속도가 빠르다(다량의 데이터를 넣고 처리할 때 좋음)

t=('a','b','c','a')
t='a','b','c','a' #소괄호를 생략해도 가능하나 가독성을 위해 적는걸 권장

#순서
print(t,type(t),len(t),t.count('a'),t.index('b'))
print(t[0])

#수정불가
#t[0]='k' #err: 'tuple' object does not support item assignment
#수정을 하고 싶으면 형을 변경
imsi=list(t)
print(imsi,type(imsi))
imsi[0]='k'
t=tuple(imsi)
print(t)

##주의: 요소값이 단수일 경우에는 ,를 꼭 찍어라
print()
print((1),type((1))) #int
print((1,),type((1,))) #tuple

print()
t1=(10,20)
a,b=t1 #a랑 b가 나눠가짐
print(t1)
b,a=a,b #자리 바꿈
t2=a,b
print(t2)

print('---------- set ----------')
#set: 순서X, 중복X, 수정X(update를 이용해서 추가 가능)
a={1,2,3,1}
print(a,type(a),len(a)) #{1, 2, 3} <class 'set'> 3

b={3,4}
print(a.union(b)) #union(합집합) {1, 2, 3, 4}
print(a|b) #합집합
print(a.intersection(b)) #intersection(교집합) {3}
print(a&b) #교집합
print(a-b) #차집합 {1, 2}

print()
'''
print(a[0]) #err:'set' object is not subscriptable
a[0]=100 #err: 'set' object does not support item assignment
'''
#update 함수를 이용한 수정(추가) 가능
a.update({4,5})
a.update([6,7,8])
a.update((9,))
print(a)
#discard / remove 를 이용한 값에 의한 삭제
a.discard(3) #해당 값이 없으면 통과
a.remove(5) #해당 값이 없으면 에러 KeyError
print(a)
#clear : 홀랑 날리는거다~
c=set()
c=a #얕은카피
print(c)
a.clear()
print(a)
print(c)
#중복 없애기 이녀석 쓸모가 많다~
print()
li=[1,2,3,1,2,3]
print(li) #[1, 2, 3, 1, 2, 3]
imsi=set(li)
li=list(imsi)
print(li) #[1, 2, 3]

print('---------- dict ----------')
#{'key':'value'}
#dict(사전형): 순서X, key를 이용해 value참조
#방법1
my=dict(k1=1,k2='mbc',k3=3.4)
print(my,type(my))
#방법2
dic={'파이썬':'뱀',"자바":"커피",'스프링':'용수철','점수':[60,70,90]}
print(dic, type(dic),len(dic))
print(dic['자바'])
#print(dic[0]) #err:KeyError 순서가 없으니 당연하 에러
#추가
dic['오라클']='예언자'
print(dic)
#삭제1
del dic['오라클']
#삭제2(추출)
dic.pop('파이썬')
print(dic)
#수정
dic['자바']='웹용언어'
print(dic)

print(dic.keys())
print(dic.values())
print('파이썬' in dic) #False















