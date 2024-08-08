import os
import PySimpleGUI as gui
import shutil
import re
#变量建立
books_set = []
books = []
#查看指定书架中的所有书籍
def read_see(place,value):
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
    books_set2 = os.listdir(place+'/'+str(value[0]))
    pages = len(books_set2)
    pages_left = 0
    pages_right = 10
    while True:
        format_2 = [
            [gui.Text(str(value[0]) + '下的书籍', size=(90, 0), justification='center', font=(40)), ],
            [[gui.Button(i, size=(90, 0))] for i in books_set2[pages_left:pages_right]],
            [gui.Button('上一页', size=(30, 0)), gui.Button('确定', size=(30, 0)), gui.Button('下一页', size=(30, 0))]
        ]
        window2 = gui.Window('电子图书馆管理系统', format_2)
        event,valuse = window2.read()
        if event == None:
            window2.close()
            break
        if event == '确定':
            window2.close()
            break
        if event == '上一页':
            if pages_left!=0:
                pages_left = pages_left-10
                pages_right = pages_right -10
            window2.close()
        if event == '下一页':
            if pages_right <= pages:
                pages_left = pages_left+10
                pages_right = pages_right +10
            window2.close()
        for book_one in books_set2:
            if event == book_one:
                with open('data/readingbook_age.txt','r',encoding='utf-8')as fp:
                    data = fp.readlines()
                    if len(data) >=10:
                        for iv in range(0,9):
                            data[iv] = data[iv+1]
                        data[9] = book_one
                    else:
                        with open('data/readingbook_age.txt','a',encoding='utf-8')as fp:
                            fp.write(book_one+'\n')

                os.system('start '+place+'/'+str(value[0])+'/'+book_one)
                window2.close()
                break

    books.clear()
    books_set.clear()