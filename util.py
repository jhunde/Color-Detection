import numpy as np
import cv2 as cv


def get_limits(color):
    c = np.uint8([[color]])  # BGR value to convert to HSV (return uint8)
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    h = hsvC[0][0][0]  # Hue
    lowerLimit = (h - 10, 100, 100)
    upperLimit = (h + 10, 255, 255)

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit
