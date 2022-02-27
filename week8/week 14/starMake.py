HowManyStar = int(input("숫자 입력.\n"))

for i in range(HowManyStar):
    Blank1 = (HowManyStar * 2) - (3 + (2 * i))
    if i == 0:
        print("*" * HowManyStar + " " * (Blank1) + "*" * HowManyStar)
    elif i == HowManyStar - 1:
        print(" " * i + "*" + " " * (HowManyStar - 2) + "*" + " " * (HowManyStar - 2) + "*")
    else:
        print(" " * i + "*" + " " * (HowManyStar - 2) + "*" + " " * Blank1 + "*" + " " * (HowManyStar - 2) + "*")

for i in range(HowManyStar - 1):
    Blank2 = 1 + (i * 2)
    if i == HowManyStar - 2:
        print("*" * HowManyStar + " " * (Blank2) + "*" * HowManyStar)
    else:
        print(" " * (HowManyStar - (i + 2)) + "*" + " " * (HowManyStar - 2) + "*" + " " * Blank2 + "*" + " " * (HowManyStar - 2) + "*")