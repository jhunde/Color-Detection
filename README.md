# Color Detection Project


> **Note:** If you want to check the version of opencv your're currently using do the following: 
> 1. Open terminal
> 2. Invoke the Python interpreter by inserting: `python`
> 3. `import cv2`
> 4. `print(OpenCV version, cv2.__version__)`
>
> If would like to check the visions for `Pillow`, and `numPy` make sure to import them first. 
> Example: `import PIL` & `import numPy`


## Required Installation  
> **Note:** You must install all the required dependencies

```txt
opencv-python==4.10.0.84
numpy==2.1.3
Pillow==11.0.0
```
Then run: `pip install -r requirements`

## Activate Webcam 
> **Note:** Since we'll be using OpenCV make sure to `import cv2 as cv`


```python
webCam = cv.VideoCapture(1, cv.CAP_DSHOW)
```

> **Side Note:** Since I'm using external camera, I've notice a delay so I'm using `cv.CAP_DSHOW` to stop the delay. This is optional so use it if necessary. 

```python
while True:
    ret, frame = webCam.read()

    if ret == False:
        print("Camera is not working!")
        break

    # Visualize video 
    cv.imshow("Frame", frame)

    # 1ms delay and quite if 'q' is selected
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

webCam.release()
cv.destroyAllWindows()
```

## Convert BGR Image to HSV
```python
    webCam_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
```
 
 ## Detect the Color 
 
 ### Get the Upper and Lower Limit of HSV Colorspace 
> **Note:** Make sure to import util.py file (`from util import get_limits`) to access the get_limits function


```python
# Get the upper and lower limit of the HSV colorspace, of the color you want to detect
lowerLimit, upperLimit = get_limits(color=detect_red)
```
```python
def get_limits(color):
    c = np.uint8([[color]])  # BGR value to convert to HSV (return uint8)
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    h = hsvC[0][0][0]  # Hue
    lowerLimit = (h - 10, 100, 100)
    upperLimit = (h + 10, 255, 255)

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit
```
---

### Detect the Color and Get the Bounding Box
```python
mask = cv.inRange(webCam_hsv, lowerLimit, upperLimit)
    final_mask = Image.fromarray(mask)
    bbox = final_mask.getbbox()
```
![mask](/GIFs/mask.gif)

`bbox` give us the edges of the bounding box, so we will use that to get finish creating the bounding box on the webcam. 

```python
# Create a bounding box
if bbox is not None:
    x1, y1, x2, y2 = bbox
    frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

cv.imshow("Frame", frame)
```
![Frame](/GIFs/frame.gif)
