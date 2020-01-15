import requests
from bs4 import BeautifulSoup


def day_record():
    url = "http://192.168.2.147/cgi-bin/VideoSearchView.cgi"

    request = requests.get(url)
    soup = BeautifulSoup(request.content, "html5lib")

    soup = soup.find_all("script")
    script_tag = soup[-1].get_text().split()

    lines = []
    days_record = []

    for line in script_tag:
        lines.insert(1, line.replace('"', ''))
        day_record = '#669900' in line
        if day_record:
            days_record.insert(1, line.split('.')[0])

    # print(days_record)
    return days_record


def video_files(day, month, year):
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
    name=\"Save\"\r\n\r\n{}\r\n-----011000010111000001101001--\r\n".format(0, year, month, day, 00, 00, 00, 23, 59, 59, 1, 1, 0, 'Search')

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
    
    return files
