from tkinter import *

def btn(numbers):
    global operator
    operator=operator+str(numbers)
    txt_input.set(operator)

def clear():
    global operator
    operator=''
    txt_input.set('')

def equal():
    global operator
    sumall=float(eval(operator))
    txt_input.set(sumall)
    operator=''


root=Tk()
root.title('Calculator')

operator=''
txt_input=StringVar('')


#-------------Screen-------
Display=Entry(root,font=('times',30,'bold'),fg='white',bg='#463F40',justify='right',bd=50,textvariable=txt_input)
Display.grid(columnspan=4)

#----------row1-------------

btn7= Button(root,padx=32,pady=15,font=('times',25,'bold'),fg='black',text=7,bd=8,command=lambda:btn(7)).grid(row=1,column=0)
btn8= Button(root,padx=32,pady=15,font=('times',25,'bold'),fg='black',text=8,bd=8,command=lambda:btn(8)).grid(row=1,column=1)
btn9= Button(root,padx=32,pady=15,font=('times',25,'bold'),fg='black',text=9,bd=8,command=lambda:btn(9)).grid(row=1,column=2)
btnc= Button(root,padx=29,pady=15,font=('times',25,'bold'),fg='black',text='C',bd=8,bg='#53C16C',command=clear).grid(row=1,column=3)
#----------row2-------------

btn4= Button(root,padx=32,pady=15,font=('times',25,'bold'),fg='black',text=4,bd=8,command=lambda:btn(4)).grid(row=2,column=0)
btn5= Button(root,padx=32,pady=15,font=('times',25,'bold'),fg='black',text=5,bd=8,command=lambda:btn(5)).grid(row=2,column=1)
btn6= Button(root,padx=32,pady=15,font=('times',25,'bold'),fg='black',text=6,bd=8,command=lambda:btn(6)).grid(row=2,column=2)
btnplus= Button(root,padx=32,pady=15,font=('times',25,'bold'),fg='black',text='+',bd=8,bg='orange',command=lambda:btn('+')).grid(row=2,column=3)
#----------row3-------------

btn1= Button(root,padx=32,pady=15,font=('times',25,'bold'),fg='black',text=1,bd=8,command=lambda:btn(1)).grid(row=3,column=0)
btn2= Button(root,padx=32,pady=15,font=('times',25,'bold'),fg='black',text=2,bd=8,command=lambda:btn(2)).grid(row=3,column=1)
btn3= Button(root,padx=32,pady=15,font=('times',25,'bold'),fg='black',text=3,bd=8,command=lambda:btn(3)).grid(row=3,column=2)
btnminus= Button(root,padx=35,pady=15,font=('times',25,'bold'),fg='black',text='-',bd=8,bg='orange',command=lambda:btn('-')).grid(row=3,column=3)
#----------row4-------------

btn0= Button(root,padx=30,pady=15,font=('times',25,'bold'),fg='black',text=0,bd=8,command=lambda:btn(0)).grid(row=4,column=0)
btndot= Button(root,padx=37,pady=15,font=('times',25,'bold'),fg='black',text='.',bg='orange',bd=8,command=lambda:btn('.')).grid(row=4,column=1)
btn_div= Button(root,padx=35,pady=15,font=('times',25,'bold'),fg='black',text='/',bg='orange',bd=8,command=lambda:btn('/')).grid(row=4,column=2)
btn_mul= Button(root,padx=33,pady=15,font=('times',25,'bold'),fg='black',text='*',bg='orange',bd=8,command=lambda:btn('*')).grid(row=4,column=3)
#----------row5-------------

btn_equal= Button(root,padx=93,pady=15,font=('times',25,'bold'),fg='black',text='=',bg='#53C16C',bd=8,command=equal).grid(row=5,column=0,columnspan=2)
btn_open_bracket= Button(root,padx=35,pady=15,font=('times',25,'bold'),fg='black',text='(',bg='#66A0C1',bd=8,command=lambda:btn('(')).grid(row=5,column=2)
btn_close_bracket= Button(root,padx=36,pady=15,font=('times',25,'bold'),fg='black',text=')',bg='#66A0C1',bd=8,command=lambda:btn(')')).grid(row=5,column=3)


root.mainloop()