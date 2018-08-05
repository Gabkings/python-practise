from tkinter import *
from tkinter import ttk 

window = Tk()
month = StringVar()
combox = ttk.Combobox(window,textvariable = month)
combox.pack()
combox.config(values = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
combox.set('---')
print(month.get())
year = StringVar()
Spinbox(window, from_ = 1990, to = 2030 ,textvariable=year).pack()



window.mainloop()