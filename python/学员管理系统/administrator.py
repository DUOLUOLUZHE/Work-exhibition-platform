import PySimpleGUI as gui
import os
import management
import multiprocessing
def input():
    format = [
        [gui.Text('管理员登录', size=(90, 0), justification='center', font=(40), )],
        [gui.Text('账号', size=(5, 0)),gui.In('', size=(85, 0))],
        [gui.Text('密码', size=(5, 0)),gui.In('', size=(85, 0))],
        [gui.Button('确定', size=(45, 0)),gui.Button('退出', size=(45, 0))]
    ]
    window = gui.Window('学员管理系统', format)
    sum = 0
    while True:
        event, valuse = window.read()
        if event == None:
            window.close()
            break
        if event == '确定':
            with open('data/administrator.txt', 'r', encoding='utf-8')as fp:
                users = fp.readlines()
            for user in users:
                if user == valuse[0] +'!'+ valuse[1]:
                    gui.Popup('登录成功！')
                    window.close()
                    vlan1 = multiprocessing.Process(target=management.one)
                    vlan1.start()
                    sum = 1
            if sum == 1:
                break
            else:
                gui.Popup('账户密码错误！！！')
        if event == '退出':
            window.close()