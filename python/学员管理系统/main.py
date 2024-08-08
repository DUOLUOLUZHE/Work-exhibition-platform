import PySimpleGUI as gui
import multiprocessing
import student
import administrator
import register
import PySimpleGUI


format = [
    [gui.Text('欢迎登录学员管理系统',size=(90,0),justification='center',font=(40),)],
    [gui.Text('请选择登录方式',size=(90,0),justification='center',font=(20))],
    [gui.Button('学员登录',size=(90,0))],
    [gui.Button('管理员登录',size=(90,0))],
    [gui.Button('学员注册',size=(90,0))]
]

if __name__ == "__main__":
    window = gui.Window('学员管理系统', format)
    while True:
        event,valuse = window.read()
        if event == None:
            window.close()
            break
        if event == '学员登录':
            vlan1 = multiprocessing.Process(target=student.input)
            vlan1.start()
        if event == '管理员登录':
            vlan2 = multiprocessing.Process(target=administrator.input)
            vlan2.start()
        if event == '学员注册':
            vlan3 = multiprocessing.Process(target=register.input)
            vlan3.start()


