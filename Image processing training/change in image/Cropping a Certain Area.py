import cv2
imag = cv2.imread("images.jpg")
cropped= imag[60:500,50:500]
cv2.imshow("orginal",imag)
cv2.imshow("cropped",cropped)
cv2.waitKey(0)
