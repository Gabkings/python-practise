import tkinter as tk

window = tk.Tk()
window.geometry('400x400')

sl1 = tk.Scale(window, from_ = 10, to=100 )
sl1.set(12)
sl1.pack()

sl2 = tk.Scale(window, from_=15, to=100)
sl2.pack()

window.mainloop()