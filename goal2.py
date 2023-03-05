from tkinter import *
import re

app = Tk()
app.title('exam python. SECOND GOAL')
app.geometry('300x400')

a = 'password'

def chek():
    if ent.get() == a:
        txt2.delete(1.0 , END)
        txt2.insert(INSERT, 'И до сих пор я не придумал')
    else:
        txt2.delete(1.0, END)
        txt2.insert(INSERT, ' password is wrong , try again')

l1 = Label(app, width = 12, text = 'little message')
l1.pack()

txt1 = Text(app, height = 3, width = 15)
txt1.insert(INSERT, 'Если честно, то я не знаю, что написать')
txt1.pack()

l2 = Label(app, width = 20, text = 'write ur PASSWORD')
l2.pack()

ent = Entry(app, width = 50)
ent.pack()

btn2 = Button(app, text = 'Log in', width = 12, height = 5, command = chek )
btn2.pack()

txt2 = Text(app, height = 3, width = 20)
txt2.pack()

def toMain():
    app.destroy()
    import main

btn4 = Button(app, text = 'Назад', width = 12 , height =5, command = toMain)
btn4.pack()


app.mainloop()