infile = input("입력 파일 이름: ")
outfile = input("출력 파일 이름: ")

infile = open(infile, "r")
outfile = open(outfile, "w")
sum1 = 0
k = 0

for line in infile:
    sum1 += float(line)
    k += 1

print(f"합계=" + str(sum1), file = outfile)
print(f"평균=" + str(sum1/k), file = outfile)

infile.close()
outfile.close()
print("debug")
