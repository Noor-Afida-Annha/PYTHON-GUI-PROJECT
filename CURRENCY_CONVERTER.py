from tkinter import *
from tkinter import ttk

def converter():
    v2=indicator.get()
    v3=v1.get()
    if v2 == 'Argentina':
        e3.delete(0,END)
        v4=((v3*69.60),'peso')
        e3.insert(0,v4)
    elif v2 == 'Bangladesh':
        e3.delete(0,END)
        v4=((v3*84.91),'Taka')
        e3.insert(0,v4)
    elif v2 == 'China':
        e3.delete(0,END)
        v4=((v3*7.08),'Yuan')
        e3.insert(0,v4)
    elif v2 == 'Danish':
        e3.delete(0,END)
        v4=((v3*6.63),'Krone')
        e3.insert(0,v4)
    elif v2 == 'Egypt':
        e3.delete(0,END)
        v4=((v3*16.21),'Pound')
        e3.insert(0,v4)
    elif v2 == 'France':
        e3.delete(0,END)
        v4=((v3*0.89),'Euro')
        e3.insert(0,v4)
    elif v2 == 'Ghana':
        e3.delete(0,END)
        v4=((v3*5.80),'Cedi')
        e3.insert(0,v4)
    elif v2 == 'Hong Kong':
        e3.delete(0,END)
        v4=((v3*7.75),'Dollar')
        e3.insert(0,v4)
    elif v2 == 'Iran':
        e3.delete(0,END)
        v4=((v3*42105.00),'Rial')
        e3.insert(0,v4)
    elif v2 == 'Japan':
        e3.delete(0,END)
        v4=((v3*106.97),'Yen')
        e3.insert(0,v4)
    else:
        e3.delete(0,END)
        v4=('Error: Please choose a country')
        e3.insert(0,v4)

def clear():
    e1.delete(0,END)
    e3.delete(0, END)

root = Tk()
root.title('Currency Converter')
root.geometry('450x250+700+200')

v1=IntVar()
indicator=StringVar(value='Choose a country')

Label(text='Currency Converter',font=('times',20,'bold')).grid(row=0,column=1)
Label(text='Amount($)',padx=10,pady=5,font=('times',20,'bold')).grid(row=1,sticky=W)
e1=Entry(width=20,font=('times',20,'bold'),textvariable=v1)
e1.grid(row=1,column=1)

Label(text='Country',padx=10,pady=5,font=('times',20,'bold')).grid(row=2,sticky=W)
e2=ttk.Combobox(width=19, font=('times',20,'bold'), textvariable=indicator)
e2['values']=('Argentina','Bangladesh','China','Danish','Egypt','France','Ghana','Hong Kong','Iran','Japan')
e2.grid(row=2,column=1)

Label(text='Total',padx=10,pady=5,font=('times',20,'bold')).grid(row=3,sticky=W)
e3=Entry(width=20,font=('times',20,'bold'))
e3.grid(row=3,column=1)

bt1=Button(text='Convert',font=('times',20,'bold'),bg='#46CA56',command=converter).grid(row=4,column=1,sticky=W)
bt2=Button(text='Clear',font=('times',20,'bold'),bg='#EE213D',command=clear).grid(row=4,column=1,sticky=E)

root.mainloop()
