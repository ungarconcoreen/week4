import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190715',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr ')



# 		# movie 안에 a 가 있으면,
#     if not movie.a == None:
# 				# a의 text를 찍어본다.
#         print (movie.a.text)

#
client = MongoClient ('localhost', 27017)
db = client.dbsparta


    # db.star.insert_one(doc)

data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190715')
soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody >tr')

rank = 0
# print(movies)
for movie in movies:
    if movie.a:
        rank = rank + 1
        doc = {}
        doc['rank'] = rank
        doc['title'] = movie.a.text
        doc['star'] = movie.select('td.point')[0].text
        db.mov2.insert_one(doc)



