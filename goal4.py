from tkinter import *
import re

app = Tk()
app.title('exam python. FOURTH GOAL')
app.geometry('300x200')

r_var = BooleanVar()
r_var.set(0)

l4 = Label(app, text = 'first country')
l4.pack()

l5 = Label(app, text = 'second country')
l5.pack()

l6 = Label(app, text = 'third country')
l6.pack()

def forRadio1():
    l4['text'] = 'Австралийский Союз'

def forRadio2():
    l5['text'] = 'Австрия'

def forRadio3():
    l6['text'] = 'Азербайджан'

r0 = Radiobutton(app, text ='click', variable=r_var, value = 1 , command = forRadio1)
r0.pack()

r1 = Radiobutton(app, text = 'click', variable=r_var, value = 2, command = forRadio2)
r1.pack()

r2 = Radiobutton(app, text = 'click', variable=r_var, value = 3, command = forRadio3)
r2.pack()

def toMain():
    app.destroy()
    import main

btn7 = Button(app, text = 'Назад', width = 12 , height =5, command = toMain)
btn7.pack()

app.mainloop()