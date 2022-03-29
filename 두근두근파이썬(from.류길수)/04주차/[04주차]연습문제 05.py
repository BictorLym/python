#사용자가 입력한 기호 안에 문자열을 삽입하려면 어떻게 해야 하는가? 기호는 문자 2개로 이루어져있다고 가정한다.

input1 = input("기호를 입력하세요: ")
input2 = input("중간에 삽입할 문자열을 입력하시오: ")

res = input1[0:1] + input2 + input1[-1:]
print(res)
