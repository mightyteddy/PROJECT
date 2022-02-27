def MakePassword(a,b):
    password = []
    already = False
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                password.append(a[i])
                b[j] = "ㅖ"
                break
    return password

a = input("무작위하게 영단어를 입력해주세요.\n")
b = input("무작위하게 영단어를 입력해주세요.\n")
aList = []
bList = []
for i in range(len(a)):
    aList.append(a[i])
for i in range(len(b)):
    bList.append(b[i])
print(MakePassword(aList,bList))
