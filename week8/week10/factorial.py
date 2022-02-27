def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

yourNum = int(input("숫자 입력\n"))

print(str(yourNum) + "! = " + str(factorial(yourNum)))

# factorial(3): # 6
#     if n == 1:
#         return 1
#     return 3 * factorial(2) #2
#                     if n == 1:
#                         return 1
#                     return 2 * factorial(1) # 1
#                                     if n == 1:
                                        # return 1
