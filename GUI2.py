#Imports 
import tkinter as tk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from control import control

"""
x = control()

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="IB-LJ BioSensor")
        label.pack(pady=10,padx=10)
        


        button = tk.Button(self, text="view Output graph",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="View Camera Output",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Output graph")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        
        x.get_raw_data()
        data = x.get_raw_data()
        
        if data == None:
            
            img = ImageTk.PhotoImage(Image.open('dog.jpg'))
            panel = tk.Label(self, image = img)
            panel.image = img
            panel.pack()
            
        else:    

            data2 = []
            for i in data:
                data2.append(i[0])
    
            plt.scatter((range(0,len(data2))),data2)
            plt.savefig('out', format = 'png')
            
            img = ImageTk.PhotoImage(Image.open('out'))
            panel = tk.Label(self, image = img)
            panel.image = img
            panel.pack()
        
        


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Camera Output")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        img = ImageTk.PhotoImage(Image.open('dog.jpg'))
        panel = tk.Label(self, image = img)
        panel.image = img
        panel.pack()
        
class CollectDataPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Collecting Data, Look at this dog")
        label.pack(pady=10,padx=10)
        
        img = ImageTk.PhotoImage(Image.open('dog.jpg'))
        panel = tk.Label(self, image = img)
        panel.image = img
        panel.pack()
        
        x.record_data()

app = SeaofBTCapp()
app.mainloop()
"""
#import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button2.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.panel = tk.Label(self, image = ImageTk.PhotoImage(Image.open('dog.jpg')))
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
