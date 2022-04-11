import turtle

t = turtle.Turtle()
#t.shape("turtle")
t.color("red")

t.left(180)
for j in range(0,10):
    for i in range(0, 5):
        t.forward(100)
        t.right(144)
    t.left(10)
