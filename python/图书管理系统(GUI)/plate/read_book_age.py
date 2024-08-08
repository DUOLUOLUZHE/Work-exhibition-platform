import os
import PySimpleGUI as gui
import shutil
import re
#变量建立
books_set = []
books = []
#查看历史记录
def read_book_age(place,text):
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
    #这里books_set包含所有书架名
    #books包含所有数据名
    while True:
        with open('data/readingbook_age.txt','r',encoding='utf-8')as fp:
            books_set2 = fp.readlines()
        format_2 = [
            [gui.Text('阅读记录', size=(90, 0), justification='center', font=(40)), ],
            [[gui.Button(i[:-1],size=(90, 0))] for i in reversed(books_set2)],
            [gui.Button('确定', size=(90, 0))]
        ]
        window2 = gui.Window('电子图书馆管理系统', format_2)
        event,valuse = window2.read()
        if event == None:
            window2.close()
            break
        if event == '确定':
            window2.close()
            break
        for book_one in books_set2:
            book_one = book_one[:-1]
            if event == book_one:
                for book_set_one in books_set:
                    try:
                        with open(place+'/'+book_set_one+'/'+book_one,'r')as fp:#提前判断文件是否存在，防范命令行报可能
                            print(fp)
                        os.system('start '+place+'/'+book_set_one+'/'+book_one)
                    except:
                        pass
                window2.close()
                break