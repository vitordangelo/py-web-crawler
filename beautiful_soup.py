import requests
from bs4 import BeautifulSoup

url = "http://192.168.2.143/cgi-bin/VideoSearchOpr.cgi"

headers = {
    "Content-Type": "multipart/form-data"
}

payload = {
    "sdcard": "1",
    "date": "2019",
    "date": "12",
    "date": "12",
    "stime": "00",
    "stime": "00",
    "stime": "00",
    "etime": "23",
    "etime": "59",
    "etime": "59",
    "type": "1",
	"channel": "1",
    "select_type": "0",
    "Save": "Search"
}

r = requests.post(url, data=payload, headers=headers)

# soup = BeautifulSoup(r.content, "html5lib")
# print(soup.prettify())

print(r.text)