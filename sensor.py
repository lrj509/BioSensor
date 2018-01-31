class sensor():
    
    """
    This class encapsulates all of the sensor functions for easy use. 
    
    @author lrj509
    """
    
    def __init__(self):
        
        """
        The init method
        """
        
        return
    
   def get_sensor_1_value(self): #Analogue sensor

        #Import python modules
           import RPi.GPIO as GPIO
           import time
           
        # Set variables
           sensor_1_pin=
           
        # Pi setup
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(gpio_pin, GPIO.OUT)

        def rc_time(gpio_pin):

            # output on the pin to discharge capacitor
            GPIO.setup(gpio_pin, GPIO.OUT)
            GPIO.output(gpio_pin, GPIO.LOW)
            time.sleep(0.05)

            # reset as input
            GPIO.setup(gpio_pin, GPIO.IN)

            # count loops until voltage across capacitor reads high
            timenow = time.time()
            while (GPIO.input(gpio_pin) == GPIO.LOW):
                pass
    
            return time.time() - timenow
     

            # catch exceptions and a clean exit
        try:
            # print light levels every 5 seconds for one minute
            t = 0
            while t <= 60:       
                if t % 5 == 0: # if t modulus 5 is zero
                    # check sensor
                    rc = rc_time(sensor_1_pin)
                    print(t, rc)
        
            t += 1 # increment loop
            time.sleep(0.95 - rc) # wait 1 second

        except:
            print('An error or exception occurred')

        finally:
            GPIO.cleanup()
        
<<<<<<< HEAD
        sensor_1_value = 12
    
    def get_sensor_2_value(self): #Digital sensor

        #Import python modules
            import time
            import tsl2591
            

        tsl = tsl2591.Tsl2591()  # initialize
        full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
        lux = tsl.calculate_lux(full, ir)  # convert raw values to lux

        return time.time() - timenow

        try:
            # print light levels every 5 seconds for one minute
            t = 0
            while t <= 60:       
                if t % 5 == 0: # if t modulus 5 is zero
                    print(t, lux)
        
        return(sensor_2_value)
    
    
=======
        sensor_1_value = 12.0
        
        return(sensor_1_value)
    
    def get_sensor_2_value(self):
        
        """
        Returns the value for sensor two.
        """
        
        sensor_2_value = 12.0
        
        return(sensor_2_value)
    
    def get_sensor_3_value(self):
        
        """
        Returns the value for sensor three.
        """
        
        sensor_3_value = 12.0
        
        return(sensor_3_value)
    
    
>>>>>>> ee7df814c973cc191089d87b42f6a0428956be5c
