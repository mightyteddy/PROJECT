def star(n):

    for i in range(1,n):
        temp = 4 * (n - i) + 1
        print("* " * (i - 1) + "*" * temp + " *" * (i - 1))
        print("* " * (i) + " " * (temp - 3) + "* " * (i))
    print("* " * ((2 * n) - 1))
    for i in range(1,n):
        temp = 4 * (i) + 1
        print("* " * (n - i) + " " * (temp - 3) + "* " * (n - i))
        print("* " * (n - i - 1) + "*" * temp + " *" * (n - i - 1))


num = int(input("숫자입력\n"))
star(num)