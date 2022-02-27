from new import Chess, isOk

n = 0

def DFS(parentChessBoard):
    if parentChessBoard.howManyQueen == n:
        print(parentChessBoard.queen)
        return
    for i in range(n):
        if isOk(parentChessBoard.queen, i, parentChessBoard.howManyQueen):
            childChessBoard = Chess(n)
            childChessBoard.copyQueen(parentChessBoard.queen)
            childChessBoard.howManyQueen = parentChessBoard.howManyQueen + 1
            childChessBoard.queen[parentChessBoard.howManyQueen] = i
            DFS(childChessBoard)

def main():
    global n
    n = int(input("insert 'n' to generate n*n chess board\n"))
    chessBoard = Chess(n)
    DFS(chessBoard)



if __name__ == "__main__":
    main()
