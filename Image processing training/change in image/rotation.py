import cv2 
img=cv2.imread("images.jpg")
width =200
hightn=200
cennter_point=(width/2,hightn/2)
rot=cv2.getRotationMatrix2D(cennter_point,-180,1.0)
rotated =cv2.warpAffine(img,rot,(width,hightn))
cv2.imshow("rotation",rotated)
cv2.waitKey(0)