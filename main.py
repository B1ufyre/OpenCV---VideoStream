import cv2
green = cv2.VideoCapture("video.mp4")
while 1 == 1:
    ret, img = green.read()
    cv2.imshow("green.mp4", img)
    k = cv2.waitKey(10)
    if k == 27:
        break