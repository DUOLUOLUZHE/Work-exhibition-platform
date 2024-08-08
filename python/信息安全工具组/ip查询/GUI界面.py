import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class my_window(QWidget):
    def __init__(self):
        super().__init__()

        #设置窗口大小
        self.resize(300,300)
        #设置窗口标题
        self.setWindowTitle("ip查询")
        #整体布局方式
        all_format = QVBoxLayout()

        #第一组
        top_box = QGroupBox()
        #建立水平容器
        one_box = QHBoxLayout()
        lift_module = QLabel('ip地址:')
        center_module = QLineEdit('请输入查询ip')
        right_module = QPushButton('查询')
        #将组件添加到水平容器中
        one_box.addWidget(lift_module)
        one_box.addWidget(center_module)
        one_box.addWidget(right_module)
        #将第一组添加入窗口
        top_box.setLayout(one_box)

        # 第二组
        top_two_box = QGroupBox()
        # 建立水平容器
        one2_box = QHBoxLayout()
        lift_module = QLabel('现实地址:')
        right_module = QLabel('中国河北保定博野')
        # 将组件添加到水平容器中
        one2_box.addWidget(lift_module)
        one2_box.addWidget(right_module)
        # 将第一组添加入窗口
        top_two_box.setLayout(one2_box)
        # 第三组
        top_three_box = QGroupBox()
        # 建立水平容器
        one3_box = QHBoxLayout()
        lift_module = QLabel('数字地址:')
        right_module = QLabel('2013397511')
        # 将组件添加到水平容器中
        one3_box.addWidget(lift_module)
        one3_box.addWidget(right_module)
        # 将第一组添加入窗口
        top_three_box.setLayout(one3_box)
        # 第四组
        top_four_box = QGroupBox()
        # 建立水平容器
        one4_box = QHBoxLayout()
        lift_module = QLabel('运营商:')
        right_module = QLabel('联通')
        # 将组件添加到水平容器中
        one4_box.addWidget(lift_module)
        one4_box.addWidget(right_module)
        # 将第一组添加入窗口
        top_four_box.setLayout(one4_box)
        #将组添加到整体容器中
        all_format.addWidget(top_box)
        all_format.addWidget(top_two_box)
        all_format.addWidget(top_three_box)
        all_format.addWidget(top_four_box)

        #设置窗口显示的容器
        self.setLayout(all_format)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = my_window()
    window.show()

    app.exec()
