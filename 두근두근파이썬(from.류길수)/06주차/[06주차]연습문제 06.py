import random
n = 3
while(n>0):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    n = n-1
    print("첫번째 주사위= ", dice1,end=' ')
    print("두번째 주사위= ", dice2,end=' ')
    print()
    
