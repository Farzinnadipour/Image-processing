import cv2 
img= cv2.imread("images.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("orginal",img)
cv2.imshow("wwd",hsv)
cv2.waitKey(0)