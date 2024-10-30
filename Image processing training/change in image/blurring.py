import cv2
img=cv2.imread("images.jpg")
blur=cv2.GaussianBlur(img,(7,7),3)
cv2.imshow("org",img)
cv2.imshow("blur",blur)
cv2.waitKey(0)