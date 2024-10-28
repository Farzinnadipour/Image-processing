import cv2
img=cv2.imread("images.jpg",0)
# تشخیص لبه
canny=cv2.Canny(img,10,200)
cv2.imshow("orginal",img)
cv2.imshow("canny",canny)
cv2.waitKey(0)