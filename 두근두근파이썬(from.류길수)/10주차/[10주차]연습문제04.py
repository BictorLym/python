from tkinter import *

def translation():
    inch = int(e2.get())
    centi = inch * 2.54
    l4.configure(text = str(centi) + " 센티미터")

window = Tk()

l1 = Label(window, text="인치를 센티미터롤 변환하는 프로그램:")
l1.grid(row = 0, column = 0, columnspan = 2)

l2 = Label(window, text="인치를 입력하시오:")
l2.grid(row = 1, column = 0)
e2 = Entry(window)
e2.grid(row = 1, column = 1)

l3 = Label(window, text="변환결과:")
l3.grid(row = 2, column = 0)
l4 = Label(window, text="결과값이 아직 없습니다.")
l4.grid(row=2, column = 1)

b5 = Button(window, text="변환!", command=translation)
b5.grid(row=3, column = 1)


