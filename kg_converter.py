from tkinter import *

#Open/Create a window
window=Tk()

#Function
def kg_to_other():
    t1.delete('1.0', END)
    t2.delete('1.0', END)
    t3.delete('1.0', END)

    print(input_value.get())
    grams=float(input_value.get())*1000
    pounds=float(input_value.get())*2.20462
    ounces=float(input_value.get())*35.274

    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)

#Add a label
l1=Label(window, height=1, width=10, text='Kg')
l1.grid(row=0, column=0)


#Add a button
b1=Button(window,text='Convert', command=kg_to_other)
#can also use grid b1.pack()
b1.grid(row=0, column=2)

#Add an entry
#This value will depend on a user's input
input_value=StringVar()
e1=Entry(window, textvariable=input_value)
e1.grid(row=0, column=1)

#Add a text widget
t1=Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2=Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3=Text(window, height=1, width=20)
t3.grid(row=1, column=2)

#Maintains the window staying open
window.mainloop()


#To check what you can do with stuff
#from tkinter import * then Button?
