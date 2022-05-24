from turtle import *

class Car():
    def __init__(self):
        self.t = Turtle()
    def shape(self, x):
        self.t.shape(x)
    def move(self, x):
        if x==up:
            self.t.setheading(90)
            self.t.forward(10)
        elif x==down:
            self.t.setheading(270)
            self.t.forward(10)
        elif x==right:
            self.t.setheading(0)
            self.t.forward(70)
        elif x==left:
            self.t.setheading(180)
            self.t.forward(70)

t1 = Car()
t1.shape("turtle")
t1.move(right)
t1.move(down)
t1.move(right)

t2 = Car()
t2.shape("circle")
t2.move(left)
t2.move(up)
t2.move(left)

        
