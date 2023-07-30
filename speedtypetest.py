import random
import time
from  tkinter import *
from tkinter import messagebox
s=Tk()
s.title("Speed Type Test")
s.geometry("1000x1000")
typing=StringVar()
a=StringVar()
sentences=[
    "Keep calm and code on.",
    "Type fast, think faster.",
    "The quick brown fox jumps",
    "She sells seashells by herself",
    "Peter Piper picked a peck",
    "Time flies when you're busy",
    "Two wrongs don't make right",
    "A journey of a thousand miles",
]
start=time.time()
sentence=StringVar()
c=1
def star():
    sent.delete("0.1",END)
    typing.set("")
    global start
    global sentence
    type.config(state=NORMAL)

    sentence=random.choice(sentences)
    sent.insert(END,sentence)
    start=time.time()
    finish.config(state=NORMAL)


def enter(event):
    finish.invoke()


def test():
    global start
    global sentence
    global c
    end=time.time()

    timetaken=end-start
    ans=typing.get()
    wpm=(len(ans.split())/timetaken)*60
    correct=sum(1 for i,j in zip(ans,sentence) if i==j)
    accuracy=(correct/len(sentence))*100
    res.insert(END,"["+str(c)+"]\n")
    c=c+1
    res.insert(END,f"time taken {timetaken:.2f} seconds\n")
    res.insert(END,f"Words per minute: {wpm:.2f} WPM\n")
    res.insert(END,f"Accuracy: {accuracy:.2f}%\n")

    type.config(state="readonly")
    finish.config(state=DISABLED)

head=Label(s,text="Speed Type Test",font=("Ariel",20,"bold"))
head.pack(pady=10)

sent=Text(s,height=3,font=("Ariel",15))
sent.pack(pady=10)

space=Label(s,text="Type here",font=("Ariel",15))
space.pack(pady=10)

type=Entry(s,textvariable=typing,state="readonly",width=50,font=("Ariel",15))
type.pack(pady=10)

start=Button(s,text="Start",command=star,font=("Ariel",15))
start.pack(pady=10)

finish=Button(s,text="Finish",state=DISABLED,command=test,font=("Arial",15))
finish.pack(pady=10)
type.bind("<Return>",enter)

result=Label(s,text="Result",font=("Arial",15,"bold"))
result.pack(pady=10)

res=Text(s,relief="solid",font=("Ariel",15))
res.pack()

s.mainloop()