from tkinter import *
import re

app = Tk()
app.title('exam python. FIRST GOAL')
app.geometry('300x200')

clicks = 0
a = 0
vocabulary = ['a', 'e', 'u', 'i', 'o']

def Dynamic():
    global clicks
    global a
    m = ["a", "e"]
    btn1['text'] = str(clicks) + ' ' + m[a]
    clicks += 1
    a +=1

    if a == 2:
        a = 0

btn1 = Button(app, text = 'Button', width = 12, height = 5, command = Dynamic)
btn1.pack()

def toMain():
    app.destroy()
    import main

btn2 = Button(app, text = 'Назад', width = 12 , height =5, command = toMain)
btn2.pack()

app.mainloop()