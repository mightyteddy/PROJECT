num = 0
lottoNum = []
import random as ran
while num <= 6:
    re = False
    yourNum = ran.randint(1, 99)
    for i in lottoNum:
        if yourNum == i:
            re = True
            break
    if re:
        continue
    lottoNum.append(yourNum)
    num += 1

print(lottoNum)

