from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont

root = Tk()
root.config(bg = '#000000')

root.title("Page1")

root.geometry("500x500")

#helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')

#icon attempt
#root.iconbitmap("Raiders.ico")

#introLabel
LabelIntro = Label(root, text = "Welcome to Memory Glass!", fg = '#DAEA14' , font=("Brush Script MT", 25), bg = '#000000' )
LabelIntro.grid(row = 0, column = 20 )


#Label to create space for the buttons
labelSpace = Label(root, text = "\n\n\n\n\n                                           ", bg = '#000000', fg = "#000000" )
labelSpace.grid(row = 10, column = 10 )

#Label to create space between the two buttons
labelSpace2 = Label(root, text = "\n\n\n\n\n", bg = '#000000', fg = "#000000" )
labelSpace2.grid(row = 25, column = 20 )

# Action Function for loginButton
def my_click():
    my_label = Label(root, text = "login procedure", fg = '#26EA30' , font=("American Typewriter", 12), bg = '#000000')
    #my_label.pack()
    my_label.grid(row = 20, column = 22)
    
def my_click2():
    my_label = Label(root, text = "Sign-up Procedure", fg = '#014F05', font=("American Typewriter", 12) , bg = '#000000') 
    #my_label.pack()
    my_label.grid(row = 30, column = 22)


#labelL = Label(root, text = "login", font=("American Typewriter", 19) ) 

#use ttk.Button
loginbutton = ttk.Button(root, text = "login", command = my_click)
#loginbutton['font'] = helv36
loginbutton.grid(row = 20, column = 20)


#labelS = Label(root, text = "Sign-up", font=("Luminari", 19) ) 
signUpButton= ttk.Button(root, text = "Sign-Up", command = my_click2)
signUpButton.grid(row = 30, column = 20)
#mybutton.pack()





root.mainloop()
