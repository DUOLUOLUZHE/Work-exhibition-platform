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

def math(old_data,new_data,over_data):
    try:
        one_data = int(re.findall('发送的字节数=(.*), 接收的字节数',new_data)[0]) - int(re.findall('发送的字节数=(.*), 接收的字节数',old_data)[0])
    except:
        one_data = 0
    over_data = re.sub('<1>',str(one_data),over_data)
    try:
        two_data = int(re.findall('接收的字节数=(.*), 发送的包数据量', new_data)[0]) - int(re.findall('接收的字节数=(.*), 发送的包数据量', old_data)[0])
    except:
        two_data = 0
    over_data = re.sub('<2>', str(two_data), over_data)
    try:
        three_data = int(re.findall('发送的包数据量=(.*), 接收的包数据量', new_data)[0]) - int(re.findall('发送的包数据量=(.*), 接收的包数据量', old_data)[0])
    except:
        three_data = 0
    over_data = re.sub('<3>', str(three_data), over_data)
    try:
        four_data = int(re.findall('接收的包数据量=(.*), 接收出错次数', new_data)[0]) - int(re.findall('接收的包数据量=(.*), 接收出错次数', old_data)[0])
    except:
        four_data = 0
    over_data = re.sub('<4>', str(four_data), over_data)
    try:
        five_data = int(re.findall('接收出错次数=(.*), 发送出错次数', new_data)[0]) - int(re.findall('接收出错次数=(.*), 发送出错次数', old_data)[0])
    except:
        five_data = 0
    over_data = re.sub('<5>', str(five_data), over_data)
    try:
        six_data = int(re.findall('发送出错次数=(.*), 接收丢弃次数', new_data)[0]) - int(re.findall('发送出错次数=(.*), 接收丢弃次数', old_data)[0])
    except:
        six_data = 0
    over_data = re.sub('<6>', str(six_data), over_data)
    try:
        seven_data = int(re.findall('接收丢弃次数=(.*), 发送丢弃次数', new_data)[0]) - int(re.findall('接收丢弃次数=(.*), 发送丢弃次数', old_data)[0])
    except:
        seven_data = 0
    over_data = re.sub('<7>', str(seven_data), over_data)
    try:
        eight_data = int(re.findall('发送丢弃次数=(.*)', new_data)[0]) - int(re.findall('发送丢弃次数=(.*)', old_data)[0])
    except:
        eight_data = 0
    over_data = re.sub('<8>', str(eight_data), over_data)
    return over_data

def select1_1():
    while True:
        NUM = 0
        print('<'+str(NUM)+'>'+'所有网卡')
        for name in psutil.net_io_counters(True):
            NUM=NUM+1
            print('<'+str(NUM)+'>'+str(name))
        select = int(input('选择你想要监控的网卡序号：'))
        if select>=0 and select<=NUM:
            looking(select)
            break
        else:
            print('非法字符！！！')


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
        old_data = wish('总流量:'+str(psutil.net_io_counters()))
        time.sleep(0.5)
        new_data = wish('总流量:'+str(psutil.net_io_counters()))
        time.sleep(0.5)
        over_data = '总流量<秒级监控>:(发送的字节数=<1>, 接收的字节数=<2>, 发送的包数据量=<3>, 接收的包数据量=<4>, 接收出错次数=<5>, 发送出错次数=<6>, 接收丢弃次数=<7>, 发送丢弃次数=<8>)'
        over_data = math(old_data,new_data,over_data)
        os.system('cls')
        print(over_data)


def looking(select):
    if select == 0:
        while True:
            one_message_old_list = []
            one_message_new_list = []
            over_data_list = []
            for one_data in psutil.net_io_counters(True):
                over_data_list.append(str(one_data) + '<秒级监控>:(发送的字节数=<1>, 接收的字节数=<2>, 发送的包数据量=<3>, 接收的包数据量=<4>, 接收出错次数=<5>, 发送出错次数=<6>, 接收丢弃次数=<7>, 发送丢弃次数=<8>)')
                one_message_old_list.append(wish('<' + str(one_data) + '>:' + str(psutil.net_io_counters(True)[one_data])))
            time.sleep(0.5)
            for one_data in psutil.net_io_counters(True):
                one_message_new_list.append(wish('<' + str(one_data) + '>:' + str(psutil.net_io_counters(True)[one_data])))
            time.sleep(0.5)
            os.system('cls')
            for i in range(0,int(len(one_message_new_list))):
                over_data = math(one_message_old_list[i], one_message_new_list[i], over_data_list[i])
                print(over_data)
                time.sleep(0.1)

    else:
        sum = 0
        for i in psutil.net_io_counters(True):
            sum+=1
            if select==sum:
                one_data = i
        os.system('cls')
        while True:
            one_message_old = wish('<'+str(one_data)+'>:'+str(psutil.net_io_counters(True)[one_data]))
            time.sleep(0.5)
            one_message_new = wish('<' + str(one_data) + '>:' + str(psutil.net_io_counters(True)[one_data]))
            time.sleep(0.5)
            over_data = str(one_data) +'<秒级监控>:(发送的字节数=<1>, 接收的字节数=<2>, 发送的包数据量=<3>, 接收的包数据量=<4>, 接收出错次数=<5>, 发送出错次数=<6>, 接收丢弃次数=<7>, 发送丢弃次数=<8>)'
            over_data = math(one_message_old,one_message_new,over_data)
            os.system('cls')
            print(over_data)
            time.sleep(0.1)



if __name__ == '__main__':
    os.system('cls')
    select1()
    print('------------------------------------------关闭监控-------------------------------------------------')




