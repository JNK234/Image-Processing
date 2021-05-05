import cv2
import numpy as np

########################
#### VARIABLES ##########
########################

# True when mouse is clicked alse false
drawing = False
ix = -1
iy = -1

########################
#### FUNCTION ##########
########################

def drawRect(event,x,y,flags,params):
    
    global drawing,ix,iy

    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
         
######################################
####### SHOWING IMAGE WITH OPENCV ####
######################################

img = np.zeros((512,512,3))

cv2.namedWindow(winname = 'my_drawing')
cv2.setMouseCallback('my_drawing',drawRect)

while True:
    cv2.imshow('my_drawing',img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()

     