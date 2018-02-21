#imports
from sensor import sensor
import time
import csv

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
    
    def export_data(self):
        
        """
        This file exports the fluorescence reading from each light
        sensor, against time, to a csv file.
        """
        
        
        fl = 'export.csv'
        x = self.get_raw_data()
        
        if x != []:
            print('Writing to file', fl)
            with open(fl, 'w',) as csvfile:
                fluorescence_levels = csv.writer(csvfile)
                fluorescence_levels.writerow(['sensor_1','sensor_2','sensor_3','Time'])
                for i in x:
                    fluorescence_levels.writerow(i)
            print('done')
                    
        else:
            print('no recorded data')
    

        
    def calculate_purity(purity_coefficent_1, purity_coefficient_2, purity_coefficient_3):

        #acquire inputs
        data =[[1,1,1,0],[1,2,2,0.5],[1,1,1,1],[1,1,1,1.5]]

        #initialise variables
        total_1 = 0
        total_2 = 0
        total_3 = 0

        #calculate sum of sensor inputs
        for i in data:
            total_1 += i[0]
            total_2 += i[1]
            total_3 += i[2]

        #calculate time elapsed and number of data points per sensor
        time_elapsed = data[-1][3]
        number_data_points_1 = len(data[0])
        number_data_points_2 = len(data[1])
        number_data_points_3 = len(data[2])
        
        #check values
        print(total_1)
        print(total_2)
        print(total_3)
        print(data[-1][3])
        
        #calculate purity using simplified sum 
        purity_1 = total_1*time_elapsed*purity_coefficient_1/number_data_points_1
        purity_2 = total_2*time_elapsed*purity_coefficient_2/number_data_points_2
        purity_3 = total_3*time_elapsed*purity_coefficient_3/number_data_points_3

        print(purity_1)
        print(purity_2)
        print(purity_3)
        #give all the purity values (one for each sensor method - these need to be assigned appropriately when reported)
        return(purity_1, purity_2, purity_3)
        
        #error checking
        
""" Previous:
        #calculate means of data
        number_data_points = len(data)
        mean_1 = total_1/number_data_points
        mean_2 = total_2/number_data_points
        mean_3 = total_3/number_data_points

        # mean of data * time taken ----> gives overall light emitted
        overall_light_1 = mean_1 * time_elapsed
        overall_light_2 = mean_2 * time_elapsed
        overall_light_3 = mean_3 * time_elapsed

        # multiply by purity coefficient (determined using standards) to give purity
        purity_1 = overall_light_1 * purity_coefficient
        purity_2 = overall_light_2 * purity_coefficient
        purity_3 = overall_light_3 * purity_coefficient

        print(purity_1)
        print(purity_2)
        print(purity_3)

        return(purity_1, purity_2, purity_3)        
        
        Previously:
        Working progress. Converts peak fluorescence recorded into
        a sample purity percentage.
      
        #recorded/peak fluorescence
        x = 10.0

        #max/100% fluorescence
        y = 12.0

        purity = (x*y)/100

        return(purity)
        """
    
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
        for i in range(0,no_of_samples):

            print(i)
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

        
     
        

