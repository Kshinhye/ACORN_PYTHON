# 여기서는 형태소 분석만 보여줄거에요
# 한글 형태소 지원 라이브러리 konlpy를 사용
# 5언 9품사로 한글 문서를 분리해준다.
# pip install --upgrade pip
# pip install jpype1
# pip install konlpy

from konlpy.tag import Kkma,Okt,Komoran

kkma = Kkma()
# .sentences 문장단위 분리
print(kkma.sentences('한글 데이터 형태소 분석을 위한 라이브러리 설치를 합니다 행운을 빕니다'))
# .nouns 명사만 분리
print(kkma.nouns('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 빕니다'))
# .pos 품사태깅함께
print(kkma.pos('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 빕니다'))
# .morphs 모든 품사
print(kkma.morphs('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 빕니다'))

print()
okt=Okt()
# .nouns 명사만 분리
print(okt.nouns('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 빕니다'))
# .pos 품사태깅함께
print(okt.pos('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 빕니다'))
# .morphs 품사 추출
print(okt.morphs('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 빕니다'))
# .phrases 어절 추출
print(okt.phrases('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 빕니다'))

print()
komo=Komoran()
# .nouns 명사만 분리
print(komo.nouns('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 빕니다'))
# .pos 품사태깅함께
print(komo.pos('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 빕니다'))
# .morphs 품사 추출
print(komo.morphs('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 빕니다'))