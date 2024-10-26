import cv2
lane = cv2.imread("images.jpg")
thresh , binary =cv2.threshold(lane,100,255,cv2.THRESH_BINARY)
cv2.imshow("orginl",lane)
cv2.imshow("thresh",binary)
cv2.waitKey(0)