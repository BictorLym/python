list = []
for i in range (5):
    x = int(input("정수를 입력하시오: "))
    list.append(x)
sum = 0
for i in range (len(list)):
    sum += list[i]
avg = sum/len(list)
print(f"평균= {avg}")
