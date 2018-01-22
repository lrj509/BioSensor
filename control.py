

class control():
    
    """
    This class handles all the backend functionality of the program.
    
    @author lrj509
    """
    
    def __init__(self):
        
        """
        The initialisation function for the control class
        """
        
        return_data = []
        
        return

    
    def get_raw_data(self):
        
        """
        THis function will return the raw data collected from the sensor module
        """
        
        return(self.return_data)
    
    def get_key_stats(self):
        
        """
        
        """
        
        key_stats = (1,1,1)
        
        #calculate the stats
        
        return(key_stats)
    
    def export_data(self, export_type):
        
        """
        
        """
        
    
    def calculate_purity(self):
        
        """
        
        """
        purity = 0.45
        
        return(purity)
    
    def record_data(self, time):
        
        """
        
        """
        
        self.return_data = []
        
    def self_check(self):
        
        """
        
        """
        
        pass_or_fail = True
        
        return(pass_or_fail)
        
x = control()
x.export_data(12)
print("done")
