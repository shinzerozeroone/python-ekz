from tkinter import *

def populateList():
    print('Populate')

def addItem():
    print('Add')

def removeItem():
    print('Remove')

def updateItem():
    print('Update')

def clearText():
    print('Clear')

app = Tk()

app.title('just program')
app.geometry('700x300')

#Part
PartNameText = StringVar()
PartName = Label(app, text = 'Part Name', pady = 20)
PartEntry = Entry(app, textvariable = PartNameText)

PartName.grid(row = 0, column = 0, sticky = W)
PartEntry.grid(row = 0, column = 1)

#Customer
CustomerNameText = StringVar()
CustomerName = Label(app, text='Customer', pady=20)
CustomerEntry = Entry(app, textvariable = CustomerNameText)

CustomerName.grid(row = 0, column = 2, sticky = W)
CustomerEntry.grid(row = 0 , column = 3)

#Retailer
RetailerNameText = StringVar()
RetailerName = Label(app, text = 'Retailer', pady = 20)
RetailerEntry = Entry(app, textvariable = RetailerNameText)

RetailerName.grid(row = 1, column = 0, sticky = W)
RetailerEntry.grid(row = 1, column = 1)

#Price
PriceNameText = StringVar()
PriceName = Label(app, text = 'Price', pady = 20)
PriceEntry = Entry(app, textvariable = PriceNameText)

PriceName.grid(row = 1 , column = 2, sticky = W)
PriceEntry.grid(row = 1, column = 3)

#Partlist
PartList = Listbox(app, height = 8, width = 50, border = 0)
PartList.grid(row = 3, column = 0 , columnspan = 3 , rowspan = 6, pady = 20, padx = 20)

#ScrollBar
ScrollBar = Scrollbar(app)
ScrollBar.grid(row = 3, column = 3)

#ScrollBar to Partlist
PartList.configure(yscrollcommand= ScrollBar.set)
ScrollBar.configure(command=PartList.yview)

#Buttons
btn1 = Button(app, text = 'Add Part', width = 12, command= addItem)
btn1.grid(row = 2 , column = 0, pady = 20)

btn2 = Button(app, text = 'remove Part', width = 12, command= removeItem)
btn2.grid(row = 2 , column = 1)

btn3 = Button(app, text = 'Update Part', width = 12, command= updateItem)
btn3.grid(row = 2 , column = 2)

btn4 = Button(app, text = 'Clear Input', width = 12, command= clearText)
btn4.grid(row = 2 , column = 3)

#PopulateList
populateList()

app.mainloop()