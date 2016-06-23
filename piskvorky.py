#!/usr/local/bin/python3

import os
import sys

# Global variables
g_rows = 0 # number of rows of g_board
g_cols = 0 # number of columns of g_board
g_win_len = 0 # number of pieces needed to win
g_board = [] # game board, 2D array(after initilization)


# Get size of board and number of pieces needed to win from player
def ask_rules():
    # write into globals
    global g_rows
    global g_cols
    global g_win_len
    # Read number of rows
    g_rows = input("Gimme number of rows(1-9): ")
    # Check if input is valid
    while not(g_rows.isdigit() and int(g_rows) > 0 and int(g_rows) < 10):
        print("---not a valid number---")
        g_rows = input("Gimme number of rows(1-9): ")
    # Read number of columns
    g_cols = input("Gimme number of cols(1-9): ")
    while not(g_cols.isdigit() and int(g_cols) > 0 and int(g_cols) < 10):
        print("---not a valid number---")
        g_cols = input("Gimme number of cols(1-9): ")
    # Read number of pieces needed to win
    g_win_len = input("Gimme number of pieces in line required to win(1-9): ")
    while not(g_win_len.isdigit() and int(g_win_len) > 1 and int(g_win_len) < 10):
        print("---not a valid number---")
        g_win_len = input("Gimme number of pieces in line required to win(1-9): ")
    # type conversion
    g_rows = int(g_rows)
    g_cols = int(g_cols)
    g_win_len = int(g_win_len)

    return 0

# Initialize game board with 0s
def init_board(g_board):
    for row in range(int(g_rows)): g_board += [[0]*int(g_cols)]
    return 0

# Prints g_board in simple matrix
def print_board():
    for i in range(0, (g_rows)):
        print(g_board[i])

# Draws g_board with ASCII chars
def draw_board():
    os.system("clear") # clear the terminal
    print("   ", end="") # indent
    # top line(number of column)
    for col_num in range(0,g_cols):
        print(col_num,"  ", end="")

    print("")    
    # draws game board
    for r in range(0,g_rows):
        print("  ", end="") # indent
        print("--- " * g_cols, end="") # first row separator
        print("")
        print(r,end="") # number of row
        # draws row - column separator and X or O as a player piece
        for c in range(0, g_cols):
            if(g_board[r][c] == 0):
                print("|   ", end="")
            elif(g_board[r][c] == 1):
                print("| X ", end="")
            else:
                print("| O ", end="")
        print("|", end="") # last column separator
        print("")
    print("  ", end="")
    print("--- " * g_cols, end="") # last row separator
    print("")    


# Puts new game piece on specified position
def new_piece_position():
    p_row = input("Gimme row: ")
    if (p_row == "exit"):
        exit(0)
    while not(p_row.isdigit() and int(p_row)< g_rows and int(p_row) >= 0):
        print("Not in the range of a board")
        p_row = input("Gimme row: ")

    p_col = input("Gimme col: ")
    if (p_col == "exit"):
        exit(0)
    while not(p_col.isdigit() and int(p_col)< g_cols and int(p_col) >= 0):
        print("Not in the range of a board")
        p_col = input("Gimme col: ")
    return int(p_row), int(p_col)


# Check for victory condition in East direction
def check_east(r_pos, c_pos, current_player):
    streak = 1 # sequence of same pieces
    for l in range(1, g_win_len):
        if((c_pos+l) == g_cols ): # outside of the board limits 
            return 0
        if(g_board[r_pos][c_pos+l] != current_player): # streak break
            return 0
        else: # increment streak
            streak += 1 
            if(streak == g_win_len): # victory
                return 1



# Check for victory condition in South direction
def check_south(r_pos, c_pos, current_player):
    streak = 1
    for l in range(1, g_win_len):
        if((r_pos+l) == g_rows ):
            return 0
        if(g_board[r_pos+l][c_pos] != current_player):
            return 0
        else:
            streak += 1
            if(streak == g_win_len):
                return 1


# Check for victory condition in South East direction
def check_southeast(r_pos, c_pos, current_player):
    streak = 1
    for l in range(1, g_win_len):
        if(((c_pos+l) == g_cols) or ((r_pos + l ) == g_rows) ):
            return 0
        if(g_board[r_pos+l][c_pos+l] != current_player):
            return 0
        else:
            streak += 1
            if(streak == g_win_len):
                return 1


# Check for victory condition in South West direction
def check_southwest(r_pos, c_pos, current_player):
    streak = 1
    for l in range(1, g_win_len):
        if(((c_pos-l) < 0) or ((r_pos + l ) == g_rows) ):
            return 0
        if(g_board[r_pos+l][c_pos-l] != current_player):
            return 0
        else:
            streak += 1
            if(streak == g_win_len):
                return 1


# Checks the g_board for victory condition
def check_end(current_player):
    result = 0
    FULL_BOARD = 1 # flag indicating full board
    # goes through whole g_board, checks for winning sequence in 4 directions
    for r in range(0, g_rows):
        for c in range(0, g_cols):
            # only checks for victory of the player that was on the move
            if(g_board[r][c] == current_player):
                result = check_east(r,c,current_player)
                if(result):
                    draw_board()
                    print("Player", current_player, "won!")
                    exit(0)
                result = check_south(r,c,current_player)  
                if(result):
                    draw_board()
                    print("Player", current_player, "won!")
                    exit(0)
                result = check_southeast(r,c,current_player)  
                if(result):
                    draw_board()
                    print("Player", current_player, "won!")
                    exit(0)
                result = check_southwest(r,c,current_player)  
                if(result):
                    draw_board()
                    print("Player", current_player, "won!")
                    exit(0)
            elif(g_board[r][c] == 0):
                FULL_BOARD = 0
    # if board is full game ends
    if (FULL_BOARD):
        draw_board()
        print("Board is full.")
        exit(0)


# Player 1 turn
def player1_move():
    draw_board()
    print("Player 1(x) is on the move")
    # Get position of players new piece
    p_row, p_col = new_piece_position()
    while ( g_board[int(p_row)][int(p_col)] != 0): # Position already taken
        print("Already taken")
        p_row, p_col = new_piece_position() # New positon

    g_board[p_row][p_col] = 1 # Put piece in board

    check_end(1) # Check if new piece ended game
    player2_move()

# Player 2 turn
def player2_move():
    draw_board()
    print("Player 2(o) is on the move")

    p_row, p_col = new_piece_position()
    while ( g_board[int(p_row)][int(p_col)] != 0):
        print("already taken")
        p_row, p_col = new_piece_position()

    g_board[p_row][p_col] = 2

    check_end(2)
    player1_move()
        

# Main
if __name__ == "__main__":
    # ask for game rules(board size, number of pieces required to win)
    ask_rules()
    # basic check if it is even possible to win on given board
    if(  (g_win_len > g_rows) and (g_win_len > g_cols) ):
        print("It's impossible to win on this board")
        rows, cols, win_len = ask_rules()


    init_board(g_board)

    player1_move() # Start of game
