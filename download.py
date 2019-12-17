import requests

url = 'http://192.168.2.143/sd2/2019-12-12/H20191212-232705NBN2P0.avi'
request = requests.get(url)

with open('/home/vitor/Documents/Apps/py-web-crawler/downloads/H20191212-232705NBN2P0.avi', 'wb') as f:
    f.write(request.content)

# Retrieve HTTP meta-data
print(request.status_code)
print(request.headers['content-type'])
print(request.encoding)
