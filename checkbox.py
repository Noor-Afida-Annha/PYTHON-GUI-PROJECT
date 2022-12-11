from tkinter import *

def check():
    print(chbkx1.get(),chbkx2.get(),chbkx3.get(),chbkx4.get())

root=Tk()
root.title('Checkbox')
root.geometry('300x300')


chbkx=[('Java',1),('Python',2),('PHP',3),('Ruby',4)]

chbkx1=IntVar()
Checkbutton(text='Java',variable=chbkx1).pack()
chbkx2=IntVar()
Checkbutton(text='Python',variable=chbkx2).pack()
chbkx3=IntVar()
Checkbutton(text='PHP',variable=chbkx3).pack()
chbkx4=IntVar()
Checkbutton(text='Ruby',variable=chbkx4).pack()

btn1=Button(text='Get Values',command=check).pack()
btn2=Button(text='Close',command=root.destroy).pack()
root.mainloop()