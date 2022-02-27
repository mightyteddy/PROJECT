def triangle(visual, length):
    if visual == 1:
        for i in range(length + 1):
            print("*" * i)

        for i in range(length - 1):
            blank = i - 1
            print("*" + " " * blank, end="")
            if i == 0:
                print()
            else:
                print("*")
    elif visual == 2:
        for i in range(length):
            print(" " * (length - (i + 1)), end="*" * (i + 1))
            print()
        for i in range(length):
            if i == length - 1:
                print("*" * length)
            else:
                print(" " * (length - (i + 1)) + "*", end="")
                if i == 0:
                    print()
                else:
                    print(" " * (i - 1) + "*")
    if visual == 3:
        for i in range(length):
            print("*" * (length - i))
        print("*" * length)
        for i in range(length - 1):
            print("*" + " " * (length - i - 3), end="")
            if i == length - 2:
                print()
            else:
                print("*")
    if visual == 4:
        for i in range(length):
            print(" " * i + "*" * (length - i))
        for i in range(length):
            if i == 0:
                print("*" * length)
            else:
                print(" " * i, end="")
                print("*" + " " * (length - i - 2), end="")
                if i == length - 1:
                    print()
                else:
                    print("*")







length = int(input("삼각형의 길이 입력\n"))
visual = int(input("삼각형의 형태 입력\n"))
triangle(visual,length)



