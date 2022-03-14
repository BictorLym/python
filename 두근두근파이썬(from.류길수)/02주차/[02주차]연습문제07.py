#다음과 같은 그림을 그리는 프로그램을 작성하시오
#이떄 작은 사각형의 한 변의 길이는 side변수에 저장하고
#거북이가 회전하는 각도는 angle변수에 저장한다.
import turtle as t
t.shape("turtle")
side = 50

for i in range(0, 4):
    t.forward(side)
    t.right(90)
for i in range(0, 4):
    t.forward(side)
    t.left(90)
t.right(180)
for i in range(0, 4):
    t.forward(side)
    t.right(90)
for i in range(0, 4):
    t.forward(side)
    t.left(90)
t.left(90)
