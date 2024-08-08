import time
import requests
import re
from selenium import webdriver
from lxml import etree

options = webdriver.EdgeOptions()
options.add_argument('--headless')

#国内超级ping
url = str(input('请填写域名:'))
my = webdriver.Edge(options=options)
my.get('https://www.itdog.cn/ping')
my.find_element('xpath','//*[@id="ip"]').send_keys(url)
my.find_element('xpath','//*[@id="screenshots"]/div/div/div/div[3]/div/div/div/div[1]/button[1]').click()
time.sleep(3)
html = my.page_source
xpath_html = etree.HTML(html)
#运营商
merchants = xpath_html.xpath('//*[@id="simpletable"]/tbody/tr/td[1]//text()')
merchant_list = []
test_list = []
i = 1
for one_data in merchants:
    one_data = one_data.replace('\n', '')
    one_data = one_data.replace('\t', '')
    if one_data:
        if i%2:
            merchant_list.append(one_data)
            i+=1
        else:
            test_list.append(one_data)
            i+=1

#检测点

#响应ip
request = re.findall('<div id="(.*?)" style="display:inline-block;">(.*?)</div>',html)
#ip地理位置
IP = re.findall('<td class="ip_address address-hidden" id="(.*?)" style="min-width:300px;" title="(.*?)">(.*?)</td>',html)




for i in range(0,100000):
    try:
        print('运营商:',merchant_list[i],end='')
        print('---检测点:',test_list[i],end='')
        print('---响应ip:', request[i][1], end='')
        print('---ip地理位置:', IP[i][2])

    except:
        break
print('检测结束')