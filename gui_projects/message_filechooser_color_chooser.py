from tkinter import messagebox

messagebox.showinfo(title='Messege', message='Hello from tkinter')
print(messagebox.askyesno(title='Open',message='Do you want to open'))

from tkinter import filedialog
filename = filedialog.askopenfile()
print(filename.name)

from tkinter import colorchooser
print(colorchooser.askcolor(initialcolor='#ffffff'))