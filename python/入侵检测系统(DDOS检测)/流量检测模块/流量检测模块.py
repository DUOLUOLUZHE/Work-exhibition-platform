import re
import sys
import os
import time
import PySimpleGUI
import cv2
import matplotlib.pyplot as plt

import psutil
# bytes_sent: 发送的字节数
# bytes_recv: 接收的字节数
# packets_sent: 发送的包数据量
# packets_recv: 接收的包数据量
# errin: 接收出错次数
# errout: 发送出错次数
# dropin: 接收丢弃次数
# dropout: 发送丢弃次数

def wish(one_message):
    data_wish = re.sub('bytes_sent','发送的字节数',one_message)
    data_wish = re.sub('bytes_recv', '接收的字节数', data_wish)
    data_wish = re.sub('packets_sent', '发送的包数据量', data_wish)
    data_wish = re.sub('packets_recv', '接收的包数据量', data_wish)
    data_wish = re.sub('errin', '接收出错次数', data_wish)
    data_wish = re.sub('errout', '发送出错次数', data_wish)
    data_wish = re.sub('dropin', '接收丢弃次数', data_wish)
    data_wish = re.sub('dropout', '发送丢弃次数', data_wish)
    data_wish = re.sub('snetio', '', data_wish)
    return data_wish

def select1_1():
    NUM = 0
    for name in psutil.net_io_counters(True):
        NUM=NUM+1
        print('<'+str(NUM)+'>'+str(name))
    select = int(input('选择你想要监控的网卡序号：'))
    looking(select)


def select1():
    #选择1
    while True:
        print('---------------------<监控总流量>-----------------------')
        print('--------------------<监控指定网卡>-----------------------')
        select = int(input('请选择(1/2)：'))
        if select==1:
            select1_2()
            break
        elif select==2:
            select1_1()
            break
        else:
            print('非法字符，请重新输入！')
            time.sleep(3)
            os.system('cls')


def select1_2():
    #监控总流量
    while True:
        print(wish('总流量:'+str(psutil.net_io_counters())))

def looking(select):
    sum = 0
    for i in psutil.net_io_counters(True):
        sum+=1
        if select==sum:
            one_data = i
    os.system('cls')
    while True:

        one_message = '<'+str(one_data)+'>:'+str(psutil.net_io_counters(True)[one_data])
        over_data = wish(one_message)
        print(over_data)
        time.sleep(0.1)



if __name__ == '__main__':
    os.system('cls')
    select1()




