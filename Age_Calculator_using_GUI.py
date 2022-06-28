from calendar import c
from tkinter import *
from datetime import date
import tkinter.messagebox
root = Tk()
root.geometry("500x300")
root.configure(bg='#ADD8E6') 
root.title("Age Calculator")

def calculate():
    y = int(year.get())
    m = int(month.get())
    d = int(day.get())
    today = date.today()
    age = today.year - y - ((today.month ,today.day) < (m ,d))
    tkinter.messagebox.showinfo("HOW OLD YOU ARE?","You are " +str(age)+ " years old" )

label = Label(text="HOW OLD YOU ARE?",fg="BLUE",bg='#ADD8E6',font=("Helvetica",13,"bold"))
label.place(x=150,y=15)

label1 = Label(text="Enter your birth year",fg="red",bg='#ADD8E6',font=("Helvetica",13,"bold"))
label1.place(x=100,y=70)

label2 = Label(text="Enter your birth month",fg="red",bg='#ADD8E6',font=("Helvetica",13,"bold"))
label2.place(x=100,y=95)

label3 = Label(text="Enter your birth day date",fg="red",bg='#ADD8E6',font=("Helvetica",13,"bold"))
label3.place(x=100,y=120)



year = Entry(root,width=20)
month = Entry(root,width=20)
day = Entry(root, width= 20)

year.place(x=320,y=70)
month.place(x=320,y=95)
day.place(x=320,y=120)

Button(text="Calculte age",command = calculate,bg="black",fg="white",font=("Helvetica",13,"bold")).place(x=100,y=170)
Button(text="Exit",command=exit,bg="black",fg="white",font=("Helvetica",13,"bold")).place(x=300,y=170)
root.mainloop()