from tkinter import *
from tkinter.ttk import *
import calendar
 
# creates a Tk() object
# sets the geometry of main
# root window
root = Tk()
root.title("Pick a date")
root.geometry("240x240")
root.resizable(0,0)

#Lables on calendar
lable1 = Label(root,text="Month",font=('arial',12,'bold')).place(x=9,y=0)

lable2 = Label(root,text="Year",font=('arial',12,'bold')).place(x=109,y=0)

#create spinbox
spin1 = Spinbox(root,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4)
spin1.place(x=60,y=0)

spin2 = Spinbox(root,from_=1999,to= 2100,width=4)
spin2.place(x=150,y=0)



 
# function to open a new window
# on a button click
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Calendar")
 
    # sets the geometry of toplevel
    newWindow.geometry("240x150")
    a = int(spin1.get())
    b = int(spin2.get())
    cal = calendar.month(b,a)
    txt = Text(newWindow,width=240,height=8)
    txt.delete(0.0,END)
    txt.insert(INSERT, cal)
    txt.place(x=0,y=0)
    root.mainloop()

    btn2 = Button(root,text = "Exit", command = None).place(x=85,y=30)


    
    
    
 
 

 
# a button widget which will open a
# new window on button click
btn = Button(root,text ="show",command = openNewWindow).place(x=85,y=30)

 



