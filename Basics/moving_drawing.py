import cv2 
import numpy as np


# True when pressed 
drawing = False
ix,iy = -1,-1



def draw_rectangle(event,x,y,flags,params):
    global ix, iy, drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y # where mouse is located (starting rectangle)
        
    elif event == cv2.EVENT_MOUSEMOVE:
        # if mouse is moving
        if drawing == True:
            # start point ix,iy (stored variables)
            # end point x,y (last variables [ending])
            cv2.rectangle(img,(ix,iy),(x,y),(255,0,255),-1)
    
    elif event == cv2.EVENT_LBUTTONUP: # release
        drawing = False
        # redraw rectangle
        cv2.rectangle(img,(ix,iy),(x,y),(255,0,255),-1)

# image

img = np.zeros((512,512,3))

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',draw_rectangle)

while True: 
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()