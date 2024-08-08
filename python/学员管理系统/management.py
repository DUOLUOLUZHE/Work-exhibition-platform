import PySimpleGUI as gui
import multiprocessing
import management_1
import management_2
import management_3
import management_4

import os

def one():
    format = [
        [gui.Text('管理后台', size=(90, 0), justification='center', font=(80), )],
        [gui.Text('', size=(22, 0)),gui.Button('查看所有学员账号', size=(45, 0),font=(40)),gui.Text('', size=(22, 0))],
        [gui.Text('', size=(22, 0)), gui.Button('查看所有管理员账号', size=(45, 0), font=(40)), gui.Text('', size=(22, 0))],
        [gui.Text('', size=(22, 0)),gui.Button('学员账号管理', size=(45, 0),font=(40)),gui.Text('', size=(22, 0))],
        # [gui.Text('', size=(22, 0)),gui.Button('添加学员账号', size=(45, 0),font=(40)),gui.Text('', size=(22, 0))],
        [gui.Text('', size=(22, 0)),gui.Button('管理员账号管理', size=(45, 0),font=(40)),gui.Text('', size=(22, 0))],
        [gui.Button('退出', size=(90, 0))]
    ]
    window = gui.Window('学员管理系统', format)
    while True:
        event, valuse = window.read()
        if event == None:
            window.close()
            break
        if event == '查看所有学员账号':
            vlan1 = multiprocessing.Process(target=management_1.vlan)
            vlan1.start()
        if event == '学员账号管理':
            vlan2 = multiprocessing.Process(target=management_2.vlan)
            vlan2.start()
        if event == '查看所有管理员账号':
            vlan3 = multiprocessing.Process(target=management_3.vlan)
            vlan3.start()
        if event == '管理员账号管理':
            vlan4 = multiprocessing.Process(target=management_4.vlan)
            vlan4.start()

        if event == '退出':
            window.close()