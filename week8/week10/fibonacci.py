def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

num = int(input("숫자 입력\n")) + 1
for i in range(num):
    print(fibonacci(i))