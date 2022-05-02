import turtle
import random

t=turtle.Turtle()
t.shape("turtle")
color = ["yellow", "red", "purple", "blue"]

def draw_square(x, y, c):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black", c)
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.end_fill()

for c in color:
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    draw_square(x, y, c)


