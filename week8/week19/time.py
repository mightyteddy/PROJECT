class Time:
    def __init__(self, hour, minute, second, clock):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clock =

    def isTimeValid(self, hour, minute, second):
        if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59:
            return True

    def fromString(self, clock):
        clock = clock.split(":")
        time = clock[0]
        minute = clock[1]
        second = clock[2]
        return [time, minute, second]






timeString = input("시간 입력\n")
t = Time.fromString(timeString)
if Time.isTimeValid(t):
    print(t.hour, t.minute, t.second)
else:
    print("잘못된 시간 형식입니다.")