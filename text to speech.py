import tkinter as tk
from tkinter import *
import pyttsx3

engine=pyttsx3.init()

def speaknow():
    engine.say(text.get())
    engine.runAndWait()
    engine.stop()

root=Tk()
text=StringVar()



obj=LabelFrame(root,text="Text to speech 1",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

lbl=Label(obj,text="Text",font=30)
lbl.pack(side=tk.LEFT,padx=5)

text=Entry(obj,textvariable=text,font=30,width=25,bd=5)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="Speak",font=20,bg="black",fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)


btn2=Button(text="     Exit     ",font=('Helvetica','18','bold underline'),command=root.destroy,)
#for styling the button as different
#btn2 = Button(root, text = 'Quit !',style = 'TButton',command = root.destroy)
btn2.configure(bg='red',fg='yellow',activebackground='yellow')
btn2.place(x=50,y=400)


root.title("Text to speech")
root.geometry("400x500")
#root.attributes("-fullscreen",True)

root.resizable(False,False)
root.mainloop()
