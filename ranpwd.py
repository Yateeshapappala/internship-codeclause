import string
import random
from tkinter import *
from tkinter import messagebox

r=Tk()
r.title("Random Password Generator")
r.geometry("500x400")
paswd=StringVar()
leng=StringVar()
def generate():
    l=string.ascii_letters #lowercase and uppercase letters
    n=string.digits # numbers from 0 to 9
    c=string.punctuation #special charcters
    lengt=leng.get()
    if lengt and lengt!="":
            a=l+n+c
            password=""
            lengt=int(lengt)
            for i in range(lengt):
                password+=''.join(random.choice(a))
            paswd.set(password)
    else:
        messagebox.showwarning("Invalid input","Please enter length to generate the password")
def resetpwd():
     leng.set("")
     paswd.set("")  

def acceptpwd():
     ans=paswd.get()
     if ans != "" and ans!="Invalid input":
          r.destroy()
     else:
        messagebox.showwarning("Invalid Input","Please generate the password first")

def validate_input(input):
    if input.isdigit():
        return True
    elif input=="":
        return True
    else:
        messagebox.showwarning("Invalid Input","Please enter only numeric value")
        
        return False
    
validation=r.register(validate_input)

title=Label(r,text="Random Password Generator",fg="Black",font=("Aerial 15 bold",20))
title.grid(row=0,column=0,columnspan=2)

pwdlen=Label(r,text="Length of Password",font=("Arial",15))
pwdlen.grid(row=1,column=0,pady=10)

length=Entry(r,textvariable=leng,validate="key",validatecommand=(validation,"%P"),font=("Arial",15),relief="ridge",borderwidth='2')
length.grid(row=1,column=1,padx=10)

genpwd=Label(r,text="Generated Password",font=("Arial",15))
genpwd.grid(row=2,column=0,pady=10)

pwd=Entry(r,text=paswd,relief="solid",font=("Arial",15))
pwd.grid(row=2,column=1,padx=10)

gener=Button(r,text="Generate Password",command=generate,font=("Arial",15),activebackground="green")
gener.grid(row=3,column=1,pady=10)

accept=Button(r,text="Accept",command=acceptpwd,font=("Arial",15),activebackground="green")
accept.grid(row=3,column=0,sticky=W,padx=10)

reset=Button(r,text="Reset",command=resetpwd,font=("Arial",15),activebackground="green")
reset.grid(row=3,column=0,sticky=E)

r.mainloop()
