from http.client import IncompleteRead
import cv2
img = cv2.imread("download.jpg")
cv2.imshow("image",img)
cv2.waitKey(10000)
