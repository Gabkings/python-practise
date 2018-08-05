from tkinter import *
from tkinter import ttk 

window = Tk()

frame = ttk.Frame(window)
frame.pack()
frame.config(height=300,width = 300,relief=RIDGE, padding=(100,100))
ttk.Button(frame,text='hi').pack()

window.mainloop()
