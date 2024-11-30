import cv2 as cv
from util import get_limits

detect_yellow = [0, 255, 255]  # yello in BGR colorspace
webCam = cv.VideoCapture(1, cv.CAP_DSHOW)

while True:
    ret, frame = webCam.read()

    # Convert: RGB -> HSV
    webCam_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Get the upper and lower limit of the HSV colorspace, of the color you want to detect
    lowerLimit, upperLimit = get_limits(color=detect_yellow)

    mask = cv.inRange(webCam_hsv, lowerLimit, upperLimit)

    if ret == False:
        print("Camera is not working!")
        break
    # print(f"ret: {ret}")
    # print(f"frame: {frame}")

    cv.imshow("Frame", frame)
    cv.imshow("HSV", webCam_hsv)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

webCam.release()
webCam_hsv.release()
cv.destroyAllWindows()
