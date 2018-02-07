class camera():

#Import python modules
    import time
    import picamera
    import cv2
    import numpy as np

    """
    This class handles all the camera functions.
    
    @author lrj509
    """
    
    def __init__(self):
        
        """
        The init method for the camera class
        """
        
        return 
    
    def get_picture(self):
        
        with picamera.PiCamera() as camera:

            camera.start_preview()
            time.sleep(0) 
            camera.capture('/home/pi/Desktop/image.jpg') #Saves image to the desktop, can change to another location
            camera.stop_preview()
        
        return 
    
    def get_interpreted_picture(self):
        
        img=cv2.imread("your_image.png",0)

    def nothing(x):
        pass

    cv2.namedWindow('image')

    cv2.createTrackbar('min','image',0,255,nothing)
    cv2.createTrackbar('max','image',0,255,nothing)

    while(1):

     a = cv2.getTrackbarPos('min','image')
     b = cv2.getTrackbarPos('max','image')
     ret,thresh=cv2.threshold(img,a,b,cv2.THRESH_BINARY_INV) #Thresholds the image
     cv2.imshow("output",thresh)
     k = cv2.waitKey(10) & 0xFF
     if k == 27:
        break
    
    print cv2.countNonZero(thresh) #Counts the nuber of white pixels and gives the output
    cv2.destroyAllWindows()

        return 
        
    
