import csv
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
fname = '네이버_인기웹툰순위.csv'
fObj = open(fname, mode='w', encoding='utf-8-sig', newline='') # 공백행 제외
# fObj = open(fname, mode='w', encoding='utf-8-sig', newline='') # 엑셀에서 읽을 때 한글 깨짐
writer = csv.writer(fObj)
title = '순위 인기순'.split()
print(title)
writer.writerow(title)

res = requests.get(url)
# print(res)

res.raise_for_status() # 읽기 실패하면 작업 중지

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
datas = soup.find('ol',attrs={'id':'realTimeRankFavorite'}).findAll('li')
# print(datas)

for i,row in enumerate(datas):
    cols = row.find('a')
    print(cols)
    # if len(cols) <= 1:continue  # [''] 해결
    data = '{}'.format(i+1),cols.get_text().strip() # .strip() 공백 제거를 해야함
    print(data)
    
    writer.writerow(data) # 데이터를 파일로 저장
    
fObj.close()