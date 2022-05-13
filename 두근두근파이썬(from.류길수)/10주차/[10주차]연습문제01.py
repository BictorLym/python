from tkinter import *

window = Tk()

l1=Label(window, text="간단한 GUI프로그램!")
l1.pack()

b1 = Button(window, text="환영합니다.")
b1.pack()
b2 = Button(window, text="종료")
b2.pack()

window.mainloop()
