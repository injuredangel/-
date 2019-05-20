
import requests
from bs4 import BeautifulSoup


url = 'http://www.bjjs.gov.cn/bjjs/fwgl/fdcjy/fwjy/index.shtml'
headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Cookie':'wdcid=55e47ea030f84764; _gscu_1677760547=4060476218oivg24; _gscbrs_1677760547=1; Hm_lvt_9ac0f18d7ef56c69aaf41ca783fcb10c=1540604763,1540621692; wdlast=1540624935; _gscs_1677760547=t406249357bbz3224|pv:1; Hm_lpvt_9ac0f18d7ef56c69aaf41ca783fcb10c=1540624935',
            'Host':'www.bjjs.gov.cn',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        }




response = requests.get(url=url,headers=headers).text
print(response)
# html_doc = BeautifulSoup(response,'lxml')






