import tkinter as tk 
from tkinter import ttk 

window = tk.Tk()
color1 = 'blue'
color2 = 'gold'
color3 = 'red'

def change_back():
    b = redVar.get()
    if b == 1: window.configure(bg = color1)
    elif b == 2: window.configure(bg = color2)
    elif b == 3: window.configure(bg = color3)




redVar = tk.IntVar()
rad1 = tk.Radiobutton(window, text ='rad1',command=change_back,variabl= redVar, value=1)
rad2 = tk.Radiobutton(window, text ='rad2',command=change_back,variabl= redVar, value=2)  
rad3 = tk.Radiobutton(window, text ='rad3',command=change_back,variabl= redVar, value=3)
rad1.grid(column = 0,row= 0) 
rad2.grid(column = 0,row= 1)
rad3.grid(column = 0,row= 2)  
window.mainloop()     