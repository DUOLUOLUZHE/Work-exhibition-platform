import PySimpleGUI as gui
import multiprocessing
import register

def vlan():
    with open('data/administrator.txt','r',encoding='utf-8')as fp:
        users_passwords = fp.readlines()
    format = [
        [gui.Text('管理员账号管理', size=(90, 0), justification='center', font=(80), )],
        [gui.Text('', size=(22, 0)), gui.Button('删除指定账号', size=(45, 0), font=(40)), gui.Text('', size=(22, 0))],
        [gui.Text('', size=(22, 0)), gui.Button('添加指定账号', size=(45, 0), font=(40)), gui.Text('', size=(22, 0))],
    ]
    window = gui.Window('学员管理系统', format)
    while True:
        event, valuse = window.read()
        if event == None:
            window.close()
            break
        if event == '删除指定账号':
            vlan1 = multiprocessing.Process(target=delete)
            vlan1.start()
        if event == '添加指定账号':
            vlan2 = multiprocessing.Process(target=input)
            vlan2.start()

def delete():
    with open('data/administrator.txt','r',encoding='utf-8')as fp:
        users_passwords = fp.readlines()
        print(users_passwords)
    format_delete = [
        [gui.Text('账号指定', size=(90, 0), justification='center', font=(80), )],
        [gui.Text('账号', size=(5, 0),),gui.In('',size=(85,0))],
        [gui.Text('密码', size=(5, 0),),gui.In('',size=(85,0))],
        [gui.Button('确定', size=(45, 0)), gui.Button('退出', size=(45, 0))]
    ]
    window_delete = gui.Window('学员管理系统', format_delete)
    while True:
        event_delete, valuse_delete = window_delete.read()
        if event_delete == None:
            window_delete.close()
            break
        if event_delete == '确定':
            user_passworld = str(valuse_delete[0])+'!'+str(valuse_delete[1])+'\n'

            try:
                users_passwords.remove(user_passworld)
                with open('data/administrator.txt', 'w', encoding='utf-8')as fpr:
                    fpr.write('')
                for it in users_passwords:
                    if it == '\n':
                        pass
                    else:
                        with open('data/administrator.txt','a',encoding='utf-8')as fprt:
                            fprt.write(it)

                gui.Popup('删除成功！')
            except:
                gui.Popup('账号不存在！')

        if event_delete == '退出':
            window_delete.close()

def input():
    format1 = [
        [gui.Text('管理员账号注册', size=(90, 0), justification='center', font=(40), )],
        [gui.Text('账号', size=(5, 0)),gui.In('', size=(85, 0))],
        [gui.Text('密码', size=(5, 0)),gui.In('', size=(85, 0))],
        [gui.Button('确定', size=(45, 0)),gui.Button('退出', size=(45, 0))]
    ]
    window = gui.Window('学员管理系统', format1)
    while True:
        event,valuse = window.read()
        if event == None:
            window.close()
            break
        if event == '确定':
            user = valuse[0]
            password = valuse[1]
            with open('data/administrator.txt','a',encoding='utf-8')as fp:
                fp.write(user+'!'+password+'\n')
            gui.Popup('注册成功！')
        if event == '退出':
            window.close()
