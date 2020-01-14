import requests
from bs4 import BeautifulSoup

url = "http://192.168.2.147/cgi-bin/VideoSearchView.cgi"

request = requests.get(url)
soup = BeautifulSoup(request.content, "html5lib")

soup = soup.find_all("script")
script_tag = soup[-1].get_text().split()

lines = []
days_record = []

for line in script_tag:
    lines.insert(1, line.replace('"',''))
    day_record = '#669900' in line
    if day_record:
        days_record.insert(1, line.split('.')[0])

print(days_record)