def Reverse(a,b):
    a = list(a)
    b = list(b)
    a.reverse()
    b.reverse()
    a = int("".join(a))
    b = int("".join(b))
    if a > b:
        return a
    else:
        return b

board = input("상근이가 칠판에 적은 숫자는?\n")
splitBoard = board.split(" ")
a = splitBoard[0]
b = splitBoard[1]
print(Reverse(a,b))