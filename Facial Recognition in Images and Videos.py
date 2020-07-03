# Detecting faces in images
import cv2
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('Image_Photo.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Facial Recognition',img)
f=face.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
for x,y,w,h in f:
    img=cv2.rectangle(img,(x,y),(x+h,y+w),(0,255,0),2)
    cv2.imshow('Face Recognized',img) 
cv2.waitKey(0)
cv2.destroyAllWindows()

# Comparing if two images are same or not
import cv2
import numpy as np

img=cv2.imread('Photo.jpg')
image=cv2.imread('Photo_changed.jpg')
difference=cv2.subtract(img,image)
result = not np.any(difference) 
if result is True:
    print('This is the same image')
else:
    print('This is not the same image')
cv2.waitKey(0)
cv2.destroyAllWindows()

# Detecting faces in Videos
import cv2
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

while True:
    _,img = cap.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    f = face.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 7)

    for x,y,w,h in f:
        img = cv2.rectangle(img,(x,y),(x+h,y+w),(0,255,0),-2)
    cv2.imshow('Face Recognized',img)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows() 
