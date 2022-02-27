def ignite(n):
    result = 0
    if n == 0:
        return 1
    for i in range(n):
         result += ignite(i) * ignite(n-(i+1))
    return result

num = int(input("숫자 입력\n"))
print(ignite(num))