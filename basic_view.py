import requests
from bs4 import BeautifulSoup

url = "http://192.168.2.147/cgi-bin/BasicView.cgi"

request = requests.post(url)
soup = BeautifulSoup(request.content, "html5lib")

# content = soup.prettify()

# with open('/home/vitor/Documents/Apps/py-web-crawler/html_code.html', 'w') as f:
#     f.write(content)

soup = soup.find_all("script")
script_tag = soup[-1].get_text().split()
print(script_tag)