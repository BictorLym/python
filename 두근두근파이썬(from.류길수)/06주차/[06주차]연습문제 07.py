import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

t.right(30)
for i in range(0, 7):
    t.left(60);
    t.forward(100); t.forward(-30);
    t.left(60); t.forward(30); t.forward(-30);
    t.right(120); t.forward(30); t.forward(-30);
    t.left(60); t.forward(-70);


