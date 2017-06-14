from tkinter import *

#Open/Create a window
window=Tk()

#Function
def km_to_miles():
    print(e1_value.get())
    miles=float(e1_value.get())*1.6
    t1.insert(END, miles)

#Add a button
b1=Button(window,text='Execute', command=km_to_miles)
#can also use grid b1.pack()
b1.grid(row=0, column=0)

#Add an entry
#This value will depend on a user's input
e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

#Add a text widget
t1=Text(window, height=1, width=20)
t1.grid(row=0, column=2)

#Maintains the window staying open
window.mainloop()


#To check what you can do with stuff
#from tkinter import * then Button?
