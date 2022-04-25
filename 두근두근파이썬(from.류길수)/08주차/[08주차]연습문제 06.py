def generationMathProblem():
    x = int(input("첫 번째 정수: "))
    y = int(input("두 번째 정수: "))
    ans = x+y

    print(f'정수{x}+{y}의 합은?',end='')
    userAns = int(input())
    if(userAns==ans):
        print("맞았습니다.")
    else:
        print("틀렸습니다.")

generationMathProblem()
