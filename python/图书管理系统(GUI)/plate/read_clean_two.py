import os
import PySimpleGUI as gui
import shutil
import re

#变量建立
books_set = []
books = []
#整理非书架上的书，将之放入对应书架中
#思路：创建文件夹dictionary,将dictionary导入本模块,每创建一个书架都生成一个txt文件,文件以每行一个词的方式追加关键词,调用关键词对书籍进行挑选整理
#增加调试模块
def read_clean(place):
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
    #这里book_set包含所有书架名
    #books包含所有数据名

    for one_bookset in books_set:  # 取出一个书架名
        with open('dictionary/'+one_bookset+'.txt','r',encoding='utf-8')as fp:#取出书架对应的字典
            dictionary_data = fp.readlines()#取出字典内所有关键词
        for data in dictionary_data:#从所有关键词中逐个提取
            data = data[:-1]#去除换行符
            long = len(data)#关键词长度
            for one_book in books:  # 取出一个书本名
                sum = 0
                for write_data in data:  # 取出这个关键词的每一个字
                    for write_book in one_book:  # 取出这个书本名的每一个字
                        if write_data == write_book:  # 比较，如果相同，sum加一，当sum==long时代表此书应该放入书架
                            sum += 1
                            break
                    if sum == long:  # 此处判断sum长度等于long，将书放入书架，取出下一个书进行比较
                        # 放入前路径
                        place_old = place + '\\' + one_book
                        # 放入后路径
                        place_new = place + '\\' + one_bookset + '\\' + one_book
                        # 书本转移
                        os.system('move "' + place_old + '" ' + '"' + place_new + '"')
                        break
    gui.Popup('整理成功')
    books.clear()
    books_set.clear()
