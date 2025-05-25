import numpy as np
import cv2

def get_limits(color : list)->list:
    c = np.uint8([[color]]) #put BGR value in a 1x1 Image (correct formatting for cv2)
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV) #translate BGR to HSV



    #cast to int to avoid overflow
    h=int(hsvC[0][0][0])

    #hsvC[0][0][0] → Hue, hsvC[0][0][1] → Saturation, hsvC[0][0][2] → Value
    lower_limit = max(h - 5, 0), 100, 100
    upper_limit = min(hsvC[0][0][0] + 5, 179), 255, 255

    #transfer limits to np arrays
    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)
    
    return lower_limit, upper_limit