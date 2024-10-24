import cv2
imag = cv2.imread("images.jpg")
cv2.circle(imag,(150,150),42,(255,0,0),3)
cv2.imshow("circle",imag)
cv2.waitKey(0)
