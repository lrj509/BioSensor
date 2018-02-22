#Import python modules
#import tsl2591
#import Adafruit_CharLCD as LCD


class sensor():

    """
    This class encapsulates all of the sensor functions for easy use. 
    
    @author Amy, Adam, Luke
    """


    def get_sensor_value(self): 
        
        """
        
        Gets the digital sensor value
        
        
    
        tsl = tsl2591.Tsl2591()  # initialize
        full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
        lux = tsl.calculate_lux(full, ir)  # convert raw values to lux
        print ('Lux:', lux)
        digital = round(lux,1)
        return(digital)
        """
        return(1.0)


    def LCD(self, time_to_sleep): #LCD screen
    
        """
        This method displays the lux value on the LCD output display
    
             
        
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
        
        
        #The message to be displayed on the lcd
        display_message = 'Lux:' + str(self.get_sensor_value()) 
        
        #clears the screen
        lcd.clear()
        
        # display a two line message
        lcd.message(display_message)
        #Displays output for time_to_sleep seconds and then clears message
        
        """
        
        return
        


