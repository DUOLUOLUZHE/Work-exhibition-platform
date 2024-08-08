import PySimpleGUI as gui
def vlan():
    with open('data/administrator.txt','r',encoding='utf-8')as fp:
        data = fp.readlines()
    users = []
    passwords = []
    one = ''
    for user_passworld in data:
        sum = 0
        for zimu in user_passworld:
            if zimu == '!':
                sum = sum + 1
            else:
                one = one + zimu
            if sum == 1:
                users.append(one)
                one = ''
                sum = sum +1
        passwords.append(one[:-1])
        one = ''
    data_over = []
    for it in range(0,len(users)):
        data_over.append('账号:'+users[it]+'   密码:'+passwords[it])

    left = 0
    right = 9
    format = [
        [gui.Text('管理员账号', size=(90, 0), justification='center', font=(40), )],
        [[gui.Text(i, size=(90, 0), justification='center', font=(20), )] for i in data_over[left:right]],
        [gui.Button('上一页', size=(30, 0)), gui.Button('确定', size=(30, 0)), gui.Button('下一页', size=(30, 0))]
    ]
    while True:
        window = gui.Window('学员管理系统', format)
        event,valuse = window.read()
        if event == None:
            window.close()
            break
        if event == '确定':
            window.close()
            break
        if event == '上一页':
            if left != 0:
                left = left - 10
                right = right - 10
            window.close()
        if event == '下一页':
            if right <= len(data_over):
                left = left + 10
                right = right + 10
            window.close()