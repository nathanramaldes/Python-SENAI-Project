import random
jogadas=0
board=[["1","2","3"],
       ["4","5","6"],
       ["7","8","9"]]

def display_board(board):
  print("+-------+-------+-------+","|       |       |       |","|   "+board[0][0]+"   |   "+board[0][1]+"   |   "+board[0][2]+"   |","|       |       |       |", sep="\n")
  print("+-------+-------+-------+","|       |       |       |","|   "+board[1][0]+"   |   "+board[1][1]+"   |   "+board[1][2]+"   |","|       |       |       |", sep="\n")
  print("+-------+-------+-------+","|       |       |       |","|   "+board[2][0]+"   |   "+board[2][1]+"   |   "+board[2][2]+"   |","|       |       |       |", "+-------+-------+-------+", sep="\n")

def enter_move(board):
    global jogadas
    jogador = input("choose a number from 1 to 9: ")
    flag = False
    for l in range(3):
        for c in range(3):
            if jogador == board[l][c]:
                board[l][c] = "O"
                jogadas += 1
                flag = True
    if flag == False:
        print("Choose other number")
        enter_move(board)

def draw_move(board):
    global jogadas
    pc = random.randint(1, 9)
    flag = False
    for row in range(3):
        for c in range(3):
            if str(pc) == board[row][c]:
                board[row][c] = "X"
                print("The machine choose: ", pc)
                jogadas += 1
                flag = True
                break
    if flag == False:
        draw_move(board)

def victory_for(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == "X":
                return "You lose"
            if row[0] == "O":
                return 'You win!'

    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c]:
            if board[0][c] == "X":
                return "You lose"
            if board[0][c] == "O":
                return "You win!"

    if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
        if board[1][1] == "O":
            return "You win!"
        if board[1][1] == "X":
            return "You lose"

    return None

while True:
    display_board(board)
    enter_move(board)

    result = victory_for(board)
    if result:
        display_board(board)
        print(result)
        break

    if jogadas == 9:
        display_board(board)
        print("It's a draw!")
        break

    display_board(board)
    draw_move(board)

    result = victory_for(board)
    if result:
        display_board(board)
        print(result)
        break

    if jogadas == 9:
        display_board(board)
        print("It's a draw!")
        break