import cv2
from cvzone.HandTrackingModule import HandDetector
import pyfirmata
import numpy as np

cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Camera couldn't Access!!!")
    exit()

#port = "/dev/tty.usbserial-2130"
#board = pyfirmata.Arduino(port)
#servo_pinX = board.get_pin('d:9:s') #pin 9 Arduino
#servo_pinY = board.get_pin('d:10:s') #pin 10 Arduino

detector = HandDetector(detectionCon=0.8)
servoPos = [90, 90] # initial servo position

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=True)

    if hands:
        # Get the coordinates of the hand's center
        lmList = hands[0]['lmList']
        hx, hy = lmList[9][0], lmList[9][1]  # Using landmark 9 (center of the palm)
        pos = [hx, hy]

        # Convert coordinates to servo degrees
        servoX = np.interp(hx, [0, ws], [180, 0])  # Inverse x-axis
        servoY = np.interp(hy, [0, hs], [0, 180])

        servoPos[0] = max(0, min(180, servoX))
        servoPos[1] = max(0, min(180, servoY))

        cv2.circle(img, (hx, hy), 80, (0, 255, 0), 2)
        cv2.putText(img, str(pos), (hx+15, hy-15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.line(img, (0, hy), (ws, hy), (0, 0, 0), 2)
        cv2.line(img, (hx, hs), (hx, 0), (0, 0, 0), 2)
        cv2.circle(img, (hx, hy), 15, (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "HAND DETECTED", (850, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    else:
        cv2.putText(img, "NO HAND", (880, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        cv2.circle(img, (640, 360), 80, (0, 0, 255), 2)

    cv2.putText(img, f'Servo X: {int(servoPos[0])} deg', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.putText(img, f'Servo Y: {int(servoPos[1])} deg', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    #servo_pinX.write(servoPos[0])
    #servo_pinY.write(servoPos[1])

    cv2.imshow("Hand Tracking", img)
    cv2.waitKey(1)
