#사용자로부터 3개의 숫자를 받아서 평균을 계산하고 결과를 출력하는 프로그램 작성
a = int(input("첫 번째 숫자를 입력하시오: "))
b = int(input("두 번째 숫자를 입력하시오: "))
c = int(input("세 번째 숫자를 입력하시오: "))
average = (a+b+c)/3
print(f"{a} {b} {c}의 평균은 {average} 입니다.")
