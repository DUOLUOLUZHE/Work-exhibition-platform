import os
import PySimpleGUI as gui
import shutil
import re
#变量建立
books_set = []
books = []
#查看当前所有书架名称
def read_book_set(place):
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
        [gui.Text('现有书架', size=(90, 0), justification='center', font=(40)), ],
        [[gui.Text(i,size=(90,0),justification='center')] for i in books_set],
        [gui.Button('确认',size=(90,0))]
    ]
    window2 = gui.Window('电子图书馆管理系统', format_2)
    while True:
        envent, value = window2.read()
        if envent == None:
            window2.close()
            break
        if envent == '退出':
            window2.close()
            break
        if envent == '确认':
            window2.close()
            break
    books.clear()
    books_set.clear()