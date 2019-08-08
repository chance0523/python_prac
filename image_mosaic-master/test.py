import cv2
img = cv2.imread('01.jpg')
print(img)
cv2.imshow('image', img)
cv2.waitKey(0)
