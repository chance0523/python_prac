import cv2

img = cv2.imread("12.png", cv2.IMREAD_COLOR)
copy_img = img.copy()
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
