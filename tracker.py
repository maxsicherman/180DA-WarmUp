import cv2 as cv
import numpy as np
def foo():
    return
cap = cv.VideoCapture(0);


while (cap):

    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_r1 = np.array([0,100,100])
    u_r1 = np.array([10,255,255])
    l_r2 = np.array([160,100,100])
    u_r2 = np.array([180,255,255])

    mask = cv.inRange(hsv, l_r1, u_r2) + cv.inRange(hsv, l_r2, u_r2)


    res = cv.bitwise_and(frame, frame, mask=mask)

    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    max_w=0
    max_h=0
    max_x=0
    max_y=0


    for cnt in contours:
        area = cv.contourArea(cnt)
        if area>200:   
            x, y, w, h = cv.boundingRect(cnt)
            if (w*h > max_h*max_w):
                max_h=h
                max_w=w
                max_x=x
                max_y=y
        
    cv.rectangle(frame, (max_x, max_y), (max_x + max_w, max_y + max_h), (0, 255, 0), 3)

    cv.imshow("frame", frame)
#    cv.imshow("mask", mask)
#    cv.imshow("res", res)

   
    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
