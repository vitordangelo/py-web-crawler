import requests
from bs4 import BeautifulSoup

url = "http://192.168.2.143/cgi-bin/VideoSearchOpr.cgi"

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
    name=\"Save\"\r\n\r\n{}\r\n-----011000010111000001101001--\r\n".format(1, 2019, 12, 12, 00, 00, 00, 23, 59, 59, 1, 1, 0, 'Search')

headers = {
    'content-type': 'multipart/form-data; boundary=---011000010111000001101001'}

response = requests.post(url, data=payload, headers=headers)

soup = BeautifulSoup(response.content, "html5lib")

url_list = []

def list_url():
    for link in soup.find_all('a'):
        link = link.get('href')
        url_list.insert(1, 'http://192.168.2.143' + link)

def name_file(url):
    file_name = url.split('/')
    return file_name[5]

list_url()

for url in url_list:
    file_name = name_file(url)
    with open('/home/vitor/Documents/Apps/py-web-crawler/downloads/'+file_name, 'wb') as f:
        request = requests.get(url)
        f.write(request.content)
        print('File: {} complete'.format(url))

        total = response.headers.get('content-length')
        for data in request.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
            downloaded += len(data)
            print(downloaded)


print('TCHAU')