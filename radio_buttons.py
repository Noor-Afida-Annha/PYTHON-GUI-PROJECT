from tkinter import *

root=Tk()

def programming():
    r=v.get()
    if r ==1:
         label1=Label (text=' You select C programming language ',fg='white',bg='blue').pack()
    elif r == 2:
       label2=Label (text=' You select C++ programming language ',fg='white',bg='tomato').pack()
    elif r == 3:
        label3=Label (text=' You select C# programming language ',fg='white',bg='green').pack()
    elif r == 4:
        label4 = Label(text=' You select PHP programming language ',fg='white',bg='gray').pack()
    elif r == 5:
        label5 = Label(text=' You select Python programming language ',fg='white',bg='red').pack()
    elif r == 6:
        label6=Label (text=' You select Java programming language ',fg='black',bg='yellow').pack()
    elif r == 7:
        label7 = Label(text=' You select Swift programming language ',fg='black',bg='skyblue').pack()
    else:
        label8 = Label(text=' You select Ruby programming language ',fg='black',bg='orange').pack()



root.geometry('400x400')
root.title('Radio Buttons')
v=IntVar()

Radios=[('C',1),('C++',2),('C#',3),('PHP',4),('Python',5),('Java',6),('Swift',7),('Ruby',8)]
mylabel=Label(text='Computer Programming').pack()

for rad,val in Radios:
    Radiobutton(text=rad,padx=10,variable=v,value=val,indicatoron=0,width=20,bg='#2C3E50',fg='#1ADAD4',command=programming).pack(anchor=W)
root.mainloop()