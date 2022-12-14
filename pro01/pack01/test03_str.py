#집합형(묶음형) 자료: str, list, tuple, set, dict
#나중에 빛을 발하는 아이들입니다.

#str(문자열): 순서O(인덱싱,슬라이싱 가능), 수정X
#순서O: count,find,index ....
s='sequence'
print(s,type(s),len(s))
print(s.count('e')) #'e'의 개수를 반환
print(s.find('e'))#'e'가 처음으로 등장하는 인덱스를 반환/해당 문자를 찾지 못하면 -1을 반환
print(s.find('e'),'',s.find('e',3),s.rfind('e'))#r.find뒤에서 찾기
#수정X
ss='mbc'
print(ss,id(ss))
ss='abc' #수정이 아니라 참조 대상이 바뀜
print(ss,id(ss))
#순서O: 인덱싱, 슬라이싱
#인덱싱
print(s[0],s[3])#s[8] 없는경우 err
print(s[-1],s[-3])
#슬라이싱 대상[시작:끝:증가치]
print(s[0:3],s[3:],s[:3],s[:],s[1:5:1],s[::2])
print(s[-4:-1],s[-3:])
print('fre'+s[2:])

print()
s2='kbs mbc'
s2=' '+s2[:4]+'sbs '+s2[4:]+' '
print(s2,len(s2))
print(s2.strip()) #strip()좌우 공백을 자른다 #lstrip(), rstrip()
s3=s2.split(sep=' ') #sep(구분자) / 공백을 기준으로 잘라보자
print(s3)
print(':'.join(s3)) #iterable:집합형

a='Life is too long'
b=a.replace('Life', 'Your leg') #replace(대상, 뭘로 바꿀거야)
print(b)