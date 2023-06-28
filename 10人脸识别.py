import cv2 as cv
import os

# 创建识别器
recognizer = cv.face.LBPHFaceRecognizer_create()
# 加载训练好的数据文件
recognizer.read('./trainer/trainer1.yml')
# 名称
names = []

# 准别识别的图片
def face_detect_demo(img):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier('F:\\software\\opencv\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt2.xml')
    face = face_detector.detectMultiScale(gray_img)
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=2)
        # 人脸识别
        ids, confidence = recognizer.predict(gray_img[y:y+h, x:x+w])
        if confidence > 80:
            cv.putText(img, 'unknow', (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 1)
        else:
            cv.putText(img, str(names[ids-1]), (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 1)
    cv.imshow('result',img)
    cv.waitKey(0)


def loadname():
    path = './data/'
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    for imagePath in imagePaths:
        name = str(os.path.split(imagePath)[1].split('.')[1])
        names.append(name)


# 加载图片
img = cv.imread('./myface2.jpg')
img = cv.resize(img, dsize=(600,400))
loadname()
face_detect_demo(img)