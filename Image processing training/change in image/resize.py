import cv2
imag =cv2.imread("images.jpg")
reszing = cv2.resize(imag,(350,350))
cv2.imshow("ordinal", imag)
cv2.imshow("reszing",reszing)
cv2.waitKey(0)