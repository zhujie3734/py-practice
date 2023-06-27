from urllib import request, response

url = 'http://www.baidu.com'
response = request.urlopen(url,timeout=1)
print(response.read().decode('utf-8'))

