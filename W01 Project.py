# Name: James Roy
# Date: 9/15/2022
# Assignment: W01 Prove; Tic-Tac-Toe
# Description: Allows two players to play tic-tac-toe on a 3x3 board
 
import math

#Iterates through board_list and adds formatting to draw the game board
def drawBoard(board_list):
    for i in range(9):
        print(board_list[i], end="")
        if (i+1) % 3 != 0:
            print("|", end="")
        elif (i+1) % 3 == 0 and i != 8:
            print("\n-+-+-")
    print("\n")
    pass

#Gets and validates player input for next move, changes the board_list to reflect move
def playerTurn(board_list, player):
    turn_over = False
    while not(turn_over):
        move = input(player + "\'s turn to choose a square (1-9): ")
        try:
            if type(board_list[int(move)-1]) == int:
                board_list[int(move)-1] = player
                turn_over = True            
            else:
                print("Invalid Selection: Square is already filled")
        except:
            print("Invalid Selection: Input is invalid or out of range")    
    pass

#Checks all win conditions
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

#Iterates through board_list. If an open (int) space is found, returns false
def checkDraw(board_list):
    for i in range(len(board_list)):
        if type(board_list[i]) ==  int:
            return False
    return True

#Runs the game
def main():
    #Set initial parameters
    game_over = False
    player_1 = "x"
    player_2 = "o"
    board_list = [1, 2, 3,
                    4, 5, 6,
                    7, 8, 9]
    #Draw board
    drawBoard(board_list)
    #Game loop: Players take turns, board redrawn and checked for end conditions after each move
    while not(game_over):
        playerTurn(board_list, player_1)
        drawBoard(board_list)
        if checkWin(board_list):
            game_over = True
            print(player_1 + " wins!")
            break
        elif checkDraw(board_list):
            game_over = True
            print("It's a draw!")
            break
        playerTurn(board_list, player_2)
        drawBoard(board_list)
        if checkWin(board_list):
            game_over = True
            print(player_2 + " wins!")
            break

if __name__ == "__main__":
    main()