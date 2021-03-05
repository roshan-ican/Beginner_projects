board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

#if game is still going
game_still_going = True

#who won? or Tie?
winner = None

#whos turn is it
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    #display intial_board
    display_board()
    #while game is still go
    while game_still_going:

        #handle a single of an arbitary player
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()

        #flip to the other player
        flip_player()

    #the game has ended
    if winner == "X" or winner == "0":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


#handle a single turn of an arbitary player
def handle_turn(player):

    print(player + "s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player

    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():

    global winner

    #check rows
    row_win = check_rows()
    #check coloumns
    coloumn_win = check_coloumns()
    #check diagonals
    diagonal_win = check_diagonals()

    if row_win:
        #there's a winner
        winner = row_win
    elif coloumn_win:
        #there's a winner
        winner = coloumn_win
    elif diagonal_win:
        #there's a winner
        winner = diagonal_win
    else:
        #there's no winner
        winner = None
    return


def check_rows():
    # Set up global variables
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if any row does have a match, flag that there is a winner
    if row_1 or row_2 or row_3:
        game_still_going = False
    #return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_coloumns():
    coloumn_1 = board[0] == board[3] == board[6] != "-"
    coloumn_2 = board[1] == board[4] == board[7] != "-"
    coloumn_3 = board[2] == board[5] == board[8] != "-"

    #if any column does have a match, flag that there is a winner
    if coloumn_1 or coloumn_2 or coloumn_3:
        game_still_going = False
    #return the winner
    if coloumn_1:
        return board[0]
    elif coloumn_2:
        return board[1]
    elif coloumn_3:
        return board[3]
    return


def check_diagonals():
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    #if any diagonals does have a match, flag that there is a winner
    if diagonal_1 or diagonal_2:
        game_still_going = False
    #return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_if_tie():
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    #global variables we Need
    global current_player
    #if the current_player was x, then change it to O
    if current_player == "X":
        current_player = "O"
    #if current_player was O, change it to X
    elif current_player == "O":
        current_player = "X"

    return


play_game()

#print('Hello, world!')
#board
#display board
#play game
#check win
#check rows
#check diagonals
#check coloumns
#check tie
#flip player
