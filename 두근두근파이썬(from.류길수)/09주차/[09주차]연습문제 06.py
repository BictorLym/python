import turtle
import random

def draw_star(t, color, length, x, y):
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.forward(length)
        t.right(144)
    t.end_fill()


s = turtle.Screen()
s.bgcolor("black")
t = turtle.Turtle()
color = ["red", "orange", "yellow", "green", "blue", "violet"]
x = 0; y = 0; length = 0;
for c in color:
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    length = random.randint(10, 60)
    draw_star(t, c, length, x, y)

