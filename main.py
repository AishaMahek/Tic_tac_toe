def print_board(board):
    print(f"{board[0]} | {board[1]}  | {board[2]}")
    print("--------------")
    print(f"{board[3]} | {board[4]}  | {board[5]}")
    print("--------------")
    print(f"{board[6]} | {board[7]}  | {board[8]}")

board = ["0","1","2",
         "3","4","5",
         "6","7","8"]

print("===WELCOME TO TICTACTOE===")
print_board(board)

wc = [
    [0,1,2],[0,4,8],[2,4,6],
    [0,3,6],[1,4,7],[2,5,8],
    [3,4,5],[6,7,8]
]

def win(p):
    for c in wc:
        if (board[c[0]] == p and
            board[c[1]] == p and
            board[c[2]] == p):
            return True
    return False

m = 0
while m < 9:
    p = int(input("Player X, enter the pos (0-8): "))
    board[p] = "X"
    print_board(board)
    m += 1
    if win("X"):
        print("X won!!!")
        break
    if m == 9:
        print("Draw")
        break

    p = int(input("Player O, enter the pos (0-8): "))
    board[p] = "O"
    print_board(board)
    m += 1
    if win("O"):
        print("O won!!!")
        break
