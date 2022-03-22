#사용자로부터 두 점을 입력받아서 터틀 그래픽을 이용하여 두 점을 연결하는 직선을 그린다.
# 직선의 끝점에 직선의 길이를 계산하여 ㄹ출력해보자.
import turtle
t = turtle.Turtle()
t.shape("turtle")

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

t.goto(x1,y1)
t.goto(x2,y2)

distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
print("두 점 사이의 거리 = ",distance)

t.up()
t.write("점의 길이 = ", distance)
t.write(distance)
t.goto(x2,y2)
