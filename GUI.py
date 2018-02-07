from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from control import control
import matplotlib.pyplot as plt

y = 11

x = control()
print(x.self_check())

x.record_data(10,0.5)
data = get_raw_data()

data2 = []
for i in data:
    data2.append(i[0])
qwertyiop = range(0,10)

plt.scatter(qwetyuiop,data2)




class GUI():
    
    """
    This class handles all the frontend functionality of the program.

    @authors awb519 & lwj
    """
    
    def __init__(self,master):
        
        """
        the init method for the class
        """
        frame = Frame(master)
        frame.grid()

        self.variable = StringVar(master)
        self.variable.set("Please Select") # default value

##        text = Text(frame)
##        text.insert(INSERT, "Hello....142.")
##        text.grid(row = 1, column=2)

        w = OptionMenu(frame, self.variable, "Opiates", "Cocaine")
        w.grid(row =1, column =1, padx= 80, pady=20)

        
        self.button = Button(
            frame, text="Run Test", fg="Black", command=self.result)
        self.button.grid(row =2, column =1, padx= 30,pady=5)




    def result(self):

        text.grid(row = 1, column=2)
        if y > 8:
            messagebox.showinfo("Positive", self.variable.get() + " presence confirmed", command=self.self_test())
        else:
            messagebox.showinfo("Negative", "Substance not detected", command=self.self_test())


 

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
