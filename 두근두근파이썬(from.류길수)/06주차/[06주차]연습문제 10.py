import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(5):
    t.forward(100);t.right(90); t.forward(10); t.right(90); t.forward(100)
    t.left(90); t.forward(10); t.left(90);
    
