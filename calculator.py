from tkinter import *
from math import sqrt,factorial

c=Tk()
c.title("Calculator")
c.geometry("250x250")
exp=""
string=StringVar()

def expression(num):
    global exp
    if num == "sq":
        if exp:
            try:
                result = sqrt(float(exp))
                exp = str(result)
                string.set(exp)
            except ValueError:
                string.set("Invalid input")
        else:
         string.set("Invalid input")
    if num=="!":
        if exp:
            try:
                result=factorial(int(exp))
                exp=str(result)
                string.set(exp)
            except ValueError:
                string.set("Invalid input")
    else:
        exp = exp + str(num)
        string.set(exp)


def clear():
    global exp
    exp=""
    string.set(exp)


def bac():
    global exp
    exp=exp[:-1]
    string.set(exp)


def equal():
    global exp
    if exp:
        try:
            ans=eval(exp)
            exp=str(ans)
            string.set(ans)
        except:
            string.set("Invalid input")    

sho=Entry(c,text=string,width="12",font=("Arial",15))
sho.grid(row=0,columnspan=4)

cle=Button(c,text="C",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:clear())
cle.grid(row=1,column=0)

sqrtt=Button(c,text="\u221A",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression("sq"))
sqrtt.grid(row=1,column=1)

div=Button(c,text="/",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression("/"))
div.grid(row=1,column=2)

back=Button(c,text="<-",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:bac())
back.grid(row=1,column=3)

sev=Button(c,text="7",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression(7))
sev.grid(row=2,column=0)

eig=Button(c,text="8",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression(8))
eig.grid(row=2,column=1)

nine=Button(c,text="9",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression(9))
nine.grid(row=2,column=2)

multi=Button(c,text="*",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression("*"))
multi.grid(row=2,column=3)

four=Button(c,text="4",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression(4))
four.grid(row=3,column=0)

fiv=Button(c,text="5",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression(5))
fiv.grid(row=3,column=1)

six=Button(c,text="6",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression(6))
six.grid(row=3,column=2)

sub=Button(c,text="-",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression("-"))
sub.grid(row=3,column=3)

one=Button(c,text="1",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression(1))
one.grid(row=4,column=0)

two=Button(c,text="2",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression(2))
two.grid(row=4,column=1)

three=Button(c,text="3",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression(3))
three.grid(row=4,column=2)

plus=Button(c,text="+",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression("+"))
plus.grid(row=4,column=3)

noteq=Button(c,text="!",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression("!"))
noteq.grid(row=5,column=0)

zero=Button(c,text="0",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression(0))
zero.grid(row=5,column=1)

dot=Button(c,text=".",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:expression("."))
dot.grid(row=5,column=2)

eq=Button(c,text="=",activebackground="green",height="1",width="3",font=("Arial"),command=lambda:equal())
eq.grid(row=5,column=3)

c.mainloop()