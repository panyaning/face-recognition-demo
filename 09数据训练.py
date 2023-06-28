import os
import cv2 as cv
import numpy as np


def getImageAndLabels(path):
    # 储存人脸数据
    faces_train = []
    # 储存姓名数据
    ids = []
    # 储存所有图片的路径信息
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # 加载分类器
    face_detector = cv.CascadeClassifier('F:\\software\\opencv\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt2.xml')
    # 遍历列表3中的图片，提取出列表1和2所需的信息
    for imagePath in imagePaths:
        img = cv.imread(imagePath)
        img = cv.resize(img, dsize=(600, 400))
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(img)
        id = int(os.path.split(imagePath)[1].split('.')[0])
        for x, y, w, h in faces:
            ids.append(id)
            face = img[y:y+h, x:x+w]
            faces_train.append(face)
            print('id:', id)
            print('fs:',face)
    return faces_train, ids


if __name__ == '__main__':
    # 图片路径
    path = './data/'
    # 获取图像数组和id标签数组
    faces, ids = getImageAndLabels(path)
    # 加载识别器
    recognizer = cv.face.LBPHFaceRecognizer_create()
    # 训练
    recognizer.train(faces, np.array(ids))
    # 保存文件
    recognizer.write('trainer/trainer1.yml')