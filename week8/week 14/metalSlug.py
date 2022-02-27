def Slug(day,night,branch):
    attempt = 0
    while True:
        attempt += 1
        branch -= day
        if branch <= 0:
            print(str(attempt) + "일 걸렸습니다.")
            return
        branch += night

SlugMovingTool = input("낮 동안 올라갈 거리, 밤 동안 미끄러질 거리, 나뭇가지의 길이를 입력해주세요.\n")
SlugMovingToolList = SlugMovingTool.split(" ")
day = int(SlugMovingToolList[0])
night = int(SlugMovingToolList[1])
branch = int(SlugMovingToolList[2])
Slug(day, night, branch)