import math
def starMake(n):

    for i in range(n):
        first = math.ceil(n/2)
        second = math.floor(n/2)
        print("* " * first)
        if n == 1:
            continue
        print(" *" * second)


yourStar = int(input("숫자 입력\n"))
starMake(yourStar)