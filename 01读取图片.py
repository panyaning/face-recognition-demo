# 导入cv 模块
import cv2 as cv
# 读取图片
img = cv.imread('face1.jpg')  # cv读取到的图片是ndarray格式
# 显示图片
cv.imshow('read_img', img)
# 等待
cv.waitKey(0)   # 0为无限制等待
# 释放内存
cv.destroyAllWindows()