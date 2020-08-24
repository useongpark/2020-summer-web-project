from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://news.naver.com/")

bsObject = BeautifulSoup(html, "html.parser")

for link in bsObject.find_all('a'):  #링크 가져오는 것
    print(link.text.strip(), link.get('href')) #hr 하이퍼링크

for link in bsObject.find_all('img'): #이미지 가져오는 것
    print(link.text.strip(), link.get('src'))


