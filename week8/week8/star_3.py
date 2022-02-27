#별짓기 3
younum = int(input("숫자 입력\n"))
level = 1
while level <= younum:
    blank = (2 * younum) - (2 * level)
    print("*" * level + " " * blank + "*" * level)
    level += 1
level -= 2
while level >= 1:
    blank = (2 * younum) - (2 * level)
    print("*" * level + " " * blank + "*" * level)
    level -= 1

