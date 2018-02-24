#Imports 
import tkinter as tk
from tkinter import PhotoImage
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageTk
from camera import camera
from control import control
from tkinter import messagebox

#initialise the control class
x = control()
y = camera()

class Demo1():
    
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
        self.button4 = tk.Button(self.frame, text = 'Is Sample Positive', width = 25, command = self.is_sample_positive)
        self.button4.pack()
        self.button5 = tk.Button(self.frame, text = 'Self Test', width = 25, command = self.run_self_test)
        self.button5.pack()
        self.button6 = tk.Button(self.frame, text = 'See Camera Output', width = 25, command = self.new_window_cam)
        self.button6.pack()
        self.frame.pack()

    def new_window_cd(self):
        
        """
        creates the window for saying that the data has completed recording
        """
        
        self.newWindow = tk.Toplevel(self.master)
        self.app = DataDone(self.newWindow)
    
    def new_window_plot(self):
        
        """
        creates the window for plotting the data
        """
        
        self.newWindow = tk.Toplevel(self.master)
        self.app = plot_data(self.newWindow)
        
    def new_window_cam(self):
        
        """
        creates the window for showing the camera output
        """
        
        self.newWindow = tk.Toplevel(self.master)
        self.app = cam_output(self.newWindow)
        
    def run_self_test(self):
        
        """
        runs the self check, aborts the process if the self check fails
        """
        
        result = x.self_check()
        
        if result == False:
            print('the self test has failed: aborting')
            self.master.destroy()
            
        else:
            print('The self check has completed, there were no reported errors')
            
    def is_sample_positive(self):
        
        """
        creates a dialogue box saying if the sample is positive or negative 
        """
        
        if x.is_sample_positive() == True:
            messagebox.showinfo("Result", "The sample is positive")
            
        else:
            messagebox.showinfo("Result", "The sample is not positive")      
        



class DataDone():
    
    """
    
    window for when the data has finished collecting, will displace a picture 
    of a dog
    
    """
    
    def __init__(self, master):
        
        """
        
        The init method
        
        """
        
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
        
        """
        
        closes the window
        
        """
        
        self.master.destroy()
        
class plot_data():
    
    """
    
    This class handles displaying the data in the form of a graph. all of the 
    handling is done in the init method
    
    """
    
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
        
class cam_output():
    
    """
    
    displays the camera output
    
    """
    
    def __init__(self, master):
        
        """
        
        The init method
        
        """
        
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.label = tk.Label(self.frame, text="camera output")
        self.label.pack(pady=10,padx=10)
        
        y.get_picture()       
        
        self.img = ImageTk.PhotoImage(Image.open('image.jpg'))
        self.panel = tk.Label(self.frame, image = self.img)
        self.panel.image = self.img
        self.panel.pack()
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        
        
    

    def close_windows(self):
        
        """
        
        closes the window
        
        """
        
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

main()
