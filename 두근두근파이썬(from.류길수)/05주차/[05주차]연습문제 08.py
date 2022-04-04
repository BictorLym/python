#8
#사용자로부터 2개의 원에 대한 정보를 받아서 화면에 원을 그린후에 조건문을 사용하여 큰 원 안에 작은 원이 포함되는지를 판단하는 프로그램을 작성할
import turtle
t = turtle.Turtle()

x1 = int(input("큰원의 중심좌표 x1:"))
y1 = int(input("큰원의 중심좌표 y1:"))
big_radius = int(input("큰 원의 반지름:"))
x2 = int(input("작은 원의 중심좌표 x2:"))
y2 = int(input("작은 원의 중심좌표 y2:"))
small_radius = int(input("작은 원의 반지름:"))

distance =((x1-x2)**2 + (y1-y2)**2)**0.5

print(distance)

t.up()
t.goto(x1, y1)
t.down()
t.circle(big_radius)

t.up()
t.goto(x2, y2)
t.down()
t.circle(small_radius)

if(distance < big_radius-small_radius):
    t.write("작은 원이 큰 원의 내부에 있습니다.")
elif(distance == (big_radius-small_radius)):
     t.write("작은 원이 큰 원에 걸쳐 있습니다.")
else:
     t.write("작은 원이 큰 원 외부에 있습니다.")
     
