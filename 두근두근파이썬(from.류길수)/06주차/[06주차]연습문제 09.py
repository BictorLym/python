import random
import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(10):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    r = random.randint(1, 100)

    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(r)


