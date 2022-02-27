def Timestone(hour,min):
    aftermin = (60 + min) - 45
    if aftermin >= 60:
        aftermin -= 60
    if min < 45:
        hour -= 1
    print(str(hour) + ":" + str(aftermin))




alarm = input("상근이가 기존에 정한 알람시간을 입력\n")
clock = alarm.split(" ")
hour = int(clock[0])
min = int(clock[1])
Timestone(hour,min)