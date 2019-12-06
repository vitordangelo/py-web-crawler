import requests
from bs4 import BeautifulSoup

url = 'https://chaturbate.com'
r = requests.get(url)

# soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())

soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

# print(soup.title)

# print(soup.find_all('img'))

for link in soup.find_all('img'):
  print(link.get('src'))