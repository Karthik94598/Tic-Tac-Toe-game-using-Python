import random,sys,time
n = [j for j in range(1,10)]
board = [" " for i in range(9)]
print("Tic Tac Toe")
print()
def game_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])
    print(row1)
    print(row2)
    print(row3)
def player_move(icon):
    if icon == 'X':
        number =1
    elif icon == 'O':
        number =2
    print("your turn player {}".format(number))
    choice1 = int(input("Enter your move 1-9: ").strip())
    if choice1>0 and choice1<=9:
        if board[choice1-1] == " ":
            board[choice1-1] = icon
        else:
            print()
            print("The space was taken...\U0001F643")
            print()
            player_move(icon)
    else:
        print("invalid move...\U0001F644. please enter again \U0001F60A")
        player_move(icon)
def com_move(icon):
    n1 = random.choice(n)
    print("computer turn: ")
    time.sleep(0.5)
    print(n1)
    time.sleep(1)
    if board[n1-1] ==" ":
        board[n1-1]= icon
    else:
        print()
        print("The space was taken...\U0001F643")
        print()
        com_move(icon)
def is_victory(icon):
    if board[0]==icon and board[1]==icon and board[2]==icon or\
    board[3]==icon and board[4]==icon and board[5]==icon or\
    board[6]==icon and board[7]==icon and board[8]==icon or\
    board[0]==icon and board[3]==icon and board[6]==icon or\
    board[1]==icon and board[4]==icon and board[7]==icon or\
    board[2]==icon and board[5]==icon and board[8]==icon or\
    board[0]==icon and board[4]==icon and board[8]==icon or\
    board[2]==icon and board[4]==icon and board[6]==icon:
        return True
    else:
        return False
def is_draw():
    if " " not in board:
        return True
    else:
        return False

while True:
    ch = int(input("mode you want to play \n 1. Computer Vs Player \n 2. Player Vs Player: "))
    if ch == 1:
        while True:
            game_board()
            player_move("X")
            #game_board()
            if is_victory("X"):
                print("Player X wins...congratulations\U0001F973\U0001F973\U0001F973")
                sys.exit()
            elif is_draw():
                print("It's a DRAW\U0001F928\U0001F928")
                sys.exit()
            game_board()
            com_move("O")
            #game_board()
            if is_victory("O"):
                print("Player O wins...congratulations\U0001F973\U0001F973\U0001F973")
                sys.exit()
            elif is_draw():
                print("It's a DRAW\U0001F928\U0001F928")
                sys.exit()
    elif ch == 2:
        while True:
            game_board()
            player_move("X")
            #game_board()
            if is_victory("X"):
                print("Player X wins...congratulations\U0001F973\U0001F973\U0001F973")
                sys.exit()
            elif is_draw():
                print("It's a DRAW\U0001F928\U0001F928")
                sys.exit()
            game_board()
            player_move("O")
            #game_board()
            if is_victory("O"):
                print("Player O wins...congratulations\U0001F973\U0001F973\U0001F973")
                sys.exit()
            elif is_draw():
                print("It's a DRAW\U0001F928\U0001F928")
                sys.exit()
    else:
        print("Enter Again: ")