import cv2

cap = cv2.VideoCapture(0)

## CALLBACK FUNCTION 

def draw_rect(event,x,y,flags,params):
    
    global pt1,pt2,topleft_Clicked,bottomRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:

        # RESET THE RECTANGLE ( CHECKS IF THE RECTANGLE I THERE)
        if topleft_Clicked == True and bottomRight_clicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topleft_Clicked = False
            bottomRight_clicked = False

        # POINT 1 is defined
        if topleft_Clicked == False:
            pt1 = (x,y)
            topleft_Clicked = True

        elif bottomRight_clicked == False:
            pt2 = (x,y)
            bottomRight_clicked = True


## GLOBAL VARIABLES

pt1 = (0,0)
pt2 = (0,0)
topleft_Clicked = False
bottomRight_clicked = False

## CONNECT TO CALLBACK 
cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rect)

while True:

    ret, frame = cap.read()

    ## DRAWING ON FRAME BASED ON GLABAL VARIABLES

    if topleft_Clicked == True:
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)
    
    if topleft_Clicked and bottomRight_clicked:
        cv2.rectangle(frame,pt1,pt2,color=(0,0,255),thickness=5)



    cv2.imshow('Test',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
