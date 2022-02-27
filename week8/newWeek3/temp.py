import random as ran
def murderedQueen(queenBoard, x, y):
    howManyQueenEaten = 0
    for i in range(n):
        if queenBoard[i] == x:
            howManyQueenEaten += 1
        elif abs(y - i) / abs(x - queenBoard[i]) == 1:
            howManyQueenEaten += 1
    return howManyQueenEaten - 1

n = int(input("insert 'n' to generate n*n chess board\n"))
while True:
    chessBoard = [["@" for i in range(n)] for i in range(n)] # 퀸이 해당 위치에서 잡아먹는 퀸의 숫자
    queenBoard = [i for i in range(n)] # 실제 퀸 위치
    howManyQueenEaten = 0
    ran.shuffle(queenBoard)
    for k in range(n):
        for i in range(n):

            for j in range(n):
                tempQueenBoard = [l for l in queenBoard]
                tempQueenBoard[k] = i
                hang = tempQueenBoard[j]
                howManyQueenEaten += murderedQueen(tempQueenBoard, hang, k)
            chessBoard[i][queenBoard[hang]] = howManyQueenEaten
            howManyQueenEaten = 0
            print(chessBoard[i][queenBoard[hang]])
            print(queenBoard)
            exit(0)


    #     hang = queenBoard[i]
    #     howManyQueenEaten += murderedQueen(queenBoard, hang, i)
    # chessBoard[i][queenBoard[hang]] = howManyQueenEaten
