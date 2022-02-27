import random as ran

def QuizGen():
    dan = ran.randint(1,9)
    num = ran.randint(1,9)
    print(str(dan) + " * " + str(num) + " = ?")
    return dan * num

for i in range(4):
    answer = QuizGen()
    you = int(input())
    if answer == you:
        print("정답!")
    else:
        print("오답! 정답은 " + str(answer))
