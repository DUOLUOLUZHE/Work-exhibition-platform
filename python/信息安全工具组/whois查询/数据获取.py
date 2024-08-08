import time
import requests
import re
from selenium import webdriver
from lxml import etree

options = webdriver.EdgeOptions()
options.add_argument('--headless')

url = 'https://www.whois365.com/cn'
place = str(input('输入域名:'))
my = webdriver.Edge(options=options)
my.get(url)
my.find_element('xpath','//*[@id="search"]').send_keys(place)
my.find_element('xpath','//*[@id="searchform"]/input[4]').click()
time.sleep(1)
html = my.page_source
off = re.findall('<span class="taken">(.*?)<br>',html)
if off:
   ip = re.findall('<a href="(.*?)" title="IP: (.*?) WHOIS">(.*?)</a>',html)[0][2]
   print('IP:',ip)
   print('注册局WHOIS主机:whois.verisign-grs.net')
   #one = re.findall('<p class="raw_data1">(.*)</p>', html)
   xpath_html = etree.HTML(html)
   one = xpath_html.xpath('//*[@id="whois-result"]/p[2]//text()')
   for one_data in one:
      one_data = one_data.replace('\n', '')
      print(one_data)
   print('注册商WHOIS主机:grs-whois.hichina.com')
   xpath_html = etree.HTML(html)
   two = xpath_html.xpath('//*[@id="whois-result"]/p[4]//text()')
   for two_data in two:
      two_data = two_data.replace('\n', '')
      print(two_data)
else:
    print('此域名未被注册！')
input()