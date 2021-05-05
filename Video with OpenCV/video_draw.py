import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Tope left corner co-ordinate
x = width // 2
y = height //2

# Width and height of rectangle
w = width // 4
h = height // 4

# Bottom right co-ordinate x + w and h + y
 
while True:

    ret, frame = cap.read()

    cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,0,255),thickness =4)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
