print("시험점수를 입력하시오")
scienceScore = []
socialScore = []
for i in range(4):
    science = int(input("\n"))
    scienceScore.append(science)
for i in range(2):
    social = int(input("\n"))
    socialScore.append(social)

socialScore.sort()
scienceScore.sort()

total = scienceScore[3] + scienceScore[2] + scienceScore[1] + socialScore[1]
print(total)
