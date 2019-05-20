import urllib.request
import re
import csv
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6756.400 QQBrowser/10.3.2545.400',
    'Connection':'keep-alive',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cookie':'_DM_SID_=2ee7424b9d76336f549c5910ff652279; Hm_lvt_5185a335802fb72073721d2bb161cd94=1540209209; _Z3nY0d4C_=37XgPK9h; JSESSIONID=B344BDEBBCD779A68507944A40EB76AC; f9big=ningbo1166; _DM_S_=233c9eb1959baa3e4ddd77aa01a77ca3; screen=1218; f19big=ip49; _dm_userinfo=%7B%22uid%22%3A0%2C%22stage%22%3A%22%22%2C%22city%22%3A%22%E6%B5%99%E6%B1%9F%3A%E6%9D%AD%E5%B7%9E%22%2C%22ip%22%3A%22115.192.32.72%22%2C%22sex%22%3A%222%22%2C%22frontdomain%22%3A%22ningbo.19lou.com%22%2C%22category%22%3A%22%E6%88%BF%E4%BA%A7%2C%E6%B1%82%E8%81%8C%2C%E6%97%B6%E5%B0%9A%2C%E6%95%B0%E7%A0%81%22%7D; pm_count=%7B%22pc_allCity_threadView_button_adv_190x205_1%22%3A13%7D; dayCount=%5B%7B%22id%22%3A78784%2C%22count%22%3A1%7D%5D; Hm_lvt_768876c24ee8384562c8812bd6191b4f=1540209215,1540274300,1540291740,1540362056; _dm_tagnames=%5B%7B%22k%22%3A%22%E5%AE%81%E6%B3%A2%E7%A7%9F%E6%88%BF%E8%AE%BA%E5%9D%9B%22%2C%22c%22%3A13%7D%2C%7B%22k%22%3A%22%E7%A7%9F%E6%88%BF%E7%BB%8F%E9%AA%8C%E5%88%86%E4%BA%AB%22%2C%22c%22%3A13%7D%2C%7B%22k%22%3A%221%E5%AE%A4%201%E5%8E%85%201%E5%8D%AB%201%E9%98%B3%E5%8F%B0%20%22%2C%22c%22%3A7%7D%2C%7B%22k%22%3A%2220%22%2C%22c%22%3A4%7D%2C%7B%22k%22%3A%22%E4%B8%AD%E5%B1%B1%E4%B8%9C%E8%B7%AF%E7%A6%8F%E6%98%8E%E8%B7%AF%E4%BA%A4%E5%8F%89%E5%8F%A3%22%2C%22c%22%3A4%7D%2C%7B%22k%22%3A%2215%22%2C%22c%22%3A1%7D%2C%7B%22k%22%3A%22%E6%B1%9F%E4%B8%9C%E4%B8%96%E7%BA%AA%E5%A4%A7%E9%81%93%E5%92%8C%E6%83%8A%E9%A9%BE%E8%B7%AF%E8%B7%AF%E5%8F%A3%22%2C%22c%22%3A1%7D%2C%7B%22k%22%3A%22cc%22%2C%22c%22%3A5%7D%2C%7B%22k%22%3A%22%E5%90%88%E7%A7%9F%22%2C%22c%22%3A4%7D%2C%7B%22k%22%3A%22%E5%BA%8A%22%2C%22c%22%3A4%7D%2C%7B%22k%22%3A%22%E9%9B%86%E7%BB%93%E5%8F%B7%22%2C%22c%22%3A4%7D%2C%7B%22k%22%3A%22cc%22%2C%22c%22%3A4%7D%2C%7B%22k%22%3A%22%E7%A7%9F%E6%88%BF%22%2C%22c%22%3A3%7D%2C%7B%22k%22%3A%22spa%22%2C%22c%22%3A3%7D%2C%7B%22k%22%3A%22%E6%8B%9B%E8%81%98%22%2C%22c%22%3A1%7D%2C%7B%22k%22%3A%22Calvin%22%2C%22c%22%3A1%7D%2C%7B%22k%22%3A%22%E7%BF%BB%E6%96%B0%E6%9C%BA%22%2C%22c%22%3A1%7D%2C%7B%22k%22%3A%22ck%22%2C%22c%22%3A1%7D%2C%7B%22k%22%3A%22%E4%BA%A4%E6%98%93%22%2C%22c%22%3A1%7D%2C%7B%22k%22%3A%224%E5%AE%A4%202%E5%8E%85%202%E5%8D%AB%202%E9%98%B3%E5%8F%B0%20%22%2C%22c%22%3A1%7D%5D; Hm_lpvt_768876c24ee8384562c8812bd6191b4f=1540362059',
    'Host':'ningbo.19lou.com',
    'Referer':'https://ningbo.19lou.com/forum-1996-thread-183351540274298747-1-1.html',
    'Upgrade-Insecure-Requests':1

}

second_href = []
second_href1 = []

def create_request(url):
    '''这个函数用来构建请求对象'''
    request = urllib.request.Request(url=url,headers=headers)
    return request

def send_request(request):
    '''这个函数用来发送请求'''
    response = urllib.request.urlopen(request).read()
    # response = response.decode('gbk', 'ignore')
    return response

def write_html_page(response,page_name):
    '''这个函数用来将爬取的网页写入文件'''
    # response = response.decode('gbk','ignore')
    with open('./detail/diyiji/%s'%(page_name),'wb+') as file:
        file.write(response)
def write_html_page1(response,page_name):
    '''这个函数用来将爬取的网页写入文件'''
    # response = response.decode('gbk','ignore')
    with open('./detail/xianqing/%s'%(page_name),'wb+') as file:

        file.write(response)

def tiqu_href(html):
    '''这个函数专门用来负责二级页面的超链接提取'''
    html = html.decode('utf-8','ignore')
    obj = re.findall(r' <a id=".*" class=".*" style=".*" href="(.*?)"  itemprop=".*" target=".*" title=".*">', html)
    # print(obj)
    second_href.extend(obj)
    # print(second_href)

def tiqu_href2(html):
    '''这个函数专门用来负责二级页面的数据的提取'''
    html = html.decode('gbk','ignore')
    obj = re.findall(r'<tr><th>.*?</th><td>\s+(.*?)\s+(.*?)\s+</td></tr>', html)
    try :
        for i in obj:
            for x in i:
                spar2_list = x.__str__()
                # print(type(spar2_list))
                second_href1.append(spar2_list)
            if '' in second_href1:
                second_href1.remove('')
        second_href1[1] = second_href1[1] + second_href1[2]
        del second_href1[2]
        second_href1[3] = second_href1[3] + second_href1[4]
        del second_href1[4]
        second_href1[11] = second_href1[11] + second_href1[12]
        del second_href1[12]
    except Exception as e:
        print(e)

def write_msg(data):
    '''这个函数用来将爬取的数据写入文件'''
    with open("./detail/xianqing/test1.csv", 'a+', newline='') as f:
        wf = csv.writer(f)
        wf.writerow(data)



if __name__ == '__main__':
    headers1 = ['房型', '户型', '区域', '建筑面积', '具体地址', '楼层', '朝向', '有效期', '租赁方式', '性别要求','最短租期', '租金', '付款要求', '押金要求','房屋来源', '建筑年代', '装修程度', '配套设施', '可入住时间', '特殊情况说明', '周边公交站点', '房源特点']
    with open('./detail/xianqing/test1.csv', 'a+') as f:
        wf = csv.writer(f)
        wf.writerow(headers1)
        f.close()
    for n in range(1,80):
        url = 'https://ningbo.19lou.com/forum-1996-'+str(n)+'.html'
        print(url)
        request = create_request(url)
        response = send_request(request)
        tiqu_href(response)
        write_html_page(response,'这是首页的内容')
        print(len(second_href))

        for i in range(0,len(second_href)):
            # print(second_href)
            url1 = 'http:'+str(second_href[i])
            print(url1)
            request1 = create_request(url1)

            response1 = send_request(request1)
            # print(type(response1))
            tiqu_href2(response1)
            # write_html_page1(response1, '这是%d页第%d条的内容'%(n,i))
            print('这是%d页第%d条的内容'%(n,i))
            write_msg(second_href1)
            second_href1.clear()
        second_href.clear()









