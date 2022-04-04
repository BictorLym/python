#5
#난수를 사용하여 1부터 100사이의 숫자를 사용하는 뺄셈 문제를 생성하고 사용자에게
#물어본 후에 사용자의 답변이 올바른지를 검사하는 프로그램을 작성하라
import random as r
a = r.randint(1, 100)
b = r.randint(1, 100)

ans = int(input(f"{a} - {b} = "))
if(ans==a-b):
    print("맞았습니다.")
else:
    print("틀렸습니다.")
