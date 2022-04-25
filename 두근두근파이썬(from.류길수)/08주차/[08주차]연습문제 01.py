import turtle
import random

def draw_snowman(x, y):
    t = turtle.Turtle()
    s = turtle.Screen()
    t.shape("turtle")
    t.color("black", "white")
    s.bgcolor('skyblue')
    #최상단
    t.up()
    t.goto(x,y+200)
    t.down()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    #중간
    t.up()
    t.goto(x,y+150)
    t.down()
    
    t.left(30)
    t.forward(90); t.forward(-90)
    t.right(30); t.left(150)
    t.forward(90); t.forward(-90)
    t.right(150)
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    #마지막
    t.up()
    t.goto(x,y+50)
    t.down()

    t.begin_fill()
    t.circle(75)
    t.end_fill()



for i in range(3):
    x = 250 * i
    y = 0
    draw_snowman(x,y)
