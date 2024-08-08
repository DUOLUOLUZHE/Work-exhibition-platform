import psutil
import socket
import re
import requests
import os
from . import format


def ip_show(ifname):
    addrs = psutil.net_if_addrs()
    if ifname in addrs:
        for addr in addrs[ifname]:
            if addr.family == socket.AF_INET:
                return addr.address
    return None

def port(ai):

    def get_service_name(port, proto):
        try:
            return socket.getservbyport(port, proto)
        except OSError:
            return "Unknown"

    def get_open_ports_and_services():
        connections = psutil.net_connections(kind='inet')
        open_ports = set()
        port_service_info = []

        for conn in connections:
            if conn.status == psutil.CONN_LISTEN:
                port = conn.laddr.port
                protocol = 'tcp' if conn.type == socket.SOCK_STREAM else 'udp'
                service = get_service_name(port, protocol)
                port_service_info.append((port, protocol, service))

        return port_service_info

    open_ports_and_services = get_open_ports_and_services()

    for port, protocol, service in open_ports_and_services:
        ai.say(f"已开启端口: {port}, 传输协议: {protocol}, 服务类型: {service}")


def harker(ai_):
    #实例化抽象类
    ai = format.format('黑客',ai_)
    #系统启动语音
    ai.start()

    while 1:
        # 语言识别
        data = ai.data_()

        # 位置判断
        ai.now_place()

        #组件汇总
        if('系统' in data):
            if('组件' in data):
                ai_.say('黑客系统现有的组件有:')
                ai_.say('IP查询系统')
                ai_.say('端口查询系统')
                ai_.say('物理地址检测系统')
                ai_.say('御剑后台目录扫描工具')
                ai_.say('御剑端口目录扫描工具')
                ai_.say('Layer子域名挖掘机')
                ai_.say('灯塔系统')
                ai_.say('VPN')
                ai_.say('Wireshark')
                ai_.say('雷电模拟器')
                ai_.say('科来网络分析器')
                continue


        if (('IP' in data) or ('ip' in data)):
            ai_.say('正在获取当前机器网卡信息')
            while(1):
                #指定获取网卡
                ai_.say('请指定网卡')
                ai_.input_audio()
                select = ai_.start()
                if ('无线网' in select):
                    ai_.say('正在获取当前机器无线网信息')
                    interface_name = "WLAN"
                    ip_address = ip_show(interface_name)
                    ai_.say('当前无线网ip为' + str(ip_address))
                    break
                if ('圣所' in select):
                    ai_.say('正在获取当前机器圣所网卡信息')
                    interface_name = "ZeroTier One"
                    ip_address = ip_show(interface_name)
                    ai_.say('当前圣所网卡ip为' + str(ip_address))
                    break

                if('关闭' in select):
                    break

            continue
        if ('本地' in data):
            if('端口' in data):
                ai_.say('正在获取当前机器端口信息')
                port(ai_)
                continue

        if('物理' in data):
            if('地址' in data):
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
                }
                res = requests.get('https://myip.ipip.net', timeout=5,headers=headers).text
                ip = str(re.findall('当前 IP：(.*?)  ', res)[0])
                place = str(re.findall('来自于：(.*)  ', res)[0])
                ai_.say('外网ip为:' + ip)
                ai_.say('当前现实地址为' + place)
                continue

        # 御剑后台扫描工具操控
        ai.app_open_off('后台', r'D:\A_HAT\Weapon_database\1.信息搜集\7.敏感目录文件搜索\御剑后台扫描珍藏版\御剑后台扫描工具.exe', '御剑后台扫描工具.exe', '御剑后台扫描工具')

        # 御剑端口扫描工具操控
        ai.app_open_off('端口', r'D:\A_HAT\Weapon_database\1.信息搜集\5.端口扫描\御剑无字典扫描工具\御剑无字典大小限制1937版\御剑无字典大小限制版.exe','御剑无字典大小限制版.exe','御剑端口扫描工具')

        # Layer子域名挖掘机操控
        ai.app_open_off('子域名', r'D:\A_HAT\Weapon_database\1.信息搜集\3.子域名挖掘\Layer子域名挖掘机4_1重构版\Layer子域名挖掘机4_1.exe','Layer子域名挖掘机4_1.exe','Layer子域名挖掘机')

        # 灯塔操控
        ai.app_open_off('灯塔', r'D:\A_HAT\Weapon_database\1.信息搜集\13.资产搜集\goby-win-x64-2.7.9\Goby.exe','Goby.exe','灯塔系统')

        # VPN
        ai.app_open_off('VPN', r'D:\Ruan_Jian\VPN\Clash for Windows\Clash for Windows.exe', 'Clash for Windows.exe','兔兔VPN')

        # Wireshark
        ai.app_open_off('鲨鱼', r'D:\Network_Security\Weapon\wireshark\Wireshark.exe', 'Wireshark.exe','Wireshark')

        # 雷电模拟器
        ai.app_open_off('模拟器', r"D:\A_HAT\Weapon_database_smalldi\1.基础入门\2.模拟器\雷电模拟器\leidian\LDPlayer9\dnplayer.exe", 'dnplayer.exe', '雷电模拟器')

        # 科来网络分析器
        ai.app_open_off('网络分析器', r"D:\A_HAT\Weapon_database_smalldi\1.基础入门\1.抓包工具\科来网络分析器\Csnas.exe.lnk",
                        'Csnas.exe.lnk', '雷电模拟器')







        # 关闭系统判断
        if ai.off():
            break
