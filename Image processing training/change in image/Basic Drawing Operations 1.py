import cv2
imag =cv2.imread("images.jpg")
cv2.line(imag,(120,50),(250,70),(255,0,0),2)
cv2.imshow("lines",imag)
cv2.waitKey(0)