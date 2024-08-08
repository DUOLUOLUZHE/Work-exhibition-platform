import os
import PySimpleGUI as gui
import shutil
import re
import multiprocessing

#变量建立
books_set = []
books = []
#调试字典
def read_clean_debug(place,text):
    format_debug_one = [
        [gui.Text('字典调试界面',size=(90,0),justification = 'center',font=(40)),],
        [gui.Text('显示指定书架字典'),gui.In(''),gui.Button('查看')],
        [gui.Text('向指定书架字典中添加关键字'),gui.In(''),gui.Button('确定')],
        [gui.Text('删除指定书架字典中指定关键字'),gui.In(''),gui.Button('指定')],
        [gui.Button('退出',size=(90,0))]
    ]

    window = gui.Window('字典调试界面',format_debug_one)
    while True:
        event,valuse = window.read()
        if event == None:
            window.close()
            break
        if event == '查看':
            vlan1 = multiprocessing.Process(target=see,args=(valuse[0],))
            vlan1.start()
        if event == '确定':
            vlan2 = multiprocessing.Process(target=add, args=(valuse[1],))
            vlan2.start()
        if event == '指定':
            vlan3 = multiprocessing.Process(target=delete, args=(valuse[2],))
            vlan3.start()
        if event == '退出':
            window.close()
            break

#查看模块
def see(valuse):
    with open('dictionary/'+str(valuse)+'.txt','r',encoding='utf-8')as fp:
        data = fp.readlines()#data是列表
    sum_lift = 0
    sum_right = 11
    while True:
        format_see = [
            [gui.Text(valuse + '书架字典', size=(90, 0), justification='center', font=(40))],
            [[gui.Text(i, size=(90, 0), justification='center', font=(40))]for i in data[sum_lift:sum_right]],
            [gui.Button('上一页',size=(30,0)), gui.Button('确定',size=(30,0)), gui.Button('下一页',size=(30,0))],
        ]
        window = gui.Window(valuse + '书架字典', format_see)
        event,valuses = window.read()
        if event == None:
            window.close()
            break
        if event == '确定':
            window.close()
            break
        if event == '上一页':
            if sum_lift==0:
                pass
            else:
                sum_lift=sum_lift-10
                sum_right=sum_right-10
            window.close()
        if event == '下一页':
            if sum_right>=len(data):
                pass
            else:
                sum_lift=sum_lift+10
                sum_right = sum_right+10
            window.close()




#添加模块
def add(valuse):
    format_add = [
        [gui.Text(valuse + '书架字典', size=(90, 0), justification='center', font=(40))],
        [gui.In('请输入想要添加的关键词',size=90)],
        [gui.Button('添加', size=(45, 0)), gui.Button('退出', size=(45, 0))],
    ]
    window = gui.Window('添加界面',format_add)
    while True:
        event,valuses = window.read()
        if event == None:
            window.close()
            break
        if event == '添加':
            try:
                with open('dictionary/' + valuse + '.txt', 'r', encoding='utf-8')as fp:
                    data = fp.readlines()
                    for it in data:
                        if it == str(valuses[0]) +'\n':
                            gui.Popup('关键词已经存在字典中')
                            break
            except:
                pass
            try:
                with open('dictionary/'+valuse+'.txt','a',encoding='utf-8')as fp:
                    fp.write(str(valuses[0])+'\n')

                gui.Popup('添加成功！')
            except:
                gui.Popup('您输入的书架名称有误！')
        if event == '退出':
            window.close()
            break

#删除模块
def delete(valuse):
    format_defete= [
        [gui.Text(valuse + '书架字典', size=(90, 0), justification='center', font=(40))],
        [gui.In('请输入想要删除的关键词', size=90)],
        [gui.Button('删除', size=(45, 0)), gui.Button('退出', size=(45, 0))],
    ]
    window = gui.Window('删除界面', format_defete)
    while True:
        event, valuses = window.read()
        if event == None:
            window.close()
        if event == '删除':
            try:
                with open('dictionary/' + valuse + '.txt', 'r', encoding='utf-8')as fp:
                    data = fp.readlines()
                    for it in data:
                        if it == str(valuses[0]) +'\n':
                            data.remove(it)
                            with open('dictionary/' + valuse + '.txt', 'w', encoding='utf-8')as time:
                                time.write('')
                            for irir in data:
                                with open('dictionary/' + valuse + '.txt', 'a', encoding='utf-8')as wr:
                                    wr.write(irir)

                            gui.Popup('删除成功！')
                            break

            except:
                gui.Popup('您输入的书架名称有误！')
        if event == '退出':
            window.close()
            break



