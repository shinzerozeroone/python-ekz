from tkinter import *
import re

app = Tk()

app.title('ekz')
app.geometry('700x1000')

clicks = 0
q = 0
vocabulary = ['a', 'e', 'u', 'i', 'o']
password = 'password'

def chek():
    if ent.get() == password:
        txt2.delete(1.0 , END)
        txt2.insert(INSERT, 'И до сих пор я не придумал')
    else:
        txt2.delete(1.0, END)
        txt2.insert(INSERT, ' password is wrong , try again')

def Dynamic():
    global clicks
    global q
    arrr = ["a", "e"]
    btn1['text'] = str(clicks) + ' ' + arrr[q]
    clicks += 1
    q +=1

    if q == 2:
        q = 0

btn1 = Button(app, text = 'Button', width = 12, height = 5, command = Dynamic)
btn1.pack()

l1 = Label(app, width = 12, text = '1st lable')
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

l3 = Label(app, width = 20, text = 'checkbuttons')
l3.pack()

f = open('file.txt')
s = f.read().splitlines()
let = s[1]

letter1 = let[0]
letter2 = let[1]
letter3 = let[2]
letter4 = let[3]
letter5 = let[4]
letter6 = let[5]
letter7 = let[6]
letter8 = let[7]
letter9 = let[8]


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
def let5():
    text.insert(INSERT, letter6)
def let6():
    text.insert(INSERT, letter7)
def let7():
    text.insert(INSERT, letter8)
def let8():
    text.insert(INSERT, letter9)

check0 = Checkbutton(text = letter1, command = let0)
check1 = Checkbutton(text = letter2, command = let1)
check2 = Checkbutton(text = letter3, command = let2)
check3 = Checkbutton(text = letter4, command = let3)
check4 = Checkbutton(text = letter5, command = let4)
check5 = Checkbutton(text = letter6, command = let5)
check6 = Checkbutton(text = letter7, command = let6)
check7 = Checkbutton(text = letter8, command = let7)
check8 = Checkbutton(text = letter9, command = let8)

check0.pack()
check1.pack()
check2.pack()
check3.pack()
check4.pack()
check5.pack()
check6.pack()
check7.pack()
check8.pack()

text = Text(width=25, height=5)
text.pack()

l4 = Label(app, text = 'Radiobutton')
l4.pack()

def forRadio():
    l4['text'] = 'Австралийский Союз , Австрия, Азербайджан'

r = Radiobutton(app, text ='Названия стран', value = 0, command = forRadio)
r.pack()


app.mainloop()