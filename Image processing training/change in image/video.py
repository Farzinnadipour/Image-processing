import cv2 
video = cv2.VideoCapture("vdd.mp4")
while True :
    control , frame =video.read()
    if not control :
        break
    cv2.imshow("Yilmas",frame)
    if cv2.waitKey(110)==27:
        break