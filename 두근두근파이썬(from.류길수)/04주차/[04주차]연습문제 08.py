#사용자가 입력하는 3개의 좌표 (x, y)를 리스트에 저장한다. 이들 좌표를 꺼내서 거북이를 이동하는 프로그램을 작성해보자.
import turtle as t
t.shape("turtle")

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))

list1 = [x1, y1]
list2 = [x2, y2]
list3 = [x3, y3]

t.goto(list1)
t.goto(list2)
t.goto(list3)
