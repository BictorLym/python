#사용자로부터 두 개의 정수를 받아서 정수의 합, 정수의 차, 정수의 곱, 정수의 평균,
#작은 수를 계산하여 화면에 출력하는 프로그램을 작성하라
#파이썬이 제공하는 내장 함수 max(x, y), min(x, y)를 사용해보자

a = int(input("첫 번쨰 정수를 입력하세요: "))
b = int(input("두 번쨰 정수를 입력하세요: "))
sum = a + b
sub = a - b
mul = a * b
avg = (a+b) / 2
minimum = min(a, b)
maximum = max(a, b)
print(f"정수의 합{sum}")
print(f"정수의 차{sub}")
print(f"정수의 곱{mul}")
print(f"정수의 평균{avg}")
print(f"최솟값 {minimum}")
print(f"최댓값 {maximum}")
