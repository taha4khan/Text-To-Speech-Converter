#import tkinter as tk
from tkinter import*

import pyttsx3

root = Tk()
root.title("text to speech project")
root.geometry("800x500")
#root.iconbitmap('c:/gui/codemy.ico')



title=Label(root,text='TEXT TO SPEECH',font=('times','30','bold italic'),bg='burlywood',fg='blue',activebackground='pink')
title.pack(pady=10)

def talk():
    engine = pyttsx3.init()
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0,END)

my_entry = Entry(root,font=("Helvatica",28))
my_entry.pack(pady=60)

my_button=Button(root, text="speak",command=talk)
my_button.configure(bg='purple',fg='white',activebackground='powder blue')
my_button.pack(pady=20)


btn2=Button(root,text="     Exit     ",font=('chiller','18','bold underline'),command=root.destroy)
btn2.configure(bg='green',fg='white',activebackground='pink')
btn2.place(x=50,y=400)




root.mainloop()
