import time
import requests
import re
from selenium import webdriver
from lxml import etree

options = webdriver.EdgeOptions()
options.add_argument('--headless')

place = str(input('域名:'))

url = 'https://icp.aizhan.com'

my = webdriver.Edge(options=options)
my.get(url)
my.find_element('xpath','//*[@id="domain"]').send_keys(place)
my.find_element('xpath','/html/body/div[4]/div[1]/div[2]/form/input[2]').click()
time.sleep(3)
html = my.page_source
data_list1 = re.findall('<td>(.*?)&nbsp;&nbsp;<a target="_blank" href="(.*?)" class="button">反查主办单位</a></td>',html)
print('-------------------备案信息----------------------')
print('主办单位名称:',data_list1[0][0])
print('反查主办单位:',data_list1[0][1])
xpath_html = etree.HTML(html)
data = xpath_html.xpath('//*[@id="icp-table"]/table/tbody//text()')
print('主办单位性质:',data[10])
print('网站备案/许可证号:',data[16])
data_list2 = re.findall('<a target="_blank" href="(.*?)" class="button">(.*?)</a>',html)
print('反查备案/许可证号:',data_list2[0][0])
print('审核时间:',data[24])
print('-------------------企业信息----------------------')
xpath_html2 = etree.HTML(html)
body = xpath_html2.xpath('//*[@id="tian"]/table/tbody/tr/td//text()')
i=1
for one_data in body[:-7]:
    if one_data[0:1] == "\n":
        pass
    else:
        if(i%2):
            print(one_data+':',end='')
            i+=1
        else:
            print(one_data)
            i+=1
# title_list = re.findall('<span class="gray">(.*?)</span>',html)
# print(title_list)
# title_list2 = re.findall('<span class="gray" style="width:74px">(.*?)</span>',html)
# print(title_list2)
# center_list = re.findall('<span>(.*?)</span>',html)
# print(center_list)