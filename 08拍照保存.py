# 导入模块
import cv2 as cv
# 摄像头
cap = cv.VideoCapture(0)

num = 1

while(cap.isOpened()):
    flag, frame = cap.read()
    cv.imshow("Capture_Test", frame)
    k = cv.waitKey(1) & 0xFF
    if k == ord('s'):
        cv.imwrite("C:/Users/zhemzhu/Desktop/face_detect/data/"+str(num)+".pyn"+".jpg", frame)
        print("save successfully:"+str(num)+".jpg")
        print("----------------------")
        num += 1
    elif k == ord('q'):
        break

# 释放摄像头
cap.release()
# 释放内存
cv.destroyAllWindows()