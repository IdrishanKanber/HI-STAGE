import cv2
import numpy as np
"""
img = cv2.imread("klon.jpg")
dimension = img.shape
color = img[150,200]
print(dimension)
#cv2.imshow("klon",img)
#cv2.waitKey(0)
blue = img[420,500,0]
print(blue)

n_blue1 = img.item(150,200,0)
img.itemset((150,200,0),172)
"""
img = cv2.imread("klon.jpg")
roi = img[25:200,200:360]
cv2.imshow("klon",img)
cv2.imshow("roi",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
