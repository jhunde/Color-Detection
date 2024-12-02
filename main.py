import cv2 as cv
from util import get_limits
from PIL import Image  # use for bounding box

detect_red = [0, 255, 255]  # yellow in BGR colorspace
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

    print(bbox)  # For testing

    # Create a bounding box
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    if ret == False:
        print("Camera is not working!")
        break

    cv.imshow("Frame", frame)

    # Break webcam if 'q' is selected from the keyboard
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

webCam.release()
webCam_hsv.release()
cv.destroyAllWindows()
