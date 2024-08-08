import os
import PySimpleGUI as gui
import shutil
import re
#变量建立
books_set = []
books = []
#用资源管理器打开图书馆
def read_strat(place,value):
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
    os.system('start '+str(place))