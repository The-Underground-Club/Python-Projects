import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h3', {'class': 'gs-c-promo-heading__title'})

for t in title:
    print(t.getText())
