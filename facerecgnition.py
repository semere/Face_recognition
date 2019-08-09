import cv2
img = cv2.imread("C:\\Users\semere\\PycharmProjects\\sem\\face.jpg", 1)
face_csc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_csc.detectMultiScale(gray, 1.3, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
cv2.imshow('img', img)
cv2.waitKey(0)