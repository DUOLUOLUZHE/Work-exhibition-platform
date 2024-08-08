import sys
import time
import os
from PyQt5.QtWidgets import *
import requests
from PyQt5 import uic
from PyQt5.QtWidgets import *
from selenium import webdriver
from lxml import etree


class my_window():
    def __init__(self):
        super(my_window, self).__init__()
        self.format()

    def format(self):
        self.ui = uic.loadUi('胡大师.ui')
        add_button = self.ui.pushButton
        del_button = self.ui.pushButton_2
        start_button = self.ui.pushButton_3
        init = self.ui.lineEdit
        self.small_window = self.ui.textBrowser
        self.small_window2 = self.ui.textBrowser_2
        self.small_window.setStyleSheet("background-color:black;color:white;")
        self.small_window2.setStyleSheet("background-color:black;color:white;")
        add_button.clicked.connect(lambda:self.add_start(init.text()))
        del_button.clicked.connect(lambda:self.delete(init.text()))
        start_button.clicked.connect(self.clean)
        self.show()

    def add_start(self,text):
        self.small_window2.clear()
        self.small_window2.append('开始添加。。。。。。')
        with open('监控列表.txt','a',encoding='utf-8')as fp:
            fp.write(text+'\n')
        self.small_window.clear()
        self.show()
        self.small_window2.append('添加成功！')

    def show(self):
        with open('监控列表.txt','r',encoding='utf-8')as fp:
            data_list = fp.readlines()
        for data in data_list:
            self.small_window.append(data[:-1])

    def delete(self,text):
        print(text)
        self.small_window2.clear()
        self.small_window2.append('开始删除。。。。。。')
        with open('监控列表.txt','r',encoding='utf-8')as fp:
            data_list = fp.readlines()
        try:
            print(data_list)
            data_list.remove(text+'\n')
            print(data_list)
            with open('监控列表.txt','w',encoding='utf-8')as f:
                f.write('')
            for data in data_list:
                if data != '\n':
                    with open('监控列表.txt','a',encoding='utf-8')as fps:
                        fps.write(data)
            self.small_window2.append('删除成功！')

        except:
            self.small_window2.append('监控列表中不存在'+text)

        self.small_window.clear()
        self.show()

    def clean(self):
        self.small_window2.clear()
        self.small_window2.append('电脑开始自动清理。。。。。。')
        with open('监控列表.txt','r',encoding='utf-8')as d:
            target_list = d.readlines()
        for target in target_list:
            #print(target[:-1])
            os.system('rmdir /s /q '+target[:-1])
            self.small_window2.append('正在清理'+target[:-1])

        self.small_window2.append('电脑清理结束！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = my_window()
    window.ui.show()

    app.exec()