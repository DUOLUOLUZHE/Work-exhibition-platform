import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import requests
import re
import time
from selenium import webdriver
from lxml import etree
import threading
import multiprocessing








class my_window(QWidget):
    def __init__(self):
        super(my_window, self).__init__()
        # 创建类变量
        # ip查询变量
        self.ip_place = ''
        self.ip_math = ''
        self.ip_buyer = ''
        self.format()



    #框架布局

    def format(self):
        # 创建其他类实例
        self.win1 = window1()
        self.win2 = window2()
        self.win3 = window3()
        self.win4 = window4()
        self.win5 = window5()
        # 设置窗口大小
        self.resize(1800,900)
        # 设置窗口标题
        self.setWindowTitle("鬼眼系统")
        # 整体布局方式
        all_format = QHBoxLayout()
        #组件调用
        self.ip()
        self.area()
        self.whois()
        self.whois2()
        self.super_ping()

        #左屏幕
        part_format = QVBoxLayout()
        #第一层
        #创建外部盒子
        box = QGroupBox()
        box.setLayout(self.all_ip)

        # 第二层
        # 创建外部盒子
        box2 = QGroupBox()
        box2.setLayout(self.all_area)

        # 第三层
        # 创建外部盒子
        box3 = QGroupBox()
        box3.setLayout(self.all_whois)

        # 第三层
        # 创建外部盒子
        box4 = QGroupBox()
        box4.setLayout(self.all_whois2)

        # 将组添加到整体容器中
        part_format.addWidget(box)
        part_format.addWidget(box2)
        part_format.addWidget(box3)
        part_format.addWidget(box4)

        #右屏幕
        right_part_format = QVBoxLayout()
        # 第一层
        # 创建外部盒子
        box = QGroupBox()
        box.setLayout(self.all_ping)

        # 将组添加到整体容器中
        right_part_format.addWidget(box)

        #创建水平布局器综合全部组件
        every = QGroupBox()
        every.setLayout(part_format)
        every2 = QGroupBox()
        every2.setLayout(right_part_format)
        all_format.addWidget(every)
        all_format.addWidget(every2)

        # 设置窗口显示的容器
        self.setLayout(all_format)

    def ip(self):
        # 整体布局方式
        self.all_ip = QVBoxLayout()
        # 第一组
        top_box = QGroupBox()
        # 建立水平容器
        one_box = QHBoxLayout()
        lift_module = QLabel('ip地址:')
        font = QFont()
        font.setPointSize(16)
        lift_module.setFont(font)
        self.center_module_ip = QLineEdit('请输入查询ip')
        right_module = QPushButton('查询')
        #添加按钮触发事件
        right_module.clicked.connect(self.ip_find)
        # 将组件添加到水平容器中
        one_box.addWidget(lift_module)
        one_box.addWidget(self.center_module_ip)
        one_box.addWidget(right_module)
        # 将第一组添加入窗口
        top_box.setLayout(one_box)
        # 第二组
        top_two_box = QGroupBox()
        # 建立水平容器
        one2_box = QHBoxLayout()
        lift_module = QLabel('现实地址:')
        font = QFont()
        font.setPointSize(16)
        lift_module.setFont(font)
        self.ip_place_right_module = QLabel(self.ip_place)
        # 将组件添加到水平容器中
        one2_box.addWidget(lift_module)
        one2_box.addWidget(self.ip_place_right_module)
        # 将第一组添加入窗口
        top_two_box.setLayout(one2_box)
        # 第三组
        top_three_box = QGroupBox()
        # 建立水平容器
        one3_box = QHBoxLayout()
        lift_module = QLabel('数字地址:')
        font = QFont()
        font.setPointSize(16)
        lift_module.setFont(font)
        self.ip_math_right_module = QLabel(self.ip_math)
        # 将组件添加到水平容器中
        one3_box.addWidget(lift_module)
        one3_box.addWidget(self.ip_math_right_module)
        # 将第一组添加入窗口
        top_three_box.setLayout(one3_box)
        # 第四组
        top_four_box = QGroupBox()
        # 建立水平容器
        one4_box = QHBoxLayout()
        lift_module = QLabel('运营商:')
        font = QFont()
        font.setPointSize(16)
        lift_module.setFont(font)
        self.ip_buyer_right_module = QLabel(self.ip_buyer)
        # 将组件添加到水平容器中
        one4_box.addWidget(lift_module)
        one4_box.addWidget(self.ip_buyer_right_module)
        # 将第一组添加入窗口
        top_four_box.setLayout(one4_box)
        # 将组添加到整体容器中
        self.all_ip.addWidget(top_box)
        self.all_ip.addWidget(top_two_box)
        self.all_ip.addWidget(top_three_box)
        self.all_ip.addWidget(top_four_box)

    def area(self):
        # 整体布局方式
        self.all_area = QVBoxLayout()

        #第一组
        top_box = QGroupBox()
        #建立水平容器
        one_box = QHBoxLayout()
        lift_module = QLabel('域名:')
        font = QFont()
        font.setPointSize(16)
        lift_module.setFont(font)
        self.center_module_areaname = QLineEdit('请输入查询域名')
        right_module = QPushButton('查询')
        #添加点击事件
        right_module.clicked.connect(lambda:self.redly(self.center_module_areaname.text()))
        #将组件添加到水平容器中
        one_box.addWidget(lift_module)
        one_box.addWidget(self.center_module_areaname)
        one_box.addWidget(right_module)
        #将第一组添加入窗口
        top_box.setLayout(one_box)

        # 第二组
        top2_box = QGroupBox()
        # 建立水平容器
        two_box = QHBoxLayout()
        lift1_module = QLabel('IP:')
        font = QFont()
        font.setPointSize(16)
        lift1_module.setFont(font)
        self.IP_right_module = QLabel(self.win1.Ip)

        # 将组件添加到水平容器中
        two_box.addWidget(lift1_module)
        two_box.addWidget(self.IP_right_module)
        # 将第一组添加入窗口
        top2_box.setLayout(two_box)

        # 设置窗口显示的容器
        self.all_area.addWidget(top_box)
        self.all_area.addWidget(top2_box)

    def whois(self):
        #创建水平布局器
        self.all_whois = QHBoxLayout()

        #创建滚动对象
        scrool = QScrollArea()
        scrool2 = QScrollArea()


        # 第一组
        self.widget1 = QWidget()
        self.widget1.setStyleSheet("background-color:black;")

        scrool.setWidget(self.win1.zero_data)

        layout_format = QVBoxLayout()
        layout_format.addWidget(scrool)

        # 第二组
        self.widget2 = QWidget()
        self.widget2.setStyleSheet("background-color:black;")

        scrool2.setWidget(self.win2.zero_data)

        layout_format2 = QVBoxLayout()
        layout_format2.addWidget(scrool2)

        box = QGroupBox()
        box.setLayout(layout_format)
        box.setStyleSheet("background-color:black;color:white;")
        box2 = QGroupBox()
        box2.setLayout(layout_format2)
        box2.setStyleSheet("background-color:black;color:white;")

        # 将第一组添加入窗口
        self.all_whois.addWidget(box)
        self.all_whois.addWidget(box2)

    def whois2(self):
        #创建水平布局器
        self.all_whois2 = QHBoxLayout()


        #创建滚动对象
        scroll = QScrollArea()
        scroll2 = QScrollArea()



        # 第一组
        widget1 = QWidget()
        widget1.setStyleSheet("background-color:black;color:white;")

        scroll.setWidget(self.win3.zero_data)

        layout_format = QVBoxLayout()
        layout_format.addWidget(scroll)



        # 第二组
        widget2 = QWidget()
        widget2.setStyleSheet("background-color:black;color:white;")

        scroll2.setWidget(self.win4.zero_data)

        layout_format2 = QVBoxLayout()
        layout_format2.addWidget(scroll2)

        #建立盒子
        box = QGroupBox()
        box.setLayout(layout_format)
        box.setStyleSheet("background-color:black;color:white;")
        box2 = QGroupBox()
        box2.setLayout(layout_format2)
        box2.setStyleSheet("background-color:black;color:white;")

        # 将第一组添加入窗口
        self.all_whois2.addWidget(box)
        self.all_whois2.addWidget(box2)

    def super_ping(self):
        # 整体布局方式
        self.all_ping = QVBoxLayout()

        # 创建一个 滚动对象
        scroll = QScrollArea()
        scroll.setStyleSheet("background-color:black;color:white;")

        # 第一组
        one_box = QGroupBox()
        # 建立水平容器
        one_one_box = QHBoxLayout()
        lift_format = QLabel('超级ping:')
        font = QFont()
        font.setPointSize(16)
        lift_format.setFont(font)
        self.right_format_super_ping = QLineEdit('请输入域名或ip')
        self.center_module = QPushButton('开始')
        #添加点击事件
        self.center_module.clicked.connect(lambda:self.win5.whois_find(self.right_format_super_ping.text()))
        # 将组件添加到水平容器中
        one_one_box.addWidget(lift_format)
        one_one_box.addWidget(self.right_format_super_ping)
        one_one_box.addWidget(self.center_module)
        # 将容器插入第一组中
        one_box.setLayout(one_one_box)



        #创建第二组内容
        widget2 = QWidget()
        widget2.setStyleSheet("background-color:black;color:white;")


        scroll.setWidget(self.win5.zero_data)

        layout2 = QVBoxLayout()
        layout2.addWidget(scroll)
        # 将组插入整体布局中
        self.all_ping.addWidget(one_box)
        self.all_ping.addLayout(layout2)

    #触发函数
    #整体触发
    def redly(self,domin):
        print(domin)
        self.win1.whois_find(domin,self.IP_right_module,self.win1)
        self.win3.whois_find(domin)
        self.win4.whois_find(domin)
        self.win2.whois_find(domin)
        # self.domin1 = domin
        #
        #
        # self.t1 = threading.Thread(target=self.win1.whois_find,args=(self.domin1,))#self.IP_right_module,self.win1,))
        # self.t2 = threading.Thread(target=self.win2.whois_find,args=(self.domin1,))
        # self.t3 = threading.Thread(target=self.win3.whois_find,args=(self.domin1,))
        # self.t4 = threading.Thread(target=self.win4.whois_find,args=(self.domin1,))
        # self.t1.start()
        # self.t2.start()
        # self.t3.start()
        # self.t4.start()



    #ip查询
    def ip_find(self):
        ip = self.center_module_ip.text()
        print(ip)
        url = 'https://ip.tool.chinaz.com/' + str(ip)
        # 信息搜集
        html = requests.get(url=url).text
        self.ip_place = re.findall('<em id="infoLocation">(.*?)</em>', html)[0]
        self.ip_math = re.findall('<span class="Whwtdhalf w15-0 lh45">(.*?)</span>', html)[1]
        self.ip_buyer = re.findall('<span class="Whwtdhalf w15-0 lh45">(.*?)</span>', html)[2]
        #更新信息
        self.ip_place_right_module.setText(self.ip_place)
        self.ip_place_right_module.repaint()
        self.ip_math_right_module.setText(self.ip_math)
        self.ip_math_right_module.repaint()
        self.ip_buyer_right_module.setText(self.ip_buyer)
        self.ip_buyer_right_module.repaint()






class window1(QWidget):
    def __init__(self):
        super(window1, self).__init__()
        self.zero_data = QLabel('注册局WHOIS主机:whois.verisign-grs.net',self)
        self.zero_data.resize(1800, 20)
        font = QFont()
        font.setPointSize(16)
        self.zero_data.setFont(font)
        self.setStyleSheet("background-color:black;color:white;")
        self.Ip = ''


    #whois查询
    def whois_find(self,areaname,IP_right_module,win1):
        print(areaname)
        # print(IP_right_module)
        # 清空操作
        self.zero_data.setText("")
        self.zero_data.repaint()

        self.data_list = []

        self.data_list.append('注册局WHOIS主机:whois.verisign-grs.net')
        self.zero_data.setText("<br>".join(self.data_list))
        self.zero_data.resize(1800, 20)
        self.zero_data.repaint()

        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        url = 'https://www.whois365.com/cn'

        place = areaname
        my = webdriver.Edge(options=options)
        my.get(url)
        my.find_element('xpath', '//*[@id="search"]').send_keys(place)
        my.find_element('xpath', '//*[@id="searchform"]/input[4]').click()
        time.sleep(1)
        html = my.page_source
        off = re.findall('<span class="taken">(.*?)<br>', html)
        if off:
            self.Ip = re.findall('<a href="(.*?)" title="IP: (.*?) WHOIS">(.*?)</a>', html)[0][2]

            print('IP:', self.Ip)
            print('注册局WHOIS主机:whois.verisign-grs.net')
            # one = re.findall('<p class="raw_data1">(.*)</p>', html)
            xpath_html = etree.HTML(html)
            one = xpath_html.xpath('//*[@id="whois-result"]/p[2]//text()')
            for one_data in one:
                self.one_data = one_data.replace('\n', '')
                self.data_list.append(self.one_data)
                self.zero_data.setText("<br>".join(self.data_list))
                self.zero_data.resize(1800, self.zero_data.frameSize().height() + 20)
                self.zero_data.repaint()
            print('注册商WHOIS主机:grs-whois.hichina.com')


        else:
            self.data_list.append('此域名未被注册！')
            self.zero_data.setText("<br>".join(self.data_list))
            self.zero_data.resize(1800, 40)
            self.zero_data.repaint()

        IP_right_module.setText(win1.Ip)
        IP_right_module.repaint()

class window2(QWidget):
    def __init__(self):
        super(window2, self).__init__()
        self.zero_data = QLabel('注册商WHOIS主机:grs-whois.hichina.com',self)
        self.zero_data.resize(1800, 20)
        font = QFont()
        font.setPointSize(16)
        self.zero_data.setFont(font)
        self.setStyleSheet("background-color:black;color:white;")

    #whois查询
    def whois_find(self,areaname):
        # 清空操作
        self.zero_data.setText("")
        self.zero_data.repaint()

        self.data_list = list()

        self.data_list.append('注册商WHOIS主机:grs-whois.hichina.com')
        self.zero_data.setText("<br>".join(self.data_list))
        self.zero_data.resize(1800, 20)
        self.zero_data.repaint()

        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        url = 'https://www.whois365.com/cn'
        place = areaname
        my = webdriver.Edge(options=options)
        my.get(url)
        my.find_element('xpath', '//*[@id="search"]').send_keys(place)
        my.find_element('xpath', '//*[@id="searchform"]/input[4]').click()
        time.sleep(1)
        html = my.page_source
        off = re.findall('<span class="taken">(.*?)<br>', html)
        if off:
            ip = re.findall('<a href="(.*?)" title="IP: (.*?) WHOIS">(.*?)</a>', html)[0][2]
            print('IP:', ip)
            print('注册局WHOIS主机:whois.verisign-grs.net')
            # one = re.findall('<p class="raw_data1">(.*)</p>', html)
            xpath_html = etree.HTML(html)
            one = xpath_html.xpath('//*[@id="whois-result"]/p[2]//text()')
            for one_data in one:
                one_data = one_data.replace('\n', '')
                # self.data_list.append(one_data)
                # self.zero_data.setText("<br>".join(self.data_list))
                # self.zero_data.resize(420, self.zero_data.frameSize().height() + 20)
                # self.zero_data.repaint()
            print('注册商WHOIS主机:grs-whois.hichina.com')
            xpath_html = etree.HTML(html)
            two = xpath_html.xpath('//*[@id="whois-result"]/p[4]//text()')
            for two_data in two:
                self.two_data = two_data.replace('\n', '')
                self.data_list.append(two_data)
                self.zero_data.setText("<br>".join(self.data_list))
                self.zero_data.resize(1800, self.zero_data.frameSize().height() + 20)
                self.zero_data.repaint()
        else:
            self.data_list.append('此域名未被注册！')
            self.zero_data.setText("<br>".join(self.data_list))
            self.zero_data.resize(1800, self.zero_data.frameSize().height() + 20)
            self.zero_data.repaint()
class window3(QWidget):
    def __init__(self):
        super(window3, self).__init__()
        self.zero_data = QLabel("备案信息",self)
        self.zero_data.resize(1800,20)
        font = QFont()
        font.setPointSize(16)
        self.zero_data.setFont(font)
        self.setStyleSheet("background-color:black;color:white;")

    def whois_find(self,areaname):
        # 清空操作
        self.zero_data.setText("")
        self.zero_data.repaint()

        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        self.data_list = []

        self.data_list.append('备案信息')
        self.zero_data.setText("<br>".join(self.data_list))
        self.zero_data.resize(1800, 20)
        self.zero_data.repaint()

        place = areaname

        url = 'https://icp.aizhan.com'

        my = webdriver.Edge(options=options)
        my.get(url)
        my.find_element('xpath', '//*[@id="domain"]').send_keys(place)
        my.find_element('xpath', '/html/body/div[4]/div[1]/div[2]/form/input[2]').click()
        time.sleep(3)
        html = my.page_source
        data_list1 = re.findall('<td>(.*?)&nbsp;&nbsp;<a target="_blank" href="(.*?)" class="button">反查主办单位</a></td>',html)
        self.data_list.append("主办单位名称:" + data_list1[0][0])
        self.zero_data.setText("<br>".join(self.data_list))
        self.zero_data.resize(1800, self.zero_data.frameSize().height() + 20)
        self.zero_data.repaint()
        self.data_list.append('反查主办单位:' + str(data_list1[0][1]))
        self.zero_data.setText("<br>".join(self.data_list))
        self.zero_data.resize(1800, self.zero_data.frameSize().height() + 20)
        self.zero_data.repaint()
        xpath_html = etree.HTML(html)
        data = xpath_html.xpath('//*[@id="icp-table"]/table/tbody//text()')
        self.data_list.append('主办单位性质:' + data[10])
        self.zero_data.setText("<br>".join(self.data_list))
        self.zero_data.resize(1800, self.zero_data.frameSize().height() + 20)
        self.zero_data.repaint()
        self.data_list.append('网站备案/许可证号:' + data[16])
        self.zero_data.setText("<br>".join(self.data_list))
        self.zero_data.resize(1800, self.zero_data.frameSize().height() + 20)
        self.zero_data.repaint()
        data_list2 = re.findall('<a target="_blank" href="(.*?)" class="button">(.*?)</a>', html)
        self.data_list.append('反查备案/许可证号:' + data_list2[0][0])
        self.zero_data.setText("<br>".join(self.data_list))
        self.zero_data.resize(1800, self.zero_data.frameSize().height() + 20)
        self.zero_data.repaint()
        self.data_list.append('审核时间:' + data[24])
        self.zero_data.setText("<br>".join(self.data_list))
        self.zero_data.resize(1800, self.zero_data.frameSize().height() + 20)
        self.zero_data.repaint()



class window4(QWidget):
    def __init__(self):
        super(window4, self).__init__()
        self.zero_data = QLabel('企业信息',self)
        font = QFont()
        font.setPointSize(16)
        self.zero_data.setFont(font)
        self.zero_data.resize(1800,20)
        self.setStyleSheet("background-color:black;color:white;")

    def whois_find(self,areaname):
        #清空操作
        self.zero_data.setText("")
        self.zero_data.repaint()

        self.data_list = []

        self.data_list.append('企业信息')
        self.zero_data.setText("<br>".join(self.data_list))
        self.zero_data.resize(1800,0)
        self.zero_data.repaint()

        one_list = []
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')

        place = areaname

        url = 'https://icp.aizhan.com'

        my = webdriver.Edge(options=options)
        my.get(url)
        my.find_element('xpath', '//*[@id="domain"]').send_keys(place)
        my.find_element('xpath', '/html/body/div[4]/div[1]/div[2]/form/input[2]').click()
        time.sleep(3)
        html = my.page_source
        xpath_html2 = etree.HTML(html)
        body = xpath_html2.xpath('//*[@id="tian"]/table/tbody/tr/td//text()')
        i = 1
        for one_data in body:
            if one_data[0:1] == "\n":
                pass
            else:
                if (i % 2):
                    one_list.append(one_data + ':')
                    i += 1
                else:
                    one_list.append(one_data)
                    i += 1
        i = 0
        string_data = ''
        for data in one_list:
            if i == 0:
                string_data = string_data +data
                i+=1
                continue

            if i == 1:
                string_data = string_data + data
                self.data_list.append(string_data)
                self.zero_data.setText("<br>".join(self.data_list))
                self.zero_data.resize(1800, self.zero_data.frameSize().height() + 20)
                self.zero_data.repaint()
                i=0
                string_data=''
                continue


class window5(QWidget):
    def __init__(self):
        super(window5, self).__init__()
        self.zero_data = QLabel('',self)
        self.zero_data.resize(1800, 20)
        font = QFont()
        font.setPointSize(16)
        self.zero_data.setFont(font)
        self.setStyleSheet("background-color:black;color:white;")

    def whois_find(self,areaname):
        self.zero_data.setText("")
        self.zero_data.repaint()

        self.data_list = []
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')

        # 国内超级ping
        url = areaname
        my = webdriver.Edge(options=options)
        my.get('https://www.itdog.cn/ping')
        my.find_element('xpath', '//*[@id="ip"]').send_keys(url)
        my.find_element('xpath', '//*[@id="screenshots"]/div/div/div/div[3]/div/div/div/div[1]/button[1]').click()
        time.sleep(3)
        html = my.page_source
        xpath_html = etree.HTML(html)
        # 运营商
        merchants = xpath_html.xpath('//*[@id="simpletable"]/tbody/tr/td[1]//text()')
        merchant_list = []
        test_list = []
        i = 1
        for one_data in merchants:
            one_data = one_data.replace('\n', '')
            one_data = one_data.replace('\t', '')
            if one_data:
                if i % 2:
                    merchant_list.append(one_data)
                    i += 1
                else:
                    test_list.append(one_data)
                    i += 1

        # 检测点

        # 响应ip
        request = re.findall('<div id="(.*?)" style="display:inline-block;">(.*?)</div>', html)
        # ip地理位置
        IP = re.findall(
            '<td class="ip_address address-hidden" id="(.*?)" style="min-width:300px;" title="(.*?)">(.*?)</td>', html)

        for i in range(0, 100000):
            try:
                self.data_list.append('运营商:'+merchant_list[i]+'---检测点:'+test_list[i]+'---响应ip:'+ request[i][1]+'---ip地理位置:'+IP[i][2])
                height = self.zero_data.frameSize().height()
                self.zero_data.setText("<br>".join(self.data_list))
                self.zero_data.resize(1800, height + 20)
                self.zero_data.repaint()

            except:
                break
        self.data_list.append('检测结束')
        height = self.zero_data.frameSize().height()
        self.zero_data.setText("<br>".join(self.data_list))
        self.zero_data.resize(1800, height + 20)
        self.zero_data.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = my_window()
    window.show()

    app.exec()