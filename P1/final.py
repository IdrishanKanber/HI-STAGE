import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("webcam")
cv2.createTrackbar("L_TH","webcam",0,255,nothing)
cv2.createTrackbar("U_TH","webcam",0,255,nothing)
cv2.setTrackbarPos("U_TH","webcam",255)

img = cv2.imread("masa.jpeg")
img = cv2.resize(img,(640,480))

while True:
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.GaussianBlur(img_gray, (51, 51), -10)
    uth = cv2.getTrackbarPos("U_TH","webcam")
    lth = cv2.getTrackbarPos("L_TH","webcam")
    canny = cv2.Canny(img_gray,lth,uth)
    cv2.imshow("webcam", canny)
    h, w = img.shape[:2]
    row_inds = np.indices((h, w))[0]  # gives row indices in shape of img
    row_inds_at_edges = row_inds.copy()
    row_inds_at_edges[canny == 0] = 0  # only get indices at edges, 0 elsewhere
    max_row_inds = np.amax(row_inds_at_edges, axis=0)  # find the max row ind over each col
    inds_after_edges = row_inds >= max_row_inds
    filled_from_bottom = np.zeros((h, w))
    filled_from_bottom[inds_after_edges] = 255
    kernel = np.ones((5,5),np.uint8)
    filled_from_bottom = cv2.morphologyEx(filled_from_bottom,cv2.MORPH_OPEN,kernel)

    cv2.imshow("fill",filled_from_bottom)
    cv2.imshow("img",img)
    cv2.imshow("gray",img_gray)
    if cv2.waitKey(36) & 0xFF == ord("q"):
        break



