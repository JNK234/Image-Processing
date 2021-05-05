import cv2
import time

cap = cv2.VideoCapture('/Users/narasimhajwalapuram/Downloads/record.mp4')

if cap.isOpened() == False:
    print('ERROR FILE NOT FOUND OR WRONG CODEC USED')

while cap.isOpened():
    ret,frame = cap.read()

    if ret == True:

        # WRITER 20 FPS - to show the video in speed understandable to human
        # time.sleep(1/20)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else:
        break

cap.release()
cv2.destroyAllWindows()