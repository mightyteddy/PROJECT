def star(n):
    for i in range(n):
        if i == 0 or i % 2 == 0:
            print("* " * n)
        else:
            print(" *" * n)


num = int(input("숫자 입력\n"))
star(num)