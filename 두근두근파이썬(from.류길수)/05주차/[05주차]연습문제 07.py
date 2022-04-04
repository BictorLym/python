#7
#2자리 숫자로 이루어진 복권이 있다. 사용자가 가지고 있는 복권 번호가 2자리 모두 일치하면 100만원을 받는다. 2자리 중에서 하나만 일치하면 50만원을 받는다. 하나도 일치하지 않으면 상금은 없다. 복권 당첨 번호는 난수로 생성하고 사용자의 입력에 따라서 상금이 얼마인지를 출력하는 프로그램을 작성하라

import random as r
input=int(input("복권 번호를 입력하시오(0에서 99사이):"))
winningNumber = r.randint(1, 99)

print("당첨번호는 %d입니다." %winningNumber)

winningNumberUnits = winningNumber % 10
winningNumberTens = winningNumber // 10
inputNumberUnits = input % 10
inputNumberTens = input // 10
if((winningNumberUnits == inputNumberUnits) and (winningNumberTens==inputNumberTens)):
   print("상금은 100만원입니다.")
elif((winningNumberUnits == inputNumberUnits) | (winningNumberTens==inputNumberTens)):
   print("상금은 50만원입니다.")
else:
    print("당첨되지 못했습니다.")
