from cv2 import cv2

face_cascade=cv2.CascadeClassifier(r"D:\SHRIMAD\PROJECTS\JARVIS\src\cascades\data\haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)
def video():

    while True:
        _, img= cap.read()
        #img=cv2.imread("C:\Jarvis\modules\img.jpg")
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces=face_cascade.detectMultiScale(gray,1.1,4)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow('img',img)
        k=cv2.waitKey(500)& 0xff
        if k==27:
            break
    cv2.destroyAllWindows()
    cap.release()
