#imports
from sensor import sensor
import time
import csv

class control():
    
    """
    This class handles all the backend functionality of the program.
    
    @author Luke, Sam, Ben
    """
    
    def __init__(self):
        
        """
        The initialisation function for the control class
        """
        
        #The lux values will be stored in this list
        self.return_data = []

        #initialise the sensor class
        self.sen = sensor()       
        

    
    def get_raw_data(self):
        
        """
        This function will return the raw data collected from the sensor
        module.
        @return 2d list
        """
        
        return(self.return_data)
    
    def get_peak(self):
        
        """
        This function will calculate the key statistics wanted for
        the collected data.
        """
        
        sensor_1_list = []

        for i in self.return_data:
            sensor_1_list.append(i[0])

        sensor_peak = max(sensor_1_list)
                
        return(sensor_peak)
    
    def export_data(self):
        
        """
        This file exports the fluorescence reading from each light
        sensor, against time, to a csv file.
        """
        
        
        output_file = 'export.csv'
        data = self.get_raw_data()
        
        if data != []:
            print('Writing to file', output_file)
            with open(output_file, 'w',) as csvfile:
                fluorescence_levels = csv.writer(csvfile)
                fluorescence_levels.writerow(['sensor_1','Time'])
                for i in data:
                    fluorescence_levels.writerow(i)
            print('done')
                    
        else:
            print('no recorded data')
    

        
    def calculate_purity(self, purity_coefficent_1):
        
        """
        This function will calculate the purity of the sample
        """

        #acquire inputs
        data = self.get_raw_data()

        #initialise variables
        total_1 = 0

        #calculate sum of sensor inputs
        for i in data:
            total_1 += i[0]

        #calculate time elapsed and number of data points per sensor
        time_elapsed = data[-1][1]
        number_data_points = len(data)
        
        #calculate purity using simplified sum 
        purity_1 = (total_1*time_elapsed*purity_coefficent_1)/number_data_points
        
        #give all the purity values (one for each sensor method - these need to be assigned appropriately when reported)
        return(purity_1)
        
    
    def record_data(self, no_of_samples, interval):
        
        """
        This function will get a sample every interval
        seconds until it has all the required samples.
        returns true when done
        @param no_of_samples int
        @param interval float
        """

        #tempory storage while function is completing
        temp_return_list = []

        #colec
        for i in range(0,no_of_samples):

            print(i)
            sensor_value = self.sen.get_sensor_value()

            temp_return_list.append([sensor_value,(i*interval)])

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
            
            sensor_1_value = self.sen.get_sensor_value()

            # checks if the value is a float else rase exception

            if type(sensor_1_value) != float:
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

        peak = self.get_peak()
        threshold = 5
        
        if peak >= threshold:
            result = True
            
        else:
            result = False

        return(result)



     
        

