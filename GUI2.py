#Imports 
import tkinter as tk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from control import control
import time
from tkinter import messagebox

#initialise the control class
x = control()

class Demo1:
    
    """
    
    This class handles the first screen, where the user chooses what to do
    
    """
    
    def __init__(self, master):
        
        """
        
        THe init function for the screen class, this populates the screen 
        with buttons
        
        """
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Collect Data', width = 25, command = self.new_window_cd)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text = 'Plot The Data', width = 25, command = self.new_window_plot)
        self.button2.pack()
        self.button3 = tk.Button(self.frame, text = 'export data', width = 25, command = x.export_data)
        self.button3.pack()
        self.button4 = tk.Button(self.frame, text = 'Is Sample Posative', width = 25, command = self.is_sample_posative)
        self.button4.pack()
        self.button5 = tk.Button(self.frame, text = 'Self Test', width = 25, command = self.run_self_test)
        self.button5.pack()
        self.frame.pack()
        
        self.y = 11

    def new_window_cd(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = DataDone(self.newWindow)
    
    def new_window_plot(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = plot_data(self.newWindow)
        
    def run_self_test(self):
        result = x.self_check()
        if result == False:
            print('the self test has failed: aborting')
            self.master.destroy()
            
        else:
            print('The self check has completed, there were no reported errors')
            
    def is_sample_posative(self):
        
        if x.is_sample_posative() == True:
            messagebox.showinfo("Result", "The sample is posative")
            
        else:
            messagebox.showinfo("Result", "The sample is not posative")

        

        
        
        



class DataDone:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.label = tk.Label(self.frame, text="The Data Has Collected, here is a dog")
        self.label.pack(pady=10,padx=10)
        
        x.record_data(10,0.1)
               
        
        self.img = ImageTk.PhotoImage(Image.open('dog.jpg'))
        self.panel = tk.Label(self.frame, image = self.img)
        self.panel.image = self.img
        self.panel.pack()
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        
        
    

    def close_windows(self):
        self.master.destroy()
        
class plot_data:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        
               
        
        
        data = x.get_raw_data()
        
        if data == []:
            
            self.label = tk.Label(self.frame, text="You Havent Collected Any Data")
            self.label.pack(pady=10,padx=10)
            
            self.img = ImageTk.PhotoImage(Image.open('dog2.jpg'))
            self.panel = tk.Label(self.frame, image = self.img)
            self.panel.image = self.img
            self.panel.pack()
            
        else:    
            
            self.label = tk.Label(self.frame, text="plot of the data")
            self.label.pack(pady=10,padx=10)

            data2 = []
            for i in data:
                data2.append(i[0])
    
            plt.scatter((range(0,len(data2))),data2)
            plt.savefig('out', format = 'png')
            
            self.img = ImageTk.PhotoImage(Image.open('out'))
            self.panel = tk.Label(self.frame, image = self.img)
            self.panel.image = self.img
            self.panel.pack()
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        
        
    

    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

main()
