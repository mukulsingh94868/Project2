
import  cv2
#  staring  camera
cap=cv2.VideoCapture(0)
while  cap.isOpened() :
    status,frame=cap.read()
    #  converting  image  frame into gray scale 
    grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  
    print(frame.shape)
    #  text writing 
    font = cv2.FONT_HERSHEY_SIMPLEX   #   this  font  type  
    cv2.putText(frame,'MUKUL',(10,50), font, 2,(0,2,55),2,cv2.LINE_AA)
    cv2.imshow('live',frame)
    #cv2.imshow('livegray',grayimg)
    if  cv2.waitKey(10)   &   0xff  ==  ord('q')  :
        break
#cv2.destroyWindow('live')
cv2.destroyAllWindows()  #   this will destroy all windows 
#  to close camera
cap.release()
