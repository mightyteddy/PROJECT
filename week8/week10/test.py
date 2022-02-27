# def word(yourword):
#     length = len(yourword)
#     reverse = ""
#     for i in yourword:
#         reverse = i + reverse
#     return reverse
# yourword = input("로꾸거\n")
# print(word(yourword))
num = 0
even = 0
while num <= 4:
    print(str(num) + "!")
    if num % 2 == 1 or num == 0:
        num += 1
        continue
    num += 1
    even += 1

print("짝수 개수:" + str(even))






