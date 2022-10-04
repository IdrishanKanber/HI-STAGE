import cv2

img = cv2.imread("images/cyrus.jpeg")
face = cv2.CascadeClassifier("cascade/frontalface.xml")
smile = cv2.CascadeClassifier("cascade/haarcascade_smile.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face.detectMultiScale(gray,1.3,25)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)

wil_img = img[y:y+h,x:x+w]
wil_gray = gray[y:y+h,x:x+w]


smiles = smile.detectMultiScale(wil_gray,1.3,25)

for x2,y2,w2,h2 in smiles:
    cv2.rectangle(wil_img,(x2,y2),(x2+w2,y2+h2),(0,0,255),4)

cv2.imshow("smiles",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
