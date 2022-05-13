from tkinter import*

def process():
    print("Hello World!")

window = Tk()
button = Button(window, text="클릭하지마세요", command=process)
button.pack()

window.mainloop()
