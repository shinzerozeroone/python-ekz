from tkinter import *

app = Tk()

app.title('ekz')
app.geometry('700x500')

def CheckPassword():
    e = password.get()
    a = 'password'
    if e == a:
        btn1['text'] == 'ok'
    else:
        btn1['text'] == 'try again'

txt1 = Text(app, width =21, height = 5)
txt1.pack()

def insertText():
    s = " da da da da da da da da"
    txt1.insert(1.0, s)

b_insert = Button(app, text="Вставить", command=insertText)
b_insert.pack()

lbl = Label(app, text = 'Введите пароль, чтобы продолжить')
lbl.pack()

password = Entry(app, width = 15)
password.pack()

btn1 = Button(app, text = 'Проерить пароль', width = 14, command = CheckPassword)
btn1.pack()

app.mainloop()