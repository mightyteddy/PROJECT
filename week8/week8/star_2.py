#별짓기 2
younum = int(input("숫자 입력\n"))
level = 1
while level <= younum:
    blank = younum - level
    print(" " * blank + "*" * level)
    level += 1
level -= 2
while level >= 1:
    blank = younum - level
    print(" " * blank + "*" * level)
    level -= 1


