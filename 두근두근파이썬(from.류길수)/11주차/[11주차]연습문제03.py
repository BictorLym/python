file_name = input("입력 파일 이름: ")
infile = open(file_name, "r")

cnt_dict = {}
for line in infile:
    for ch in line:
        if ch.isalpha():
            if ch in cnt_dict:
                cnt_dict[ch] += 1
            else:
                cnt_dict[ch] = 1

print(cnt_dict)
infile.close()
