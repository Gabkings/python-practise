from tkinter import *
from tkinter import ttk 
counter = 0
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text = str(counter))
        label.after(1000,count)
    count()

window = Tk()
window.title('Counter')
window.geometry('400x400')
label = ttk.Label(window,foreground='black')
label.pack()
counter_label(label)
button = ttk.Button(window,text='END',command=window.destroy,width = 30)
button.pack()
window.mainloop()