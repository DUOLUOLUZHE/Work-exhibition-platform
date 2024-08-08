import requests
import re

ip = str(input("ip地址为:"))
url = 'https://ip.tool.chinaz.com/'+str(ip)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
}

#信息搜集
html = requests.get(url=url,headers=headers).text
place = re.findall('<em id="infoLocation">(.*?)</em>',html)[0]
print('现实地址:',place)
math = re.findall('<span class="Whwtdhalf w15-0 lh45">(.*?)</span>',html)[1]
print('数字地址:',math)
buyer = re.findall('<span class="Whwtdhalf w15-0 lh45">(.*?)</span>',html)[2]
print('运营商:',buyer)
