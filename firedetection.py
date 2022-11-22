import numpy as np
import cv2
import serial
import time


fire_cascade = cv2.CascadeClassifier('fire_detection.xml')

ser1 = serial.Serial('COM8',9600)  #ARDUINO CONNECTION SETUP
capn = cv2.VideoCapture(0)
cap = cv2.VideoCapture(1)
while True:
    
    ret0, img0 = cap.read()
    ret1, img1 = capn.read()

    gray = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(img0, 1.2, 5)
    fire1 = fire_cascade.detectMultiScale(img1, 1.2, 5)
    #print("fire1", fire1, " Fire", fire)
    for (x,y,w,h) in fire:
        cv2.rectangle(img0,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img0[y:y+h, x:x+w]
        print ('Fire is detected.. in corridor!')
    for (x,y,w,h) in fire1:
        cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img1[y:y+h, x:x+w]
        print ('Fire is detected.. in room 2!')
        ser1.write('s'.encode())
        time.sleep(0.2)
    if (ret0):
        # Display the resulting frame
        cv2.imshow('Cam 0', img0)

    if (ret1):
        # Display the resulting frame
        cv2.imshow('Cam 1', img1)    
   # cv2.imshow('img',img0)
   # cv2.imshow('img',img1)

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
capn.release()

cv2.destroyAllWindows()
