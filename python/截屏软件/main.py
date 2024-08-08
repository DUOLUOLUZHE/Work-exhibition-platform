from PIL import ImageGrab
import cv2
import matplotlib.pyplot as plt
import time
time_time = str(time.time())[0:10]
# one_time = ''
# for i in time_time:
#     if i == '.':
#         pass
#     else:
#         one_time = one_time + i
im = ImageGrab.grab()
im.save("截屏图库/"+str(time_time)+'.jpg')
cv2.namedWindow('截屏', cv2.WINDOW_NORMAL)
im = cv2.imread(str(time_time)+'.jpg')
im = cv2.resize(im, (3108, 2040))
cv2.imshow('截屏',im)
cv2.waitKey(0)


