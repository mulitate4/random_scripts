
# importing whole module 
from tkinter import * 
from tkinter.ttk import *
import time
  
# importing strftime function to 
# retrieve system's time 

start_time = round(time.time())
  
# creating tkinter window 
root = Tk() 
root.title('Elapsed Time') 
  
# This function is used to  
# display time on the label 
def time_elapsed(): 
    string = round(time.time()) - start_time
    lbl.config(text = string) 
    lbl.after(1000, time_elapsed) 
  
# Styling the label widget so that clock 
# will look more attractive 
lbl = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'white', 
            foreground = 'black') 
  
# Placing clock at the centre 
# of the tkinter window  
lbl.pack(anchor = 'center') 
time_elapsed()

mainloop()
