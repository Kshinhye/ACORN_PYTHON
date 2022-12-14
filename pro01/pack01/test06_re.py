#정규표현식:다량의 데이터에서 원하는 데이터만 선택해서 처리할 때 효과적

import re

ss="12_1234 abc가나다abcABC_123555_6한국'Python is fun.'"
print(ss)
print(re.findall('123', ss))
print(re.findall(r'가나다', ss)) #raw string을 쓰는걸 권장합니다
print(re.findall(r'1', ss))
print(re.findall(r'[1-2]', ss)) #['1', '2', '1', '2', '1', '2']
print(re.findall(r'[0-9]', ss)) #숫자 전체 ['1', '2', '1', '2', '3', '4', '1', '2', '3', '5', '5', '5', '6']
print(re.findall(r'[0-9]+', ss)) #반복 #+:하나이상 ['12', '1234', '123555', '6']
print(re.findall(r'[0-9]{2}', ss)) #반복횟수 ['12', '12', '34', '12', '35', '55'
print(re.findall(r'[0-9]{2,3}', ss))#두개짜리 또는 세개짜리 ['12', '123', '123', '555']
print()
print(re.findall(r'[a-z]+', ss)) #['abc', 'abc', 'ython', 'is', 'fun']
print(re.findall(r'[A-Za-z]+', ss)) #['abc', 'abcABC', 'Python', 'is', 'fun']
print()
print(re.findall(r'[가-힣]+', ss)) #['가나다', '한국']
print(re.findall(r'[^가-힣]+', ss)) #부정: 한글만 빼고
print()
print(re.findall(r'12|34', ss)) #|(or) ['12', '12', '34', '12']
print(re.findall(r'.bc', ss)) #.는 아무거나 ['abc', 'abc']
print(re.findall(r'...', ss))
#구분
print(re.findall(r'[^1]+', ss)) #부정
print(re.findall(r'^1+', ss)) #첫글자가 1로 시작되는
print(re.findall(r"fun.'$", ss)) #끝나는
print()
print(re.findall(r'\d', ss)) #숫자
print(re.findall(r'\d+', ss))
print(re.findall(r'\d{1,3}', ss))
print(re.findall(r'\D', ss)) #숫자가 아닌 문자
print(re.findall(r'\s', ss)) #공백문자(스페이스,탭등)
print(re.findall(r'\S', ss))

print()
#flag주기
#IGNORECASE
p=re.compile('the', re.IGNORECASE) #객체를 만듬 #the 대소문자 구분하지 않겠다.
print(p)
print(p.findall('The dog the dog'))
print()
#MULTILINE
ss='''My name is tom.
I am happy'''
print(ss)
p=re.compile('^.+', re.MULTILINE)
print(p.findall(ss)) #['My name is tom.', 'I am happy']
