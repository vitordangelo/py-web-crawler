import requests

url = "http://192.168.2.143/cgi-bin/VideoSearchOpr.cgi"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"sdcard\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"date\"\r\n\r\n2019\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"date\"\r\n\r\n12\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"date\"\r\n\r\n12\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"stime\"\r\n\r\n00\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"stime\"\r\n\r\n00\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"stime\"\r\n\r\n00\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"etime\"\r\n\r\n23\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"etime\"\r\n\r\n59\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"etime\"\r\n\r\n59\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"channel\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"select_type\"\r\n\r\n0\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"Save\"\r\n\r\nSearch\r\n-----011000010111000001101001--\r\n"
headers = {
    'content-type': 'multipart/form-data; boundary=---011000010111000001101001'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
