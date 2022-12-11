from tkinter import *
from tkinter.colorchooser import *



root = Tk()
root.title('Color Chooser')
root.geometry('250x250+650+250')

def my_color():
    color = askcolor()
    label = Label(text='This is your preferred color', fg='white',bg=color[1]).pack()


btn=Button(text='Color Choose',bg='black',fg='white',command=my_color).pack()
root.mainloop()