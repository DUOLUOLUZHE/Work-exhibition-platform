import PySimpleGUI as gui
import os
def input():
    format = [
        [gui.Text('学员账号注册', size=(90, 0), justification='center', font=(40), )],
        [gui.Text('账号', size=(5, 0)),gui.In('', size=(85, 0))],
        [gui.Text('密码', size=(5, 0)),gui.In('', size=(85, 0))],
        [gui.Button('确定', size=(45, 0)),gui.Button('退出', size=(45, 0))]
    ]
    window = gui.Window('学员管理系统', format)
    while True:
        event,valuse = window.read()
        if event == None:
            window.close()
            break
        if event == '确定':
            user = valuse[0]
            password = valuse[1]
            with open('data/user.txt','a',encoding='utf-8')as fp:
                fp.write(user+'!'+password+'\n')
            gui.Popup('注册成功！')
        if event == '退出':
            window.close()