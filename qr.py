import cv2
import numpy as np
import sys
import time

cap = cv2.VideoCapture(0)

# Based on https://learnopencv.com/opencv-qr-code-scanner-c-and-python/

# Display barcode and QR code location
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)

    # Display results
    cv2.imshow("Results", im)

qrDecoder = cv2.QRCodeDetector()


while True:
    qrDecoder = cv2.QRCodeDetector()
    ret, frame = cap.read()

    # Detect and decode the qrcode
    data,bbox,rectifiedImage = qrDecoder.detectAndDecode(frame)
    if len(data)>0:
        print("Decoded Data : {}".format(data))
        #display(frame, bbox)
        cv2.imshow("Results", frame)
        rectifiedImage = np.uint8(rectifiedImage);
        cv2.imshow("Rectified QRCode", rectifiedImage);
    else:
        print("QR Code not detected")
        cv2.imshow("Results", frame)


    if cv2.waitKey(1) & 0xff == ord('q'):   # 1 is the time in ms
        break

