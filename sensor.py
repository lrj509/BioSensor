#Import python modules
#import RPi.GPIO as GPIO
import time
import tsl2591
import Adafruit_CharLCD as LCD


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
    
##
##    def get_sensor_1_value(self):
##        #Analogue sensor
##           
##        # Set variables
##        gpio_pin= 12
##         
##        # Pi setup
##        GPIO.setmode(GPIO.BCM) 
##
##
##
##
##
##        # output on the pin to discharge capacitor
##        GPIO.setup(gpio_pin, GPIO.OUT)
##        GPIO.output(gpio_pin, GPIO.LOW)
##        time.sleep(0.05)
##
##        # reset as input
##        GPIO.setup(gpio_pin, GPIO.IN)
##
##        # count loops until voltage across capacitor reads high
##        timenow = time.time()
##        ctr = 0
##        while (GPIO.input(gpio_pin) == GPIO.LOW):
##            ctr += 1
##
##        GPIO.cleanup()
##
##        return ctr
## 
        



def get_sensor_2_value(): #Digital sensor

    tsl = tsl2591.Tsl2591()  # initialize
    full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
    lux = tsl.calculate_lux(full, ir)  # convert raw values to lux
    print ('Lux:', lux)
    digital = round(lux,1)
    return(digital)

##
##def LCD(self, time_to_sleep): #LCD screen
##
##    """
##    This method displays the lux value on the LCD output display
##
##    """
##    return

x = sensor()

# Raspberry Pi pin configuration:
lcd_rs        = 7  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 8
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4


# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)


zxc = 'Lux:' + str(get_sensor_2_value()) #The message to be displayed on the lcd
# display a two line message
print(zxc)
lcd.message(zxc)
print(1)
#Displays output for time_to_sleep seconds and then clears message
time.sleep(5)
print(2)
lcd.clear()

#
#x.LCD(1)
   
##            
##    return time.time() - timenow
##
##    try:
##
##            # print light levels every 5 seconds for one minute
##            t = 0
##            while t <= 60:       
##                if t % 5 == 0: # if t modulus 5 is zero
        #return (sensor_2_value)
####        
##        #return(1.0)
##
##x = sensor()
##y = x.get_sensor_2_value()


