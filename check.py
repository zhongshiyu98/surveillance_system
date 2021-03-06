import cv2

def check1():

    cap = cv2.VideoCapture(0) # 使用第5个摄像头（我的电脑插了5个摄像头）
    face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml') # 加载人脸特征库

    while(True):

        # 读取一帧的图像
        ret, frame = cap.read()
        # 灰度处理
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 检测人脸
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.15, minNeighbors = 5, minSize = (5, 5))
        # 画出人脸
        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 用矩形圈出人脸

        cv2.imshow('Face Recognition', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release() # 释放摄像头
    cv2.destroyAllWindows()

def check2():
    cap = cv2.VideoCapture(0)  # 使用第5个摄像头（我的电脑插了5个摄像头）
    face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')  # 加载人脸特征库

    while (True):

        # 读取一帧的图像
        ret, frame = cap.read()
        # 灰度处理
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 检测人脸
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5))
        # 画出人脸
        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 用矩形圈出人脸

        cv2.imshow('Face Recognition', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # 释放摄像头
    cv2.destroyAllWindows()