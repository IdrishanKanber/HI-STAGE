import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX   # resmin üzerine yazı yazacağımız fontlar
font1 = cv2.FONT_HERSHEY_COMPLEX  # opencv fonts

img = cv2.imread("images\polygons.png") #çokgenler olan resimi bir değişkene atadık

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #resimi tek kanallı hale getirdik
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)     #resmi siyah ve beyazlardan oluşacak hale <binary> getirdik

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   #kontür bulmak için kullanacağımız fonksiyon

for cnt in contours:

    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)   #kontür tahmini yaklaşımı

    cv2.drawContours(img, [approx], 0, (0), 5)      #köntürleri çizdiren fonksiyon

    x = approx.ravel()[0]   #approxravel fonksiyonu resimdeki sütunları satıra döker
    y = approx.ravel()[1]   #bulduğumuz köşe kordinatlarını x,y olarak ayırdık

    if len(approx) == 3:    #eğer ravel ile 3 satır bulursa bulunan kordinata üçgen yazdır
        cv2.putText(img, "Triangle", (x, y), font, 1, (0))

    elif len(approx) == 4:  #eğer ravel ile 4 satır bulursa bulunan kordinata dörtgen yazdır
        cv2.putText(img, "Rectangle", (x, y), font, 1, (0))

    elif len(approx) == 5:  #eğer ravel ile 5 satır bulursa bulunan kordinata beşgen yazdır
        cv2.putText(img, "Pentagon", (x, y), font, 1, (0))

    elif len(approx) == 6:  #eğer ravel ile 6 satır bulursa bulunan kordinata altıgen yazdır
        cv2.putText(img, "Hexagon", (x, y), font, 1, (0))

    else:
        cv2.putText(img, "Ellipse", (x, y), font, 1, (0))


cv2.imshow("IMG", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

