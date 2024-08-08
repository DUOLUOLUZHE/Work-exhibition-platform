import os
import PySimpleGUI as gui
import shutil
import re
#变量建立
books_set = []
books = []
#创建书架
def read_make(place):
    names_2 = os.listdir(place)
    book = 0
    book_set = 0
    off = 0
    for i in names_2:
        for it in i:
            if it == '.':
                book+=1
                off = 1
                break
        if off == 1:
            book_set+=1
            books.append(i)
            off=0
        else:
            books_set.append(i)
    format_2 = [
        [gui.Text('请输入创建书架名称'),gui.In('')],
        [gui.Button('确定')],
        [gui.Button('取消')],
    ]
    widow_make = gui.Window('电子图书馆管理系统',format_2)
    while True:
        envent,valuse = widow_make.read()
        if envent == None:
            break
        if envent == '确定':
            for i in books_set:
                if str(valuse) == i:
                    gui.Popup('书架已存在！！！')
                    break
            os.mkdir(str(place)+'/'+str(valuse[0]))
            with open('dictionary/'+str(valuse[0])+'.txt','w',encoding='utf-8')as fp:
                pass
            gui.Popup('书架创建成功！')

        if envent == '取消':
            break
    widow_make.close()