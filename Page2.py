from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont
#import tkinter as tk



root = Tk()
root.config(bg = '#000000')
root.title("Page2")

root.geometry("500x500")

username = 'Fish=Trash'
password = '12341'

#introLabel
LabelIntro = Label(root, text = "Login: ", fg = '#DAEA14' , font=("Brush Script MT", 25), bg = '#000000')
LabelIntro.grid(row = 0, column = 0 )


#Label to create space for the buttons
labelSpace = Label(root, text = "\n\n\n                               ", bg = '#000000', fg = "#000000")
labelSpace.grid(row = 10, column = 0 )



boxLabel = Label(root, text = "Username/email", fg = '#DAEA14' , font=("American Typewriter", 12), bg = '#000000')
boxLabel.grid(row = 13, column = 20)

entryBox1 = Entry(root, width = 18, fg = 'blue') #use .get() method to retirieve text
entryBox1.grid(row = 15, column = 20 )

boxLabel2 = Label(root, text = "Password", fg = '#DAEA14' , font=("American Typewriter", 12), bg = '#000000')
boxLabel2.grid(row = 18, column = 20)

entryBox2 = Entry(root, width = 18, fg = 'blue') #use .get() method to retirieve text
entryBox2.grid(row = 21, column = 20 )

def clicked1():
    returnLabel = Label(root, bg = '#000000')
    if(entryBox1.get() == username and entryBox2.get() == password):
        returnLabel.config(text = 'Username & password match! Welcome: ' + entryBox1.get(), fg = '#26B506', font=("American Typewriter", 12))
    else:
        returnLabel.config(text = 'Username or password ' + 'is invalid.', fg = '#B52806', font=("American Typewriter", 12))
    returnLabel.pack()
    
def clicked2():
    backLabel = Label(root, text = 'You will be sent back to the home page', fg = '#DAEA14', bg = '#000000',  font=("American Typewriter", 12))
    backLabel.pack()
    
labelSpace = Label(root, text = "\n\n\n         ", bg = '#000000', fg = "#000000")
labelSpace.grid(row = 22, column = 25 )

myButton = ttk.Button(root, text = "→", command = clicked1 )
myButton.grid(row = 30, column = 30 )

labelSpace = Label(root, text = "\n\n", bg = '#000000', fg = "#000000")
labelSpace.grid(row = 34, column = 25 )

myButton2 = ttk.Button(root, text = "Back", command = clicked2 )
myButton2.grid(row = 40, column = 0 )

root.mainloop()

