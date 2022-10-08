import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("webcam")
cv2.createTrackbar("L_TH","webcam",0,255,nothing)
cv2.createTrackbar("U_TH","webcam",0,255,nothing)
cv2.setTrackbarPos("U_TH","webcam",255)

img = cv2.imread("img.png")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_gray = cv2.GaussianBlur(img_gray,(5,5),0)

while True:
    uth = cv2.getTrackbarPos("U_TH","webcam")
    lth = cv2.getTrackbarPos("L_TH","webcam")
    canny = cv2.Canny(img_gray,lth,uth)
    cv2.imshow("webcam", canny)
    h, w = canny.shape[:2]
    filled_from_bottom = np.zeros((h, w))
    for col in range(w):
        for row in reversed(range(h)):
            if canny[row][col] < 255:
                filled_from_bottom[row][col] = 255
            else:
                break
    cv2.imshow("fill",filled_from_bottom)
    if cv2.waitKey(36) & 0xFF == ord("q"):
        break



