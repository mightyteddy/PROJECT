#별짓기 1
younum = int(input("숫자 입력\n"))
level = 1

while level <= younum:
    blank = level - 2
    print("*", end= "")
    if level == younum:
        print("*" * blank, end="")
    else:
        print(" " * blank, end= "")
    if level == 1:
        print("")
    else:
        print("*")
    level += 1
