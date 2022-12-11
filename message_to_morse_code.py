from tkinter import *


def convert():
    v1 = indicator.get()
    for message in v1:

        if message == 'A' or message == 'a':
            message = ' ._ '
            en2.insert(0, message)
        if message == 'B' or message == 'b':
            message = ' _... '
            en2.insert(0, message)
        if message == 'C' or message == 'c':
            message = ' _._. '
            en2.insert(0, message)




def clear():
    en1.delete(0, END)
    en2.delete(0, END)


root = Tk()
root.title("ALPH TO MORSE")
root.geometry('600x400')

indicator = StringVar()

Label(text='INPUT:', padx=10, pady=5, font=('Comic Sans MS', 15)).grid(row=0, sticky=W)
en1 = Entry(width=16, font=('Comic Sans MS', 20, 'italic', 'bold'), textvariable=indicator)

en1.grid(row=0, column=1)

Label(text='OUTPUT:', padx=10, pady=5, font=('Comic Sans MS', 15)).grid(row=2, sticky=W)
en2 = Entry(width=16, font=('Comic Sans MS', 20))

en2.grid(row=2, column=1)

Label().grid(row=3)
btn1 = Button(text='Convert', padx=10, font=('Comic Sans MS', 15), bg='#C3988E', command=convert).grid(row=4, column=1,
                                                                                                       sticky=W)
btn2 = Button(text='Clear', font=('Comic Sans MS', 15), bg='#74AEB4', command=clear).grid(row=4, column=1, sticky=E)
root.mainloop()
