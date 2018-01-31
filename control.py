#imports
from sensor import sensor
import time


class control():
    
    """
    This class handles all the backend functionality of the program.
    
    @author lrj509
    """
    
    def __init__(self):
        
        """
        The initialisation function for the control class
        """
        
        self.return_data = []

        self.sen = sensor()       
        
        return

    
    def get_raw_data(self):
        
        """
        This function will return the raw data collected from the sensor
        module.
        @return 2d list
        """
        
        if self.return_data == []:
            raise Exception("you havent recorded a sample yet")
        
        return(self.return_data)
    
    def get_key_stats(self):
        
        """
        This function will calculate the key statistics wanted for
        the collected data.
        """
        
        sensor_1_list = []
        sensor_2_list = []
        sensor_3_list = []

        for i in self.return_data:
            sensor_1_list.append(i[0])
            sensor_2_list.append(i[1])
            sensor_3_list.append(i[2])

        sensor_1_peak = max(sensor_1_list)
        sensor_2_peak = max(sensor_2_list)
        sensor_3_peak = max(sensor_3_list)
        
        key_stats = (1,1,1)
        
        #calculate the stats
        
        return(key_stats)
    
    def export_data(self, export_type):
        
        """
        This file exports the fluorescence reading from each light
        sensor, against time, to a csv file.
        """
        import csv
        
        fl = '/home/pi/Workshops52M/Workshop3/fluorescence_levels.csv'
        x = [[12.0,12.0,12.0,12.0],[12.0,12.0,12.0,12.0],[12.0,12.0,12.0,12.0]]
        
        print('Writing to file', fl)
        with open(fl, 'w',) as csvfile:
            fluorescence_levels = csvwriter(csvfile)
            fluorescence_levels.writerow(['sensor_1','sensor_2','sensor_3','Time'])
            for i in x:
                flourescence_levels.writerow(i)
    
    def calculate_purity(self):
        
        """
        Working progress. Converts peak fluorescence recorded into
        a sample purity percentage.
        """
        #recorded fluorescence
        x = 10.0

        #max fluorescence
        y = 12.0

        purity = (x*y)/100

        return(purity)
    
    def record_data(self, no_of_samples, interval):
        
        """
        This function will get a sample every interval
        seconds until it has all the required samples.
        returns true when done
        @param no_of_samples int
        @param interval float
        @return bool
        """

        #tempory storage while function is completing
        temp_return_list = []

        #colec
        for _ in range(0,no_of_samples):
            
            sensor_1_value = self.sen.get_sensor_1_value()
            sensor_2_value = self.sen.get_sensor_2_value()
            sensor_3_value = self.sen.get_sensor_3_value()

            temp_return_list.append([sensor_1_value,sensor_2_value,sensor_3_value])

            time.sleep(interval)

            
            
        self.return_data = temp_return_list
        
    def self_check(self):
        
        """
        This function will perform a self check on all the
        components to make sure that they all return values, ie make sure
        theyre connected and working
        """
        
        try:
            #tries to get a value from each sensor
            
            sensor_1_value = self.sen.get_sensor_1_value()
            sensor_2_value = self.sen.get_sensor_2_value()
            sensor_3_value = self.sen.get_sensor_3_value()

            # checks if the value is a float else rase exception

            if type(sensor_1_value) != float:
                raise Exception()

            if type(sensor_2_value) != float:
                raise Exception()

            if type(sensor_3_value) != float:
                raise Exception()

            #if the sensors dont return a value or is in the wrong type
            #the code will fail before here and get caught by the catch.
            #otherwise its sets the pass or fail condition to true
            
            pass_or_fail = True
            

        except:
            #if the self check fails then it sets the pass or fail
            #condition to  false
            
            pass_or_fail = False
        
        
        return(pass_or_fail)

    def is_sample_posative(self):

        """
        This function will return true if the sample is posative or
        false if the sample tests negative.
        @return bool indecating the test result
        """

        #Not sure how im doing this

        result = False

        return(result)

        
     
        
x = control()
y = x.self_check()
x.record_data(10,0.5)
z = x.get_raw_data()

print(y)
print(z)
print("done")
