import cv2

def nothing(x):
    pass
cv2.namedWindow("webcam")
cv2.createTrackbar("L_TH","webcam",0,255,nothing)
cv2.createTrackbar("U_TH","webcam",0,255,nothing)
cv2.setTrackbarPos("U_TH","webcam",255)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if ret == 0:
        break
    frame = cv2.flip(frame, 1)
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.GaussianBlur(frame_gray,(5,5),0)
    uth = cv2.getTrackbarPos("U_TH","webcam")
    lth = cv2.getTrackbarPos("L_TH","webcam")
    canny = cv2.Canny(frame_gray,lth,uth)
    cv2.imshow("webcam", canny)
    if cv2.waitKey(36) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
