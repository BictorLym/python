import random

a = random.randint(1, 10)
b = random.randint(1, 10)
mul = a*b

while(1):
    ans = int(input(str(a) + "*" + str(b) + "는"))
    if ans == mul:
        print("맞았습니다.")
        break
    
