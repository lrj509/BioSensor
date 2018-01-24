class camera():
    
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
        
        import time
        import picamera

        with picamera.PiCamera() as camera:

            camera.start_preview()
            time.sleep(0) 
            camera.capture('/home/pi/Desktop/image.jpg') #Saves image to the desktop, can change to another location
            camera.stop_preview()
        
        return 
    
    def get_interpreted_picture(self):
        
       import Image #Might need to install Python image library
       myImage=Image.open('image name')
       myImage.show() #to display image 

        black = makeColor (0,0,0)
        red= makeColor(255,0,0) #Change colour for colour of luminescence 

    #To calculate number of pixels of a given colour, black should be background of the image
       for pixel in getPixels(picture):
           color = getColor(pixel)
           if color == black: numblacks += 1
           else color == red: numreds += 1
           print('black =' + str(black) + 'red =' str(red))

        return 
        
    
