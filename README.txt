BioSensor Project

This project was undertaken as part of the MSc BIO00052M Data Analysis and Programming
in the Biosciences module. 

To run the project, run the GUI.py code. If running on anaconda, comment out the sensor parts

Dependancies:

 - python 3 or greater
 - picamera
 - matplotlib
 - Python Imaging Library
 - tsl2591
 - Adafruit_CharLCD


Objectives for the project:

 - have a graphical user interface
 - to be able to export the data 
 - to be able to see the max peak of the data
 - to produce a graph of the sensor values
 - to have a self check
 - to be able to see if the sample is positive
 - to use a digital like sensor

example code:
#Previous (This has been kept to show the progression of code):
        
#        #calculate means of data
#        number_data_points = len(data)
#        mean_1 = total_1/number_data_points
#        mean_2 = total_2/number_data_points
#        mean_3 = total_3/number_data_points
#
#        # mean of data * time taken ----> gives overall light emitted
#        overall_light_1 = mean_1 * time_elapsed
#        overall_light_2 = mean_2 * time_elapsed
#        overall_light_3 = mean_3 * time_elapsed
#
#        # multiply by purity coefficient (determined using standards) to give purity
#        purity_1 = overall_light_1 * purity_coefficient
#        purity_2 = overall_light_2 * purity_coefficient
#        purity_3 = overall_light_3 * purity_coefficient
#
#        print(purity_1)
#        print(purity_2)
#        print(purity_3)
#
#        return(purity_1, purity_2, purity_3)        
#        
#        Previously:
#        Working progress. Converts peak fluorescence recorded into
#        a sample purity percentage.
#      
#        #recorded/peak fluorescence
#        x = 10.0
#
#        #max/100% fluorescence
#        y = 12.0
#
#        purity = (x*y)/100
#
#        return(purity)
