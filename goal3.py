from tkinter import *
import re

app = Tk()
app.title('exam python. THIRD GOAL')
app.geometry('300x400')

l3 = Label(app, width = 20, text = 'checkbuttons')
l3.pack()

f = open('info.txt')
s = f.read().splitlines()
let = s[1]
letf = s[2]

letter1 = let[0] + let[1] + let[2]
letter2 = let[3] + let[4] + let[5]
letter3 = let[6] + let[7] + let[8]
letter4 = letf[0] + letf[1] + letf[2]
letter5 = letf[3] + letf[4] + letf[5] + letf[6]


def let0():
    text.insert(INSERT, letter1)
def let1():
    text.insert(INSERT, letter2)
def let2():
    text.insert(INSERT, letter3)
def let3():
    text.insert(INSERT, letter4)
def let4():
    text.insert(INSERT, letter5)


check0 = Checkbutton(text = letter1, command = let0)
check1 = Checkbutton(text = letter2, command = let1)
check2 = Checkbutton(text = letter3, command = let2)
check3 = Checkbutton(text = letter4, command = let3)
check4 = Checkbutton(text = letter5, command = let4)


check0.pack()
check1.pack()
check2.pack()
check3.pack()
check4.pack()

text = Text(width=25, height=5)
text.pack()

def toMain():
    app.destroy()
    import main

btn4 = Button(app, text = 'Назад', width = 12 , height =5, command = toMain)
btn4.pack()

app.mainloop()