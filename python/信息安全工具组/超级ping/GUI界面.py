import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class my_window(QWidget):
    def __init__(self):
        super(my_window, self).__init__()

        # 设置窗口大小
        self.resize(600, 50)
        # 设置窗口标题
        self.setWindowTitle('超级ping')
        # 整体布局方式
        all_format = QVBoxLayout()

        # 第一组
        one_box = QGroupBox()
        # 建立水平容器
        one_one_box = QHBoxLayout()
        lift_format = QLabel('超级ping:')
        right_format = QLineEdit('请输入域名或ip')
        center_module = QPushButton('开始')
        # 将组件添加到水平容器中
        one_one_box.addWidget(lift_format)
        one_one_box.addWidget(right_format)
        one_one_box.addWidget(center_module)
        # 将容器插入第一组中
        one_box.setLayout(one_one_box)


        # 将组插入整体布局中
        all_format.addWidget(one_box)

        # 设置窗口显示容器
        self.setLayout(all_format)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = my_window()
    window.show()

    app.exec()