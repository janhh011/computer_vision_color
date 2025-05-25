import cv2
from util import get_limits
from PIL import Image


yellow = [0,255,255] #red in BGR

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    #translate frame in HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #get lower and upper limit of color yellow
    lowerlimit, upperlimit = get_limits(color=yellow)

    #create a mask of the frame where only the selected colors are visible
    mask = cv2.inRange(hsvImage, lowerlimit, upperlimit)

    #convert the array to PILLOW
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    
    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

    cv2.imshow("Frame", frame)
    if(cv2.waitKey(1)) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
