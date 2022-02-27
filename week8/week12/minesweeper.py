import random as ran
import time

def opening():
    print("지금부터 지뢰찾기를 시작합니다.\n")
    print("문자열 지뢰찾기의 규칙을 들으려면 1, 건너뛰시려면 0을 눌러주세요.\n")
    while True:
        wantRule = int(input("0 또는 1을 입력해주세요: \n"))
        if wantRule == 1:
            rule1()
        elif wantRule == 0:
            print("설명을 건너 뛰셨습니다.\n")
        else:
            print("잘못 입력하셨습니다. 다시 한번 입력해주세요.\n")
            continue

        hang = int(input("몇행으로 할까요?\n"))
        line = int(input("몇열로 할까요?\n"))
        return hang, line, wantRule


def rule1():
    print("먼저 지뢰판의 행과 열을 설정합니다.\n")
    print("예를 들어 행을 3, 열을 4로 입력하시면 다음과 깉은 판이 출력됩니다.\n")
    print("∇∇∇∇\n∇∇∇∇\n∇∇∇∇")
    print("행과 열이 너무 크면 출력이나 실행에 문제가 생길 수 있습니다.\n")


def rule2():
    print("지뢰판이 출력된 후, 몇행,몇열의 칸을 조사하거나 깃발을 꽂을 수 있습니다.\n")
    print("예를 들어 2행의 3열을 조사하기로 선택헀을때,\n")
    print("∇∇∇∇\n∇∇1∇\n∇∇∇∇\n")
    print("이 출력됩니다.\n")
    print("만약 2행의 3열에 깃발을 꽂기로 선택했을 때,\n")
    print("∇∇∇∇\n∇∇¤∇\n∇∇∇∇\n")
    print("가 출력됩니다.\n")
    print("모든 지뢰가 있는 곳에 깃발을 꽂으면 승리합니다.\n")


def difficulty():
    print("난이도 선택에 따라 지뢰의 개수가 변경됩니다.\n")
    print("난이도 1이면 약 5%±a, 난이도 9면 약45%±a 정도가 지뢰로 깔려있게 됩니다.\n")
    print("게임의 난이도를 선택해주세요.\n")
    difficult = int(input("1(매우쉬움) ~ 9(매우어려움)\n"))
    return difficult


def HowManyMine(n):
    mineMax = int((n * 3) * (hang * line) / 100 + 1)
    mineMin = int(((n - 1) * 3) * (hang * line) / 100 + 1)
    mine = ran.randint(mineMin, mineMax)
    return mine


def mineGenerator(gameBoard, mine):
    attempt = 0
    # for i in range(line):
    #     print(gameBoard[i])
    while attempt < mine:
        # print("함")
        re = False
        ranHang = ran.randrange(0, hang)
        ranLine = ran.randrange(0, line)
        # print("ranHang: " + str(ranHang) + " ranLine: " + str(ranLine))
        if gameBoard[ranHang][ranLine] == -1:
            # print("됨")
            re = True
        else:
            gameBoard[ranHang][ranLine] = -1
        if not re:
            attempt += 1


def makeBoard(hang, line):
    gumsa = [-1, 0, 1]
    for i in range(hang):
        for j in range(line):
            mineCount = 0
            if gameBoard[i][j] == -1:
                continue
            for m in gumsa:
                for n in gumsa:
                    # if not ((0 <= i + m < line) and (0 <= j + n < hang)):
                    if (i + m < 0) or (i + m >= hang) or (j + n < 0) or (j + n >= line):
                        continue
                    if gameBoard[i + m][j + n] == -1:  # 선택한 곳 주변 조사하는 코드
                        mineCount += 1
            gameBoard[i][j] = mineCount

def playAgain():
    replay = input("다시 플레이 하시겠습니까?\n 예\n 아니요\n")
    if replay == "예":
        return True
    else:
        return False

def search(h, l):
    side = [-1,0,1]
    youDied = False
    playerboard[h][l] = gameBoard[h][l]
    if playerboard[h][l] > 0:
        return

    elif playerboard[h][l] == 0:
        for i in side:
            for j in side:
                if (h + i < 0) or (h + i >= hang) or (l + j < 0) or (l + j >= line):
                    continue
                if playerboard[h + i][l + j] == "∇":
                    search(h + i, l + j)

    elif playerboard[h][l] == -1:
        playerboard[h][l] = '*'
        youDied = True

    return youDied

def flag(h,l): #깃발 꽂는 함수
    if playerboard[h][l] == "∇":
        playerboard[h][l] = "∬"
    elif playerboard[h][l] == "∬":
        playerboard[h][l] = "∇"

def Victory(usedTime):
    print("승리! 지뢰가 아닌 모든 타일을 밝혀냈습니다.")
    print("걸린 시간:" + str(usedTime))
    return playAgain()


while True:
    hang, line, wantRule = opening()
    youDied = False
    difficult = difficulty()

    if wantRule == 1:
        rule2()
    mine = HowManyMine(difficult)
    print("지뢰는 총" + str(mine) + "개 입니다.\n")
    gameBoard = [[0 for i in range(line)] for i in range(hang)]
    playerboard = [["∇" for i in range(line)] for i in range(hang)]
    mineGenerator(gameBoard, mine)
    makeBoard(hang, line)
    start = time.time()
    victoryPoint = 0
    while True:

        if youDied:
            for i in range(hang):
                for j in range(line):
                    print(playerboard[i][j], end="  ")
                print()
            print("G A M E O V E R")
            replay = playAgain()
            if replay:
                break
            exit(0)

        for i in range(hang):
            for j in range(line):
                print(playerboard[i][j], end="  ")
            print()

        for i in range(hang):
            for j in range(line):
                if playerboard[i][j] != "∇" and playerboard[i][j] != "∬":
                    victoryPoint += 1
        if victoryPoint == (hang * line) - mine:
            end = time.time()
            usedTime = end - start
            replay = Victory(usedTime)
            if replay:
                break
            exit(0)




        victoryPoint = 0
        choice = int(input("조사하고 싶으면 1을, 깃발을 꽂고 싶으면 2를 입력해주세요.\n"))

        if choice == 1:
            while True:
                searchHang = int(input("몇 행을 조사 하시겠습니까?\n"))
                searchLine = int(input("몇 열을 조사 하시겠습니까?\n"))
                if 1 <= searchHang <= hang and 1 <= searchLine <= line:
                    youDied = search(searchHang-1, searchLine-1)
                    break
                else:
                    print("잘 못 입력하셨습니다. 다시 한번 입력해주세요.")

                # for i in gameBoard[hang]
                #     for

        elif choice == 2:
            while True:
                searchHang = int(input("몇 행에 깃발을 꽂으시겠습니까?\n"))
                searchLine = int(input("몇 열에 깃발을 꽂으시시겠습니까?\n"))
                if 1 <= searchHang <= hang and 1 <= searchLine <= line:
                    youDied = flag(searchHang-1, searchLine-1)
                    break
                else:
                    print("잘 못 입력하셨습니다. 다시 한번 입력해주세요.")

        else:
            print("다시 한번 입력해주세요.\n")