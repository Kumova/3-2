import requests
from bs4 import BeautifulSoup

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
KEYWORDS = ['дизайн', 'фото', 'веб', 'python']
url='https://habr.com/ru/all'

response = requests.get(url, headers=HEADERS)
response.raise_for_status()
text=response.text
soup=BeautifulSoup(text, features='html.parser')
posts = soup.find_all('article')


for post in posts:
    keywords=post.find_all(class_='tm-article-snippet__hubs-item')
    keywords=set(keyword.text.strip() for keyword in keywords)

    for keyword in keywords:
        if keyword in KEYWORDS:
            href=post.find(class_='tm-article-snippet__title-link').attrs['href']
            link=url+href
            time=post.find(class_='tm-article-snippet__datetime-published').text
            title=post.find('h2').find('span').text
            result=f" {time} - {title} - {link}"
            print(result)
            response=requests.get(link, headers=HEADERS)