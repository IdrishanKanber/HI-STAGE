import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/cyrus.jpeg")
eye_cascade = cv2.CascadeClassifier("cascade/haarcascade_eye.xml")
face_cascade = cv2.CascadeClassifier("cascade/frontalface.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("image", gray)
#cv2.waitKey(0)


faces = face_cascade.detectMultiScale(gray, 1.3, 25)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 4)
    roi = img[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(roi, 1.3, 25)
    for x1,y1,w1,h1 in eyes:
        print(x1,y1,w1,h1)
        cv2.rectangle(img, (x1,y1), (x1+w1,y1+h1), (255,0,0), 4)
cv2.imshow("detected faces", img)
cv2.waitKey(0)