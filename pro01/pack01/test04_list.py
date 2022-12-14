#집합형(묶음형) 자료: str, list, tuple, set, dict
#나중에 빛을 발하는 아이들입니다.

#list: 순서O, 수정O
#배열 비슷하지만 배열하고 달라 얘는 아무거나 때려넣을 수 있다.

a=[1,2,3];b=[10,a,12.5,True,'문자열']
print(a,type(a),id(a))
print(b,type(b),id(b))
aa=[] #묵시적 list타입
bb=list() #명시적 list타입 
print(type(aa),type(bb)) 

print('-------- 수정 --------')
#수정(추가): append / insert / extend / +=
family=['엄마','아빠','나','여동생']
family.append('남동생') #append(추가): 늘 맨 뒤에
family.insert(0, '할아버지') #insert(삽입): 지정 가능
family.extend(['삼촌','조카']) #extend(복수 추가)
family +=['이모','고모'] #+=
#수정(제거): remove(value), del[index]
family.remove('남동생')
del family[2]
#del family #변수를 삭제

print('-------- 순서 --------')
#순서
print(family[2]) #인덱싱:나
print(family[0:2]) #슬라이싱:엄마,아빠
print(family,len(family))
print(family.index('나')) #나 몇번째니
print('엄마' in family,'할머니' in family) # True False

aa=[1,2,3,['a','kbs','c'],4,5] #중첩 리스트
print(aa)
print(aa[0])
print(aa[3])
print(aa[3][1])

print(id(aa))
aa[0]=333 #요소값 수정 가능
print(aa,id(aa))

#자료구조 트리/디자인패턴 공부하세요.
aa2=['123','34','234']
print(aa2)
aa2.sort() #sort(정렬) ascending
print(aa2)
aa2.sort(key=int, reverse=True) #sort(정렬) descending
print(aa2)
print()
print('-------- 복사 --------')
#복사
name=['소현','현성','다정']
print(name)
name2=name #주소 치환(얕은 복사) 별명을 하나 더 가진 셈
print(id(name),id(name2)) #주소가 같음

import copy
name3=copy.deepcopy(name) #깊은 복사: 새로운 객체로 생성
print(id(name),id(name2),id(name3)) #name3만 주소 다름
name[0]='용환'
print(name) #바뀜
print(name2) #바뀜
print(name3) #안바뀜
print()
#참고------------------------------
print('-------- stack, queue --------')
#stack(LiFO) 구조 (세로 통 맨 밑에가 막혀있음)
sbs=[1,2,3]
sbs.append(4) #맨 위에 들어가는 구조
print(sbs)
sbs.pop() #pop()맨 위에부터 빠져나감
print(sbs)
sbs.pop()
print(sbs)
print()
#queue(FiFO) 구조 (파이프 구조)
sbs=[1,2,3]
sbs.append(4)
sbs.pop(0) #첫번째 부터 빠져나감
print(sbs)
sbs.pop(0)
print(sbs)


