from tkinter import *

app = Tk()

cons = "aeiou"
num_click = 0
num_con = 0

def first(word):
    global num_click
    global num_con
    num_click +=1
    fi.read()
    i = len(word)-1 if num_click == 1 else num_con

    while (i>=0) and (word[i].lower() not in cons):
        i -=1
    if word[i].lower() in cons:
        num_con = i - 1
        btn1['text'] = '{}:{}'.format(num_click, word[i])

fi = open('for exam.txt','r')
f = open('lorem.txt', 'r')

app.title('ekz')
app.geometry('700x500')

def ImportText():
    Text['text'] = f.read()

#Buttons
btn1 = Button(app, text = 'Dynamic Button' , width = 12)
btn1.pack(side = TOP)
btn1.bind('<Button-1>', first)

#ContinueButton
btn2 = Button(app, text ='continue', width= 20)
btn2.pack(side = TOP)


text = Text( height = 8, width = 50)
text.pack(side = TOP)

#Pass
Pass = Label(app, text = 'Password')
Pass.pack(side = TOP)

PassEntry = Entry(app, width = 12)
PassEntry.pack(side = TOP)

text2 = Text(height =8, width = 20)
text2.pack(side = TOP)

app.mainloop()