import cv2 as cv
from util import get_limits
from PIL import Image  # use for bounding box

detect_red = [255, 255, 255]  # yello in BGR colorspace
webCam = cv.VideoCapture(1, cv.CAP_DSHOW)

while True:
    ret, frame = webCam.read()

    # Convert: RGB -> HSV
    webCam_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Get the upper and lower limit of the HSV colorspace, of the color you want to detect
    lowerLimit, upperLimit = get_limits(color=detect_red)

    mask = cv.inRange(webCam_hsv, lowerLimit, upperLimit)

    final_mask = Image.fromarray(mask)
    bbox = final_mask.getbbox()

    print(bbox)

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    if ret == False:
        print("Camera is not working!")
        break
    # print(f"ret: {ret}")
    # print(f"frame: {frame}")

    cv.imshow("Frame", mask)
    # cv.imshow("HSV", webCam_hsv)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

webCam.release()
webCam_hsv.release()
cv.destroyAllWindows()
