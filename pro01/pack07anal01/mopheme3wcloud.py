#웹문서에서 검색된 자료 스크래핑 후 형태소 분석하고난 다음 워드클라우드 작성
#donga.com 에서 검색 (깔끔해아주)

#pip install pygame
#pip install simplejson
#pip install pytagcloud

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
from konlpy.tag import Okt
from collections import Counter #카운팅 지원 모듈
import pytagcloud
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#keyword=input('검색어입력: ')
keyword="낙엽"
targetUrl="https://www.donga.com/news/search?query="+quote(keyword)
#print(targetUrl) #https://www.donga.com/news/search?query=%EB%82%99%EC%97%BD

source= urllib.request.urlopen(targetUrl)

soup=BeautifulSoup(source, 'lxml', from_encoding='utf-8')
#print(soup)

msg=""
#넘어온 애들중에 필요한 애들만 잡아떙길거야
for title in soup.find_all('p','tit'):
    title_link=title.select('a')
    #print(title_link) #a링크 전부 가져온다.
    
    articleUrl=title_link[0]['href'] #0번쨰의 href를 가져온다. (저기에 들어가야 긁어올 수 있으니까)
    #print(articleUrl)
    
    #들어가서 긁어볼게요
    #원래 위에도 써야해요 네트워크니까
    #여기는 내용이 없는 경우도 있으니 그럴때 에러를 발생시키려고 하는거에요
    try:
        source_article=urllib.request.urlopen(articleUrl)
        soup=BeautifulSoup(source_article,'lxml', from_encoding='utf-8')
        contents=soup.select('div.article_txt')
        #print('---------------------')
        #print(contents)
        
        for imsi in contents:
            item=str(imsi.find_all(text=True))
            #print(item)
            msg=msg+item #item만큼 누적됨
        
    except Exception:
        pass
#print(msg)

okt = Okt()
nouns = okt.nouns(msg)
results = []
for imsi in nouns:  #2글자 이상 명사만 작업에 참여하게
    if len(imsi) > 1:
        results.append(imsi)
        
print(results)
count = Counter(results) #빈도수 카운트
#tuple로 만들고 있어서 count를 쓴거야 list도 되요
tag = count.most_common(50) #빈도수 높은순 상위 50개만 가져옴
print(tag)

#워드클라우드
import pytagcloud
taglist=pytagcloud.make_tags(tag, maxsize=100) #maxsize(글씨 사이즈)
print(taglist)

#tag_image 생성 후 저장 #Chosun
pytagcloud.create_tag_image(taglist, output='워드클라우드.png', size=(1000,600),background=('white'),fontname="Lee", rectangular=False) #output=파일명

img=mpimg.imread('워드클라우드.png')
plt.imshow(img)
plt.show()