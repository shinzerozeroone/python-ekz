from tkinter import *
import re

app = Tk()

app.title('exam python. MAIN')
app.geometry('300x200')

def goal1():
    app.destroy()
    import goal1

def goal2():
    app.destroy()
    import goal2

def goal3():
    app.destroy()
    import goal3

def goal4():
    app.destroy()
    import goal4

f = open('info.txt')
l = f.read().splitlines()
text = Text(width=30, height=4)
text.insert(INSERT, l[0] + "\n" + l[1] +  "\n" + l[2])
text.pack()

btn1 = Button(app, text="1", command = goal1)
btn2 = Button(app, text="2", command = goal2)
btn3 = Button(app, text="3", command = goal3)
btn4 = Button(app, text="4", command = goal4)
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

app.mainloop()