def draw_line():
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(360/12)

import turtle
t = turtle.Turtle()
t.shape("turtle")
for i in range(12):
    draw_line()
    
