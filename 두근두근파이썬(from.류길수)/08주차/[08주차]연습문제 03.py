def f():
    for i in range(150):
        t.goto(i, (i**2+1)/100)


import turtle
t = turtle.Turtle()
t.shape("turtle")

t.forward(300)
t.forward(-300)
t.left(90)

t.forward(300)
t.forward(-300)
t.right(90)

f()
