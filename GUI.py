from tkinter import * 
from control import control


x = control()
print(x.self_check())

class GUI():
    
    """
    This class handles all the frontend functionality of the program.
    
    @author lrj509
    """
    
    def __init__(self,master):
        
        """
        the init method for the class
        """
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.self_test())
        self.hi_there.pack(side=LEFT)
        
        
        
    def self_test(self):
        
        """
        This function will call the self test in the backend, displaying true 
        or false if it sucseeds or fails retrospectily.
        """
        
        result = x.self_check()
        
        #Error checking 
        
        if type(result) != bool:
            raise Exception("Self check should return a bool")
            
        else:
            print(result)
            
    
    
    
    
root = Tk()

prog = GUI(root)

root.mainloop()
root.destroy() 
