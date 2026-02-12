import cv2
import numpy as np

cp = cv2.VideoCapture(0)

while True:
    ret, frame = cp.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red Color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])

    red_mask = cv2.inRange(hsv_frame, low_red, high_red) # we create mask on hsv frame
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)

    key =cv2.waitKey(1)
    if key == ord('q'):
        break