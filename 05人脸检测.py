# 导入cv 模块
import cv2 as cv


# 检测函数
def face_detect_demo():
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('F:\\software\\opencv\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt2.xml')  # 分类器是个类，face_detect是实例化的对象
    face = face_detect.detectMultiScale(gray)  # detectMultiScale函数可以检测出所有人脸，并将位置 宽 高 信息返回
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=2)
        # 参数表示依次为（图片，长方形框左上角坐标, 长方形框右下角坐标，字体颜色，字体粗细）
    cv.imshow('result', img)


# 读取图片
img = cv.imread('myface2.jpg')
img = cv.resize(img, dsize=(600,400))
# 检测函数
face_detect_demo()
# 等待
while True:
    if ord('q') == cv.waitKey(0):  # ord函数是求字符的ASCII
        break
# 释放内存
cv.destroyAllWindows()
