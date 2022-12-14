# 멀티 프로세싱으로 웹 스크래핑
# https://beomi.github.io/beomi.github.io_old/

import requests #웹에 접근하기 위함
from bs4 import BeautifulSoup as bs #웹에있는 문서를 읽어다가 처리하기에 좋은 녀석
import time
from multiprocessing import Pool
from tornado.httputil import _get_content_range

def get_links(): # a tag의 주소 읽어보기
    data=requests.get("https://beomi.github.io/beomi.github.io_old/").text
    soup=bs(data,'html.parser') 
    #print(soup)
    my_titles=soup.select(
        ' h3>a '
        )
    data=[]
    
    for title in my_titles:
        data.append(title.get('href'))
        
    return data
        
def get_content(link): # a tag에 의한 해당 사이트 문서 내용 중 일부 문자값 읽기
    abs_link='https://beomi.github.io' + link
    #print(abs_link)
    req=requests.get(abs_link)
    html=req.text #문자열일 뿐이야
    soup=bs(html,'html.parser')
    
    #가져온 자료로 뭔가를 할 수 있겠지 그런데 우린 지금 그거까지는 갈 수 없어요. 얼마나 걸리는지 시간만 확인 할 거에요
    print(soup.select('h1')[0].text)

if __name__ =='__main__':
    start_time=time.time()
    # print(get_links())
    # print(len(get_links()))
    '''
    #직렬처리 : 약 0.9초 걸림(선생님pc보다 빠르당)
    #해당 사이트로 읽으러 가보자
    for link in get_links():
        get_coutent(link)
    '''
    #병렬처리(multiprocessiong) : 약0.7초 걸림
    pool=Pool(processes=4)
    pool.map(get_content, get_links()) #실행결과를 get함수에 전달한다.
    
    print('처리시간: {}'.format(time.time()-start_time))