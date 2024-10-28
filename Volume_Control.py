import cv2
import time
import numpy as np
import Hand_tracking_module as htm
import math

# pip install pycaw, its a library for volume control you can copy a template directly
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam, hCam = 640, 480   # we have defined height of camera and width of camera

cap = cv2.VideoCapture(0)
cap.set(3, wCam) # we have set height and width of camera accordingly, 3 and 4 are ids with camera properties 
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector()

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange() # (min volume, max voume)
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400  # its the height of lowest point of volume bar rectangle 
volPer = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img) # it will track a landmarks of hand in a image
    lmList = detector.findPosition(img, draw=False)  # we have extracted landmarks of each ids, draw = false means we dont want to draw it 

    if len(lmList) != 0: # lmlist is not empty
        # lmlist : (id,x co-ordinate, y co-ordinate)
        x1, y1 = lmList[4][1], lmList[4][2] # x1 and y1 are coordinates of top most point of thumb
        x2, y2 = lmList[8][1], lmList[8][2] # x2 and y2 are coordinates of top most point of thumb

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2 # center coordinates of top point of index finger and thumb

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1) # we have used hypoteneuse function of math library to get length of a line between thumb and index finger

        # Hand range 10 - 220 , we got this after printing length in terminal
        # Volume range -65 - 0, we got this by printing Volrange

        vol = np.interp(length, [50, 220], [minVol, maxVol]) # it makes a graph between point (50,-65) and (300,0) and with changing values of length, vol changes 
        volume.SetMasterVolumeLevel(vol, None) # it changes computer volume as we change its parameter
        volBar = np.interp(length, [50, 220], [400, 150]) # 150 is height of highest point of volume bar rectangle
        volPer = np.interp(length, [50, 220], [0, 100])

        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    # Sidebar showing volume level
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    

    # Display frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    
    cv2.imshow("Img", img)
    cv2.waitKey(1)