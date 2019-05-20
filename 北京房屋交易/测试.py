import urllib.request
import chardet


url = 'http://www.fang99.com/esf/index.aspx'

headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'ASP.NET_SessionId=0qi25s3cyvbty1gsw4pi4ome; sto-id-20480=AKJDKIMAFAAA',
'Host':'www.fang99.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2545.400'
}

request = urllib.request.Request(url=url,headers=headers)
# # response = urllib.request.urlopen(request).read().decode('utf-8','ignore')
response = urllib.request.urlopen(request).read()
chardet1 = chardet.detect(response)
print(chardet1['encoding'])
# print(response)
# with open('zzz', 'wb+') as file:
#     file.write(response)


# import requests
# response1 = requests.get(url=url,headers=headers).text
# print(response1)
