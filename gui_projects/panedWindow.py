from tkinter import *
from tkinter import ttk 

window = Tk()
panedWindow = ttk.PanedWindow(window,orient = HORIZONTAL)
panedWindow.pack(fill=BOTH,expand=True)
frame = ttk.Frame(panedWindow,width=50,height=100,relief=RIDGE)
panedWindow.add(frame,weight=10)
frame2 = ttk.Frame(panedWindow,width=80,height=100,relief=RIDGE)
panedWindow.add(frame2,weight=15)
window.mainloop()