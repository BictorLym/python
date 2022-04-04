#4
#학생의 시험 점수를 물어보고 시험점수가 90점 이상이면 A,
#80점 이사이면 B, 70점 이상이면 C, 60점 이상이면 D
#그 외의 점수이면 F를 학점으로 주는 프로그램을 작성하라

input = int(input("성적을 입력하세요: "))

if(input >=90):
    print("A학점입니다.")
elif(input>=80 & input <90):
    print("B학점입니다.")
elif(input>=70 & input <80):
    print("C학점입니다.")
elif(input>=60 & input <70):
    print("D학점입니다.")
else:
    print("F학접입니다.")
