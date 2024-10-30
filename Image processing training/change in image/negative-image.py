import cv2
img= cv2.imread("images.jpg")
negative = cv2.bitwise_not(img)
cv2.imshow("org",img)
cv2.imshow("negative",negative)
cv2.waitKey(0)