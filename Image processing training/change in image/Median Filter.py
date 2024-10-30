import cv2
img=cv2.imread("images.jpg")
#گرفتن نوییز در تصویر
median= cv2.medianBlur(img,3)
cv2.imshow("org",img)
cv2.imshow("Median Filter",median)
cv2.waitKey(0)