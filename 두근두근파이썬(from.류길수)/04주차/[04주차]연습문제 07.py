#사용자가 입력하는 3가지 색상을 리스트에 저장하였다가 하나씩 꺼내서 그 색상으로 치워진 원을 그리는 프로그램을 작성해보자. 반복문은 사용하지 않는다. 채워진 원을 그리려면 다음과 같은 문장들을 사용한다.
import turtle
t = turtle.Turtle()
t.shape("turtle")

list = []
a = input("색상 #1을 입력하시오: ")
b = input("색상 #2을 입력하시오: ")
c = input("색상 #3을 입력하시오: ")

list.append(a)
list.append(b)
list.append(c)

t.fillcolor(list[0])
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(100, 0)
t.pendown()

t.fillcolor(list[1])
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(200, 0)
t.pendown()

t.fillcolor(list[2])
t.begin_fill()
t.circle(50)
t.end_fill()




