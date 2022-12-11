from tkinter import *
import tkinter.messagebox

g = Tk()
g.title('Application')
g.geometry('444x444+500+200')
def fbtn1():
    txt = text.get()
    Label(text= txt, fg='white', bg='tomato').pack()
def fbtn2():
    Label(text='Save your project', fg='white', bg='skyblue').pack()
def gui():
    gu = Tk()
    gu.title('New Project')
    gu.mainloop()
def save():
    Label(text='Save your project', fg='white', bg='blue').pack()
def open():
     tkinter.messagebox.showinfo('Open','Do you want to open this file?')
def close():
     dn= tkinter.messagebox.askquestion('Delete','Do you want to close this file?')
     if dn == 'yes':
         g.destroy()


def delete():
    dn = tkinter.messagebox.askquestion('Delete', 'Do you want to delete this file?')
    if dn == 'yes':
        g.destroy()


text = StringVar()

label1 = Label(text='Name',fg= 'white', bg = 'black').pack()
label2 = Label(text='Age',fg= 'white', bg = 'purple').pack()
btn1 = Button(text='Submit project',fg='white',bg='green', command=fbtn1).pack()
my_text = Entry(textvariable = text).pack()
btn2 = Button(text='Save project',fg='white',bg='orange', command=fbtn2).pack()

menubar = Menu()
m_item_one = Menu()

m_item_one.add_command(label='New Project',command = gui)
m_item_one.add_command(label='Save',command= save)
m_item_one.add_command(label='Open',command = open)
m_item_one.add_command(label='Close',command = delete)

m_item_two = Menu()

m_item_two.add_command(label='Cut')
m_item_two.add_command(label='Copy')
m_item_two.add_command(label='Paste')
m_item_two.add_command(label='Delete',command = delete)


menubar.add_cascade(label='File',menu =m_item_one)
menubar.add_cascade(label='Edit',menu =m_item_two)
menubar.add_cascade(label='Run')
menubar.add_cascade(label='Code')
menubar.add_cascade(label='Tools')
menubar.add_cascade(label='Help')
g.config(menu = menubar)
g.mainloop()