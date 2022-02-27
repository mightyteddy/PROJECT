class Chess:
    def __init__(self, n):
        self.queen = ["@" for i in range(n)]
        self.howManyQueen = 0

    def copyQueen(self, parent):
        for i in range(len(parent)):
            self.queen[i] = parent[i]

#자식 체스판의 퀸의 좌표 x는 몇번쨰 가로줄인지 y는 몇번째 세로줄 인지
def isOk(queen, x, y): #queen은 부모 체스판
    for i in range(y): # 부모 체스판의 i번째 세로줄 퀸과 비교
        if queen[i] == x:
            return False
        if abs(y - i) / abs(x - queen[i]) == 1:
            return False
    return True


def bfs(n):
    queue = []
    # 0번쨰 세로줄에 퀸 놓기
    for i in range(n):  # 0123 가로줄
        chessBoard = Chess(n)
        chessBoard.queen[0] = i
        chessBoard.howManyQueen = 1
        queue.append(chessBoard)

    # 자식 생성(1,2,3째 세로줄에 퀸 놓기)
    while len(queue) > 0:
        adultChessBoard = queue.pop(0)
        for i in range(n):
            if isOk(adultChessBoard.queen, i, adultChessBoard.howManyQueen):    # childChessBoard n개 만들기
                childChessBoard = Chess(n)
                childChessBoard.copyQueen(adultChessBoard.queen)
                childChessBoard.queen[adultChessBoard.howManyQueen] = i
                childChessBoard.howManyQueen = adultChessBoard.howManyQueen + 1
                if childChessBoard.howManyQueen == n:
                    print(childChessBoard.queen)
                    return
                queue.append(childChessBoard)




