import cv2
import numpy as np

cp = cv2.VideoCapture(0)

while True:
    ret, frame = cp.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red Color
    low_color = np.array([255, 255, 255])
    high_color = np.array([102, 255, 255])

    blue_mask = cv2.inRange(hsv_frame, low_color, high_color) # we create mask on hsv frame
    red = cv2.bitwise_and(frame, frame, mask=blue_mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Green", red)

    key =cv2.waitKey(1)
    if key == ord('q'):
        break