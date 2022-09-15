# Name: James Roy
# Date: 9/15/2022
# Assignment: W01 Prove; Tic-Tac-Toe
# Description: Allows two players to play tic-tac-toe on a 3x3 board

import math

def drawBoard(board_list):
    for i in range(9):
        print(board_list[i], end="")
        if (i+1) % 3 != 0:
            print("|", end="")
        elif (i+1) % 3 == 0 and i != 8:
            print("\n-+-+-")
    print("\n")
    pass

def playerTurn(board_list, player):
    turn_over = False

    while not(turn_over):
        move = int(input(player + "\'s turn to choose a square (1-9): "))
        try:
            board_list[move-1] = player
        except: 
            print("Invalid Selection")
        else:     
            if not(isinstance(board_list[move-1], str)):
                turn_over = True
            else:
                print("Invalid Selection")
    pass

def checkWin(board_list):

    #Check horizontal win conditions
    if board_list[0] == board_list[1] == board_list[2]:
        return True
    if board_list[3] == board_list[4] == board_list[5]:
        return True
    if board_list[6] == board_list[7] == board_list[8]:
        return True

    #Check vertical win conditions
    if board_list[0] == board_list[3] == board_list[6]:
        return True
    if board_list[1] == board_list[4] == board_list[7]:
        return True
    if board_list[2] == board_list[5] == board_list[8]:
        return True

    #Check diagonal win conditions
    if board_list[0] == board_list[4] == board_list[8]:
        return True
    if board_list[2] == board_list[4] == board_list[6]:
        return True
    
    return False


def checkDraw(board_list):
    for i in board_list:
        if isinstance(board_list[i], int):
            return False
    return True

def main():
    game_over = False
    player_1 = "x"
    player_2 = "o"
    board_list = [1, 2, 3,
                    4, 5, 6,
                    7, 8, 9]

    while not(game_over):
        drawBoard(board_list)
        playerTurn(board_list, player_1)
        if checkWin(board_list):
            game_over = True
            print(player_1 + " wins!")
        elif checkDraw(board_list):
            game_over = True
            print("It's a draw!")
        playerTurn(board_list, player_2)
        if checkWin(board_list):
            game_over = True
            print(player_2 + " wins!")


if __name__ == "__main__":
    main()
