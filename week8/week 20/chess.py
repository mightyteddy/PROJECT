def write(n, queen):
    print(queen)

class Chess:
    def __init__(self, n):
        self.queen = [0 for i in range(n+1)]
        self.level = 0

    def copy_queen(self, parent):
        for i in range(len(parent)):
            self.queen[i] = parent[i]

#체스판의 (x,y) 좌표에 퀸을 놓아도 될지
def isOk(queen, x, y):  # 각 column별 퀸의 나를 잡아 먹을지
    for y_ in range(1, y):
        x_ = queen[y_]
        if x_ == x:
            return False
        elif abs(y-y_) / abs(x-x_) == 1:
            return False
    return True

def bfs(n):
    q = []

    for i in range(1, n+1):
        board = Chess(n)
        board.queen[1] = i
        board.level = 1
        if n == 1:
            board.queen.pop(0)
            write(n, board.queen)
            return
        else:
            q.append(board)

    while len(q) != 0:
        board = q.pop(0)

        for i in range(1, n+1):
            child = Chess(n)
            child.level = board.level + 1
            child.copy_queen(board.queen)

            if isOk(child.queen, i, child.level):
                child.queen[child.level]= i

                if child.level == n:
                    child.queen.pop(0)
                    write(n, child.queen)
                    return
                else:
                    q.append(child)

bfs(10)