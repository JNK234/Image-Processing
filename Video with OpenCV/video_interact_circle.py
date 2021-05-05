import cv2
import numpy as np

cap = cv2.VideoCapture(0)

## CALLBACK FUNCTION 
def draw_circle(event,x,y,flags,param):
    global pt1,pt2,center_click,end_click

    if event == cv2.EVENT_LBUTTONDOWN:

        if center_click == True and end_click == True:
            pt1 = (0,0)
            pt2 = (0,0)
            center_click = False
            end_click = False

        if center_click == False:
            pt1 = (x,y)
            center_click = True

        elif end_click == False:
            pt2 = (x,y)
            end_click = True


## GLOBAL VARIABLES 
pt1 = (0,0)
pt2 = (0,0)
center_click = False
end_click = False

## CONNECT WITH FUNCTION

cap = cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_circle)

while True:

    ret,frame = cap.read()

    if center_click == True and end_click == True:
        r = int(np.sqrt(np.square(pt1[0]-pt2[0]) + np.square(pt1[1]-pt2[1])))
        cv2.circle(frame,pt1,r,(255,0,0),5)
    
    if center_click == True:
        cv2.circle(frame,pt1,3,(0,255,0),-1)

    cv2.imshow('Test',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

