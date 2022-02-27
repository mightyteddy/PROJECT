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
    queenBoard = [i for i in range(n)]  # 실제 퀸 위치
    ran.shuffle(queenBoard)
    while True:
        minimum = 99999
        minCoordinate = ["@", "@"]
        chessBoard = [["@" for i in range(n)] for i in range(n)] # 퀸이 해당 위치에서 잡아먹는 퀸의 숫자
        howManyQueenEaten = 0
        for y in range(n):
            for x in range(n):
                tempQueenBoard = [a for a in queenBoard]
                tempQueenBoard[y] = x
                for i in range(n):
                    hang = tempQueenBoard[i]
                    howManyQueenEaten += murderedQueen(tempQueenBoard, hang, i)
                chessBoard[x][y] = howManyQueenEaten
                if howManyQueenEaten < minimum:
                    minimum = howManyQueenEaten
                    minCoordinate = [x,y]
                if chessBoard[x][y] == 0: #Global min인 경우
                    print(tempQueenBoard)
                    exit(0)
                temphmq = howManyQueenEaten
                howManyQueenEaten = 0
        if queenBoard[minCoordinate[1]] == minCoordinate[0]:
            print("local minimum", queenBoard, temphmq)
            break
        else:
            queenBoard[minCoordinate[1]] = minCoordinate[0]
