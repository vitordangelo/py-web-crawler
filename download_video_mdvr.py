import requests
from bs4 import BeautifulSoup

url = "http://192.168.2.147/cgi-bin/VideoSearchOpr.cgi"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"sdcard\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"date\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"date\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"date\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"stime\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"stime\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"stime\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"etime\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"etime\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"etime\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"type\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"channel\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"select_type\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; \
    name=\"Save\"\r\n\r\n{}\r\n-----011000010111000001101001--\r\n".format(0, 2020, 1, 9, 00, 00, 00, 23, 59, 59, 1, 1, 0, 'Search')

headers = {
    'content-type': 'multipart/form-data; boundary=---011000010111000001101001'}

request = requests.post(url, data=payload, headers=headers)

soup = BeautifulSoup(request.content, "html5lib")

files = []

soup = soup.find_all('li')
for li in soup:
    url = li.find('a').get('href')
    file = li.get_text().split()
    object = {'name': file[0], 'file_size': float(file[1]),
              'date': file[3], 'time': file[4], 'path': url}
    files.insert(1, object)

def download(files):
    for file in files:
        file_path = "http://192.168.2.147{}".format(file['path'])
        with open('/home/vitor/Documents/Apps/py-web-crawler/downloads/{}'.format(file['name']), 'wb') as f:
            request = requests.get(file_path)
            f.write(request.content)
            print('File: {} complete'.format(file['name']))

download(files)