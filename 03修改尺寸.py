# 导入cv 模块
import cv2 as cv
# 读取图片
img = cv.imread('face1.jpg')
# 修改尺寸
resize_img = cv.resize(img, dsize=(200, 200))
# 显示原图
cv.imshow('img', img)
# 显示修改后的
cv.imshow('resize_img', resize_img)
# 打印出原图尺寸
print('未修改：', img.shape)
# 打印出修改后的尺寸
print('修改后：', resize_img.shape)
# 等待
while True:
    if ord('q') == cv.waitKey(0):  # ord函数是求字符的ASCII
        break
# 释放内存
cv.destroyAllWindows()
