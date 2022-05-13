from tkinter import *

tot = 0

def add():
    global tot
    tot+=int(e1.get())
    display()

def sub():
    global tot
    tot-=int(e1.get())
    display()

def init():
    global tot
    tot = 100
    display()

def display():
    global l2
    l2.destroy()
    l2 = Label(window, text=str(tot))
    l2.grid(row=0, column=1)
    

window = Tk()

l1=Label(window, text="현재합계:")
l1.grid(row=0, column=0)
l2=Label(window, text=str(tot))
l2.grid(row=0, column=1)

e1 = Entry(window)
e1.grid(row=1, column=0, columnspan=3)

b1 = Button(window, text="더하기(+)", command=add)
b1.grid(row=2, column=0)
b2 = Button(window, text="빼기(-)", command=sub)
b2.grid(row=2, column=1)
b3 = Button(window, text="초기화", command=init)
b3.grid(row=2,column=2)

window.mainloop()

