import tkinter
import cv2, PySimpleGUI as sg
USE_CAMERA = 0
format = [
    [sg.Image(filename='', key='image')],
]

format_two = [
    [sg.Button('暂停',size=(80,1))],
    [sg.Button('开始',size=(80,1))]
]


window, cap = sg.Window('简易的计算机视觉系统',format, location=(0, 0), grab_anywhere=True), cv2.VideoCapture(USE_CAMERA)
while window(timeout=20)[0] != sg.WIN_CLOSED:
    window['image'](data=cv2.imencode('.png', cap.read()[1])[1].tobytes())


