# BioSensor

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
