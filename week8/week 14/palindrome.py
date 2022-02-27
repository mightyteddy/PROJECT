def Palindrome(word):
    for i in range(len(word)):
        if word[i] != word[(len(word) - i - 1)]:
            return False
    return True




word = input("영단어를 입력해주세요.\n")
if Palindrome(word):
    print(word + "은(는) palindrome입니다!")
else:
    print(word + "은(는) palindrome이 아닙니다!")