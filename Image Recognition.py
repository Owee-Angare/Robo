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
