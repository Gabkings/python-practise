import tkinter as tk
from tkinter import ttk 
#create window
window = tk
alabel = ttk.Label(text='a Label')
alabel.grid(column=0,row=0)
def click_me():
    button.configure(text='i have clicked')
    alabel.configure(foreground='red')

button = ttk.Button(text='click me',command = click_me)
button.grid(column=1,row=1)
window.mainloop()