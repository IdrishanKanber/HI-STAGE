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
img_gray = cv2.GaussianBlur(img_gray,(19,19),-10)

while True:
    uth = cv2.getTrackbarPos("U_TH","webcam")
    lth = cv2.getTrackbarPos("L_TH","webcam")
    canny = cv2.Canny(img_gray,lth,uth)
    cv2.imshow("webcam", canny)
    h, w = img.shape[:2]
    max_row_inds = h - np.argmax(canny[::-1], axis=0)
    row_inds = np.indices((h, w))[0]
    inds_after_edges = row_inds >= max_row_inds
    filled_from_bottom = np.zeros((h, w))
    filled_from_bottom[inds_after_edges] = 255
    filled_from_bottom = cv2.erode()
    cv2.imshow("fill",filled_from_bottom)
    cv2.imshow("img",img)
    cv2.imshow("gray",img_gray)
    if cv2.waitKey(36) & 0xFF == ord("q"):
        break



