from tkinter import *
from tkinter import ttk 
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass    
window = Tk()
window.geometry('400x500')
feet = StringVar()
meters = StringVar()
feet_entry = ttk.Entry(window,width=20,textvariable = feet)
feet_entry.grid(column = 2,row = 1)
ttk.Button(window,text='Calculate',command = calculate).grid(column = 2, row = 3)
ttk.Label(window,text='Feet:').grid(column = 1,row = 2)

ttk.Label(window,text='Equivalent to').grid(column = 2,row = 2)
ttk.Label(window,text='Feet:', textvariable= meters).grid(column = 3,row = 2)
ttk.Label(window,text='Metres:').grid(column = 4,row = 2)
for child in window.winfo_children(): child.grid_configure(padx= 10, pady = 10)
    
window.mainloop()