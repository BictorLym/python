filename = input("파일 이름을 입력하시오: ")
infile = open(filename,'r')
count = 0
for line in infile:
    line = line.rstrip()
    for s in line:
        count +=1

print("파일 안에는 총 %s 개의 글자가 있습니다." %count)
