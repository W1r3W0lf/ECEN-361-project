import cv2
import numpy as np
cap = cv2.VideoCapture(0)


screen_width = 160
screen_hight = 120

cap.set(3, screen_width)
cap.set(4, screen_hight)


# How large should each turn zone be valid values 0 to 0.5
turn_zone_size = 0.33

right_zone = screen_width * turn_zone_size
left_zone = screen_width * (1-turn_zone_size)

WHITE = (255,255,255)
GREEN = (0,255,0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    low_b = np.uint8([0,70,70])
    high_b = np.uint8([60,255,255])
    mask = cv2.inRange(hsv, low_b, high_b)
    contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
    if len(contours):
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"]:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            print(f"CX : {cx}  CY : {cy}")
            if cx >= left_zone : # 120
                print("Turn Left")
            elif cx <= right_zone : #40
                print("Turn Right")
            else:
                print("On Track!")
            cv2.circle(frame, (cx,cy), 5, WHITE, -1)
    else :
        print("I don't see the line")
    cv2.drawContours(frame, c, -1, GREEN, 1)
    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
