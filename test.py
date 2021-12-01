import cv2
import numpy as np
import sys
sys.path.insert(0, './raspirobotboard3/python')
from rrb3 import*
cap = cv2.VideoCapture(0)


screen_width = 160
screen_hight = 120

cap.set(3, screen_width)
cap.set(4, screen_hight)

# How large should each turn zone be valid values 0 to 0.5
turn_zone_size = 0.33

right_zone = screen_width * turn_zone_size
left_zone = screen_width * (1-turn_zone_size)

rr = RRB3(6, 6)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    low_b = np.uint8([0,70,70])
    high_b = np.uint8([60,255,255])
    mask = cv2.inRange(hsv, low_b, high_b)
    contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0 :
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] !=0 :
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            print("CX : "+str(cx)+"  CY : "+str(cy))
            if cx >= left_zone : # 120
                print("Turn Left")
                rr.set_motors(1, 0, 1, 0)
            elif cx <= right_zone : #40
                print("Turn Right")
                rr.set_motors(1, 1, 1, 0)
            else:
                print("On Track!")
                rr.set_motors(0, 0, 1, 0)
            cv2.circle(frame, (cx,cy), 5, (255,255,255), -1)
    else :
        print("I don't see the line")
        rr.set_motors(0, 0, 0, 0)
    cv2.drawContours(frame, c, -1, (0,255,0), 1)
    cv2.imshow("Mask",mask)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xff == ord('q'):   # 1 is the time in ms
        break
cap.release()
cv2.destroyAllWindows()
