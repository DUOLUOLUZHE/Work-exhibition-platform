import cv2
import matplotlib.pyplot as plt
import time
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
import multiprocessing

class my_window(QWidget):
    def __init__(self):
        super(my_window, self).__init__()
        self.place = ''
        self.init()

    def init(self):


        #t1 = multiprocessing.Process(target=self.now_TV())
        self.ui = uic.loadUi('智能人脸捕获系统.ui')
        self.big_window = self.ui.label_2
        self.big_window.setScaledContents(True)
        self.small_window = self.ui.label_5
        # self.small_window.setScaledContents(True)
        self.title = self.ui.label_4
        self.into = self.ui.lineEdit
        self.new = self.ui.pushButton
        self.start = self.ui.pushButton_2

        self.new.clicked.connect(self.new_ting)
        self.start.clicked.connect(self.start_TV)


        # 显示UI
        self.ui.show()

    def upload(self):
        # # 读取视屏
        self.TV = cv2.VideoCapture(self.place)
        # # 判断是否获取成功
        if not self.TV.isOpened():
            print('视频获取失败')
            sys.exit()

    def start_TV(self):
        #加载视屏
        self.upload()

        # 更新视频
        # 创建定时器，用于更新视频帧
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.now_TV)
        self.timer.start(1000 // int(self.TV.get(cv2.CAP_PROP_FPS)))  # 根据视频帧率设置定时器间隔

    def now_TV(self):

        ret,frame = self.TV.read()
        if ret:
            #帧处理
            self.face_get(frame)

            #将视屏转换为QPixmap格式，才能在标签中显示
            height, width, _ = frame.shape
            qimg = QImage(frame.data, width, height, QImage.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(qimg)

            # 在标签中显示视频帧
            self.big_window.setPixmap(pixmap)

    def new_ting(self):
        title_name = self.into.text()
        self.place = title_name
        title_data = ''
        for one in title_name:
            title_data = title_data + one
            if one == '\\':
                title_data = ''

        self.title.setText(title_data)

    def face_get(self,frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 实例化分类器
        # 人脸分类器
        self.face_cas = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.face_cas.load("haarcascade_frontalface_default.xml")
        # # 眼睛分类器
        # self.eyes_cas = cv2.CascadeClassifier("haarcascade_eye.xml")
        # self.eyes_cas.load("haarcascade_eye.xml")
        # 调用识别人脸
        faces = self.face_cas.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=7, minSize=(32, 32))
        for face in faces:
            x,y,w,h = face

            #框出人脸
            cv2.rectangle(frame,(x,y),(x+h,y+w),(0,255,0),3)

            #提取人脸
            one_face_img = frame[y:y+h,x:x+w]

            height, width, _ = one_face_img.shape
            qimg = QImage(one_face_img.data.tobytes(), one_face_img.shape[1], one_face_img.shape[0],one_face_img.shape[1] * 3, QImage.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(qimg)
            self.small_window.setPixmap(pixmap)

            pixmap.save('./人脸库/'+str(time.time())+'.jpg')




if __name__ == '__main__':
    #显示主界面
    app = QApplication(sys.argv)
    window = my_window()

    sys.exit(app.exec_())
