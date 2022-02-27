def Reverse(word):
    word = list(word)
    word.reverse()
    word = "".join(word) + " "
    return word

reversedWordList = []
wordList = []
sentenceList = []
attempt = int(input("몇 문장 입력하시겠습니까?\n"))
for i in range(attempt):
    sentenceList.append(input("거꾸로 할 문장을 입력해주세요.\n"))
for i in sentenceList:
    wordList.append(i.split(" "))
for i in wordList:
    reversedWordList = []
    for j in i:
        reversedWordList.append(Reverse(j))
    print("".join(reversedWordList))