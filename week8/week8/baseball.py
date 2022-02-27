import random as ran

while True:
    real_num = str(ran.randint(100, 999))
    real_list = []
    replay = False
    for i in real_num:
        real_list.append(i)
    if real_list[0] == real_list[1] or real_list[1] == real_list[2] or real_list[2] == real_list[0]:
        continue
    print(real_num)
    print("S T A R T")
    while not replay:
        strike = 0
        ball = 0
        print("===================")

        while True:
            your_num = input("숫자 입력 (중복된 숫자X)\n")
            your_list = []
            for i in your_num:
                your_list.append(i)
            if your_list[0] == your_list[1] or your_list[1] == your_list[2] or your_list[2] == your_list[0]:
                print("중복된 숫자는 입력하실 수 있습니다")
                print("===================")
            else:
                break

        for i in range(3):
            if your_list[i] == real_list[i]:
                strike += 1
            elif your_list[i] in real_list:
                ball += 1
        print("STRIKE: " + str(strike) + "/BALL: " + str(ball))
        if strike == 3:
            re = input("승리!\n다시 플레이 하시겠습니까?\n0. 예\n1. 아니요\n")
            if re == "0":
                replay = True
                break
            else:
                exit(0)
