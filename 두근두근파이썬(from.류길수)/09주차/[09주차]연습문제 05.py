import turtle
import random

def draw_shape(t, c, length, sides, x, y):
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black", c)
    t.begin_fill()
    for i in range(sides):
        t.forward(length)
        t.left(360/sides)
    t.end_fill()



t = turtle.Turtle()
color = ["orange", "blue", "green", "yellow", "white"]
length = 0
sides = 0
x = 0; y=0;
for c in color:
    sides = random.randint(4, 8)
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    length = random.randint(10, 30)
    draw_shape(t, c, length, sides, x, y)
