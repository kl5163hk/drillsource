import time
from datetime import datetime as dt, timedelta
from tkinter import Tk
import tkinter as tk
import threading

class Root(tk.Tk):
    
    def gettime(self):
        self.nowtime = dt.now()
        self.nowtime.strftime("%D - %m - %Y | %H : %M : %S")
        self.showtime = tk.Label(text=str(self.nowtime))
        self.showtime.grid(column=0,row=0) 
        self.showtime.configure(font=40)
        threading.Timer(1, self.gettime).start()
    
    def __init__(self):
        super(Root, self).__init__()


        # Part = Window Configuration
        self.title("Clock - KL5163 Studio")
        self.geometry("600x600")


        # Part = Content
        self.gettime()

        #### Usinhg For In loop to destroy the outdated data !!!!!s
        

master = Root()
master.mainloop()
