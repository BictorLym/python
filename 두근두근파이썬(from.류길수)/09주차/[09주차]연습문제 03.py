contact = {}

while True:
    name = input("(입력모드)이름을 입력하시오: ")
    if not name:
        break;
    tel = input("전화번호를 입력하시오: ")
    contact[name] = tel


while True:
    searchName = input("검색모드)이름을 입력하시오: ")
    searchTel = contact[searchName]
    print(f"{searchName}의 번호는 {searchTel}입니다.")

