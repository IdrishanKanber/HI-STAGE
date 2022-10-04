import cv2
import numpy as np

cap = cv2.VideoCapture("images/car.mp4")    #videoyu cap değişkenine aldık
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=120, detectShadows=False)  #arkaplan çıkaran fonksiyon

while 1:
    _, frame = cap.read()   #frame değişkenine video karemizi alıyoruz
    frame = cv2.resize(frame, (640, 480))   #videonun çözünürlüğünü değiştiriyoruz
    mask = subtractor.apply(frame)      #videonun backgroundunu çıkartıyoruz

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





