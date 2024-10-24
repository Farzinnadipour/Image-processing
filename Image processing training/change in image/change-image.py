import cv2
imag =cv2.imread("images.jpg")
resizing =cv2.resize(imag,(350,350))
cv2.imshow("orginal",imag)
cv2.imshow("reszing",resizing)
cv2.waitKey(0)