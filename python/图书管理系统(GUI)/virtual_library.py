'''
注意事项
1.本软件对安装的位置并未要求，只是本软件会先行绑定电子图书馆位置，如若第一次使用或移动电子图书馆导致本软件失效，请将第6行代码中的place改为电子图书馆主文件夹所在的绝对路径位置
2.此软件创作者为胡冬阳先生，一切拿此软件非经允许用作商用的人士，我们一定会追究到底
'''
place = "E:\电子书库\程序员电子书"

#使用到的Python库
import os
import PySimpleGUI as gui
import shutil
import time
import re
import threading
import multiprocessing
import img
from plate import welcome
from plate import read_strat
from plate import read_clean_two as read_clean
from plate import read_make
from plate import read_book_set
from plate import read_see
from plate import read_clean_debug
from plate import read_book_age


#窗口格式
format_1 = [
    [gui.Text('欢迎来到胡冬阳的电子图书馆管理系统',size=(90,0),justification = 'center',font=(40)),],
    [gui.Text('现已经拥有的书架'),gui.Button('查看')],
    [gui.Text('创建书架'),gui.Button('创建')],
    [gui.Text('您是否要调试您书架对应的字典'),gui.Button('调试')],
    [gui.Text('您是否要整理所有电子书籍'),gui.Button('整理')],
    [gui.Text('打开指定书架查看所有书籍'),gui.In('书架名称'),gui.Button('查询'),gui.Button('历史记录')],
    [gui.Text('从资源管理器打开图书馆'),gui.Button('打开')],
    [gui.Button('退出',size=(90,0))]
]


#变量建立
books_set = []
books = []

def welcome():
    window = gui.Window('电子图书馆管理系统', format_1)
    while True:
        encom, text = window.read()
        if encom == None:
            window.close()
            break
        if encom == '退出':
            window.close()
            break
        if encom == '查看':
            vlan1 = multiprocessing.Process(target=read_book_set.read_book_set,args=(place,))
            vlan1.start()
        if encom == '创建':
            vlan2 = multiprocessing.Process(target=read_make.read_make,args=(place,))
            vlan2.start()
        if encom == '整理':
            read_clean.read_clean(place)
        if encom == '查询':
            vlan3 = multiprocessing.Process(target=read_see.read_see,args=(place,text,))
            vlan3.start()
        if encom == '打开':
            vlan4 = multiprocessing.Process(target=read_strat.read_strat,args=(place,text,))
            vlan4.start()
        if encom == '调试':
            vlan5 = multiprocessing.Process(target=read_clean_debug.read_clean_debug,args=(place,text,))
            vlan5.start()
        if encom == '历史记录':
            vlan6 = multiprocessing.Process(target=read_book_age.read_book_age,args=(place,text,))
            vlan6.start()
    gui.Popup('程序结束！')

# def hellow():
#     format = [
#         [gui.Image('img/1.PNG',size = (50, 50), key = "-WEATHER-IMG-")],
#     ]
#     window = gui.Window('欢迎使用',format)
#     time.sleep(3)
#     window.close()


#主程序
if __name__ == '__main__':
    # hellow()
    welcome()