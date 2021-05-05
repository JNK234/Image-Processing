import cv2
import numpy as np

########################
#### FUNCTION ##########

def drawCircle(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),-1)

cv2.namedWindow(winname = 'My_Drawing')

cv2.setMouseCallback('My_Drawing',drawCircle)

######################################
####### SHOWING IMAGE WITH OPENCV ####
######################################

img = np.zeros((512,512,3))

while True:
    cv2.imshow("My_Drawing",img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()

