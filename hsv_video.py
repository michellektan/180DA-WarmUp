"""
Detect Blue Objects in HSV

Reference: 
    https://answers.opencv.org/question/200861/drawing-a-rectangle-around-a-color-as-shown/?fbclid=IwAR3_P7pmzYS7Mw8sSBtK5d7szhg-RNjCkZzlrln65rmqrbxqHm10JTxzG1I
Modifications: 
    - Removed "show mask" function call. Only HSV frame is displayed.
    
"""

import numpy as np
import cv2  

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([100,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange (hsv, lower_blue, upper_blue)
    bluecnts = cv2.findContours(mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(bluecnts)>0:
        blue_area = max(bluecnts, key=cv2.contourArea)
        (xg,yg,wg,hg) = cv2.boundingRect(blue_area)
        cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)

    cv2.imshow('frame',frame)

    k = cv2.waitKey(5) 
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()