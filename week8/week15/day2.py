def bubbleSort(num):
    out = True
    while True:

        if not out:
            break
        out = False
        for i in range(len(num)):
            if i == len(num) - 1:
                break
            if int(num[i][1]) < int(num[i + 1][1]):
                temp = num[i]
                num[i] = num[i + 1]
                num[i + 1] = temp

                out = True
    return num

tempList = []
timeList = []
works = int(input("해야 하는 일들의 개수를 입력\n"))
workList = []
print("걸리는 시간, 끝내야 하는 시간 입력")
for i in range(works):
    workTime = input()
    tempList = (workTime.split(" "))
    timeList.append(tempList)
timeList = bubbleSort(timeList)
for i in range(works):
    if i == works - 1:
        break
    endTime = int(timeList[i][1]) - int(timeList[i][0])
    if endTime < int(timeList[i + 1][1]):
        timeList[i + 1][1] = str(endTime)
wakeUp = int(timeList[works - 1][1]) - int(timeList[works - 1][0])
if wakeUp < 0:
    print("-1")






