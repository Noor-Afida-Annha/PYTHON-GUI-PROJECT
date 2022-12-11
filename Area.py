from tkinter import *

def calculate():
    var2=var1.get()
    var3=3.1416*var2*var2
    en2.insert(0,var3)

def clear():
   en1.delete(0,END)
   en2.delete(0,END)


root=Tk()
root.title('Area of Circle')
root.geometry('500x200')

var1=IntVar()
Label(text='Radius',padx=10,pady=5,font=('times',20,'bold')).grid(row=0)
en1=Entry(width=20,font=('times',20,'bold'),textvariable=var1)
en1.grid(row=0,column=1)
Label(text='Area',padx=10,pady=5,font=('times',20,'bold')).grid(row=1)
en2=Entry(width=20,font=('times',20,'bold'))
en2.grid(row=1,column=1)

btn1=Button(text='Calculate',font=('times',20,'bold'),bg='#46CA56',command=calculate).grid(row=2,column=1,sticky=W)
btn2=Button(text='Clear',font=('times',20,'bold'),bg='#EE213D',command=clear).grid(row=2,column=1,sticky=E)
root.mainloop()

def cal():
    v3=v1.get()
    v4=v2.get()
    v5=v3*v4
    e3.insert(0,v5)

def clr():
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)

root1 = Tk()
root1.title('Area of Rectangle')
root1.geometry('500x300')

Label(text='Area of rectangle',font=('times',20,'bold')).grid(row=0,column=1)

v1=IntVar()
Label(text='length',padx=10,pady=5,font=('times',20,'bold')).grid(row=1)
e1=Entry(width=20,font=('times',20,'bold'),textvariable=v1)
e1.grid(row=1,column=1)

v2=IntVar()
Label(text='width',padx=10,pady=5,font=('times',20,'bold')).grid(row=2)
e2=Entry(width=20,font=('times',20,'bold'),textvariable=v2)
e2.grid(row=2,column=1)

Label(text='Area',padx=10,pady=5,font=('times',20,'bold')).grid(row=3)
e3=Entry(width=20,font=('times',20,'bold'))
e3.grid(row=3,column=1)

bt1=Button(text='Calculate',font=('times',20,'bold'),command=cal).grid(row=4,column=1,sticky=W)
bt2=Button(text='Clear',font=('times',20,'bold'),command=clr).grid(row=4,column=1,sticky=E)
root1.mainloop()

def calc():
    vr3=vr1.get()
    vr4=vr2.get()
    vr5=(vr3*vr4)/2
    entr3.insert(0,vr5)

def cl():
    entr1.delete(0,END)
    entr2.delete(0, END)
    entr3.delete(0, END)

root2 = Tk()
root2.title('Area of Rectangle')
root2.geometry('500x300')

Label(text='Area of triangle',font=('times',20,'bold')).grid(row=0,column=1)

vr1=IntVar()
Label(text='base',padx=10,pady=5,font=('times',20,'bold')).grid(row=1)
entr1=Entry(width=20,font=('times',20,'bold'),textvariable=vr1)
entr1.grid(row=1,column=1)

vr2=IntVar()
Label(text='height',padx=10,pady=5,font=('times',20,'bold')).grid(row=2)
entr2=Entry(width=20,font=('times',20,'bold'),textvariable=vr2)
entr2.grid(row=2,column=1)

Label(text='Area',padx=10,pady=5,font=('times',20,'bold')).grid(row=3)
entr3=Entry(width=20,font=('times',20,'bold'))
entr3.grid(row=3,column=1)

butn1=Button(text='Calculate',font=('times',20,'bold'),command=calc).grid(row=4,column=1,sticky=W)
butn2=Button(text='Clear',font=('times',20,'bold'),command=cl ).grid(row=4,column=1,sticky=E)
root2.mainloop()
