#4번 문제에서 계산한 거리가 맞는지, 터틀 그래픽으로 확인해보자.
#거북이를 왼쪽으로 45도 회전하여 141만큼 전진시킨다. 다시 거북이를 (0, 0)으로
#0도를 가리키게 한 후에 100만큼 전진하고 왼쪽으로 90도 회전하여 100만큼 전진한다.
#화면에 그려진 직선이 일치하는가?

#4번 문제 코드
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
print("두 점 사이의 거리 = ",distance)
#5번 문제 코드

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.left(45)
t.forward(141)
t.right(135)
t.forward(y2-y1)
t.right(90)
t.forward(x2-x1)
t.setheading(45)
t.forward(distance)
