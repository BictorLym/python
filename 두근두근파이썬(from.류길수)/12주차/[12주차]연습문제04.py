from turtle import *

class MyTurtle(Turtle):
    def __init__(self):
        self.t = Turtle()
    def drawSquare(self):
        for i in range(4):
            self.t.right(90)
            self.t.forward(100)

my_turtle = MyTurtle()
#my_turtle.forward(100)
my_turtle.drawSquare()
